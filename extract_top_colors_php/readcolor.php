<?php

/**
 * Flow Frame Color Extract
 */

# rm split/*.jpg
# rm split/*.png

# Genarete frames from video
# ffmpeg -i SXSW2a.mp4 -vf fps=1/120  extract_top_colors_php/out%03d.jpg

# process frame and extract colors
# for i in *.jpg; do php readcolor.php $i; done

/**
 * References
 */

# http://ld2015.scusa.lsu.edu/php/function.imagefilter.html
# https://www.php.net/manual/en/function.imagefilter.php
# https://www.hashbangcode.com/article/add-effects-images-using-image-filters-php
# https://hotexamples.com/examples/-/-/imagefilter/php-imagefilter-function-examples.html
# https://www.phpimagick.com/Imagick/modulateImage?imagePath=Lorikeet&hue=88&saturation=200&brightness=100

# https://www.php.net/manual/de/function.imagefilledrectangle.php
# https://docstore.mik.ua/orelly/webprog/php/ch09_04.htm
# https://gist.github.com/Crindigo/429474

# https://github.com/RubixML/Tensor
# https://github.com/dstogov/php-tensorflow
# https://hotexamples.com/de/examples/-/-/ImageSetPixel/php-imagesetpixel-function-examples.html

/**
 * add image saturation
 */
/*
$imagick = new \Imagick(realpath($imagePath));
$imagick->modulateImage($brightness=100, $saturation=200, $hue=88);
header("Content-Type: image/jpg");
echo $imagick->getImageBlob();
*/

// get argument image
$filename = $_SERVER['argv'][1] ? $_SERVER['argv'][1] : 'out001.jpg';
// set scale percent for resize
$percent = 0.5;

// Content type
#header('Content-Type: image/jpeg');

// calculate new sizes of thumb
list($width, $height) = getimagesize($filename);
$newWidth  = $width * $percent;
$newHeight = $height * $percent;

echo "Img Size: " . PHP_EOL;
print_r(array($width, $height));
echo "---------------------------------" . PHP_EOL;

// apply filters
$thumb  = imagecreatetruecolor($newWidth, $newHeight);
$source = imagecreatefromjpeg($filename);
imagefilter($source, IMG_FILTER_GAUSSIAN_BLUR, 220);
#imagefilter($source, IMG_FILTER_SELECTIVE_BLUR);
#imagefilter($source, IMG_FILTER_SMOOTH, 50);
#imagefilter($source, IMG_FILTER_MEAN_REMOVAL);
imagefilter($source, IMG_FILTER_CONTRAST, 220);
#imagefilter($source, IMG_FILTER_COLORIZE, 100, 0, 100);
#imagefilter($source, IMG_FILTER_NEGATE);
#imagefilter($source, IMG_FILTER_GRAYSCALE);
#imagefilter($source, IMG_FILTER_BRIGHTNESS, 50);
#imagefilter($source, IMG_FILTER_EDGEDETECT);
#imagefilter($source, IMG_FILTER_EMBOSS);
imagefilter($source, IMG_FILTER_PIXELATE, 15, true);
#imagefilter($source, IMG_FILTER_PIXELATE, 3, true);
imagejpeg($source, $filename . '-xout.jpg');
#imagedestroy($source);

// Resize
imagecopyresized($thumb, $source, 0, 0, 0, 0, $newWidth, $newHeight, $width, $height);
// get max w/h pixels from thumb
$imgw = imagesx($thumb);
$imgh = imagesy($thumb);

echo "Img Resize: " . PHP_EOL;
print_r(array($imgw, $imgh));
echo "---------------------------------" . PHP_EOL;

// n = total number or pixels
// read rbg hex colors from every pixel and store in array
$n     = $imgw * $imgh;
$histo = array();
for ($i = 0; $i < $imgw; $i++) {
   for ($j = 0; $j < $imgh; $j++) {
	  // get the rgb value for current pixel
	  $rgb = ImageColorAt($thumb, $i, $j);
	  // extract each value for r, g, b
	  $r = ($rgb >> 16) & 0xFF;
	  $g = ($rgb >> 8) & 0xFF;
	  $b = $rgb & 0xFF;
	  // get the Value from the RGB value
	  $V      = round(($r + $g + $b) / 3);
	  $arrV[] = array(
		  "r" => intval($r),
		  "g" => intval($g),
		  "b" => intval($b),
	  );
	  // $arrHex[] = sprintf("#%02x%02x%02x", $r, $g, $b);
	  // add the point to the histogram
	  // $histo[$V] += intval($V/$n);
   }
}

