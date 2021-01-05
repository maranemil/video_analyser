<?php

/**
 * Generate Visual Preview from Frame + Frame Top Colors
 */

# https://www.php.net/manual/en/function.glob.php
# https://www.php.net/manual/en/function.scandir.php

# $arrImg = scandir(".");
# print_r($arrImg);

// get array images top colors
foreach (glob("*.png") as $filename) {
	if(preg_match('/top_colors/', $filename)) {	
    	echo "$filename size " . filesize($filename) . "\n";
    	$arrTopColors[] = $filename;
    }
}

// get array images top frames
foreach (glob("*.jpg") as $filename) {
	if(preg_match('/xout/', $filename)) {	
    	echo "$filename size " . filesize($filename) . "\n";
    	$arrXout[] = str_replace('-xout.jpg', "", $filename) ;
    }
}

// generate html table
$strHTML = "<table>".PHP_EOL;
$strHTML .= "<tr>".PHP_EOL;
foreach($arrXout as $key => $img){
	$strHTML .= '<td><img src="'.$img.'" width=30></td>'.PHP_EOL;
}
$strHTML .= "</tr><tr>".PHP_EOL;
foreach($arrTopColors as $key => $img){
	$strHTML .= '<td><img src="'.$img.'" width=30></td>'.PHP_EOL;
}
$strHTML .= "</tr>".PHP_EOL;
$strHTML .= "</table>".PHP_EOL;
file_put_contents(__FILE__ . ".html", $strHTML);