#print_r($arrV);
#print_r($arrHex);

// store RGB info
foreach ($arrV as $arrRGB) {
   $arrRGBs[] = $arrRGB["r"] . "-" . $arrRGB["r"] . "-" . $arrRGB["r"];
}

echo "---------------------------------" . PHP_EOL;
$countHex = array_count_values($arrRGBs);

// get Average / Max
$arReference = array_filter($countHex);
$average     = array_sum($arReference) / count($arReference);
echo "Average:" . $average . PHP_EOL;
$max = max($arReference);
echo "Max: " . $max . PHP_EOL;
echo "---------------------------------" . PHP_EOL;

// get Top colors
echo "Top colors: " . PHP_EOL;
arsort($countHex);
$top10 = array_slice($countHex, 0, 50);
print_r($top10);
echo "---------------------------------" . PHP_EOL;

// print_r( hexdec( key($top5)));
# list($r, $g, $b) = sscanf(key($top5), "#%02x%02x%02x");
# echo key($top5) . "-> $r $g $b"; // rgb color nr 1

print PHP_EOL;
imagejpeg($thumb, $filename . '-trumb.jpg');
imagedestroy($thumb);

/**
 * Create top color image spectrum
 */

$x  = 200;
$y  = 400;
$gd = imagecreatetruecolor($x, $y);
#$red = imagecolorallocate($gd, 255, 0, 0); 

$x1 = 0;
$y1 = 10;
$x2 = 70;
$y2 = 70;

foreach ($top10 as $colorx => $countcolor) {
   $arrRGBy = explode("-", $colorx);
   // Draw a square
   # imagefilledrectangle ( resource $image , int $x1 , int $y1 , int $x2 , int $y2 , int $color )
   imagefilledrectangle($gd, $x1, $y1, $x2, $y2, imagecolorallocate($gd, $arrRGBy[0], $arrRGBy[1], $arrRGBy[2]));
   $x1 = $x1 + 0;
   $y1 = $y1 + 10;
   $x2 = $x2 + 70;
   $y2 = $y2 + 70;
   /*for ($i = 0; $i < $countcolor; $i++) {
		 imagesetpixel($gd, round($x),round($y), imagecolorallocate($gd, $arrRGBy[0], $arrRGBy[1], $arrRGBy[2]));
		 $a = rand(0, 2);
		 #$x = ($x + $corners[$a]['x']) / 2;
		 #$y = ($y + $corners[$a]['y']) / 2;
		 $x++;
	   $y++;
 }*/
}

/*
for ($i = 0; $i < 100000; $i++) {
  	imagesetpixel($gd, round($x),round($y), $red);
  	$a = rand(0, 2);
  	$x = ($x + $corners[$a]['x']) / 2;
  	$y = ($y + $corners[$a]['y']) / 2;
}
*/

#header('Content-Type: image/png');
imagepng($gd, $filename . '-top_colors.png');
imagedestroy($gd);

/*
$im = ImageCreate(200,200);
$white = ImageColorAllocate($im,0xFF,0xFF,0xFF); 
$black = ImageColorAllocate($im,0x00,0x00,0x00); 
ImageFilledRectangle($im,50,50,150,150,$black); 
header('Content-Type: image/png'); 
ImagePNG($im); 
#docstore.mik.ua/orelly/webprog/php/ch09_04.htm

$im = ImageCreate(200,200); 
$white = ImageColorAllocate($im,0xFF,0xFF,0xFF); 
$black = ImageColorAllocate($im,0x00,0x00,0x00); 
ImageFilledRectangle($im,50,50,150,150,$black); 
header('Content-Type: image/jpeg'); 
ImageJPEG($im); 
#docstore.mik.ua/orelly/webprog/php/ch09_04.htm
*/

die();

// print colors in terminal
// exec("printf '\e]4;1;%s\a\e[0;41m \n\e[m' '#ff0000'");
// xlogo -bg '#ff0000'
// https://misc.flogisoft.com/bash/tip_colors_and_formatting