"""
https://towardsdatascience.com/easy-image-classification-with-tensorflow-2-0-f734fee52d13
https://github.com/cameroncruz/notebooks/blob/master/Easy_Image_Classification_with_TF_2.ipynb


https://pythonprogramming.net/color-filter-python-opencv-tutorial/
https://docs.opencv.org/3.4.2/df/d9d/tutorial_py_colorspaces.html
https://docs.opencv.org/3.4.3/da/d97/tutorial_threshold_inRange.html
https://stackoverflow.com/questions/48470671/how-does-filtering-out-the-colors-of-a-hsv-image-in-opencv-python-work
https://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/
https://medium.com/@ckyrkou/color-thresholding-in-opencv-91049607b06d
"""
# --------------------------------------------------------------------------------

import matplotlib.pyplot as plt

X = [1, 2, 3]
Y = [2, 5, 8]
Z = [6, 4, 5]
colors = ["#0000FF", "#00FF00", "#FF0066"]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(X)):
    ax.scatter(X[i], Y[i], Z[i], color=colors[i])
# plt.show()
plt.savefig("graph.png")

# --------------------------------------------------------------------------------

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pic1.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_green = np.array([0, 0, 150])
upper_green = np.array([255, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('res1.png', res)
cv2.waitKey(0)

# --------------------------------------------------------------------------------

import numpy as np
import cv2

# load your images
dolphin = cv2.imread('dolphin.png')  # use 0 for grayscale
bicycle = cv2.imread('bicycle.png')
# add them with a weight, respectively, last parameter is a scalar added
dst = cv2.addWeighted(dolphin, 0.7, bicycle, 0.3, 0)
# show
cv2.imshow('Blended Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --------------------------------------------------------------------------------


from skimage.data import camera
from skimage.filters import frangi, hessian
import matplotlib.pyplot as plt

image = camera()
fig, ax = plt.subplots(ncols=3)
ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original image')
ax[1].imshow(frangi(image), cmap=plt.cm.gray)
ax[1].set_title('Frangi filter result')
ax[2].imshow(hessian(image), cmap=plt.cm.gray)
ax[2].set_title('Hybrid Hessian filter result')
for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

with cbook.get_sample_data('grace_hopper.png') as image_file:
    image = plt.imread(image_file)
fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
im.set_clip_path(patch)
ax.axis('off')
plt.show()

# --------------------------------------------------------------------------------

from PIL import Image, ImageFilter

# Read image
im = Image.open('image.jpg')
# Display image
im.show()
# Applying a filter to the image
im_sharp = im.filter(ImageFilter.SHARPEN)
# Saving the filtered image to a new file
im_sharp.save('image_sharpened.jpg', 'JPEG')
# Splitting the image into its respective bands, i.e. Red, Green,
# and Blue for RGB
r, g, b = im_sharp.split()
# Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data

# --------------------------------------------------------------------------------

X = [1, 2, 3]
Y = [2, 5, 8]
Z = [6, 4, 5]
colors = ["#0000FF", "#00FF00", "#FF0066"]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(len(X)):
    ax.scatter(X[i], Y[i], Z[i], color=colors[i])
plt.show()

# --------------------------------------------------------------------------------

X = [0, 1, 2]
Y = [0, 1, 2]
Z = [0, 1, 2]
C = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c=C / 255.0)
plt.show()

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()  # show color scale

# --------------------------------------------------------------------------------

from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T
plt.scatter(features[0], features[1], alpha=0.2,
            s=100 * features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# --------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

x = np.arange(10)
ys = [i + x + (i * x) ** 2 for i in range(10)]
colors = cm.rainbow(np.linspace(0, 1, len(ys)))
for y, c in zip(ys, colors):
    plt.scatter(x, y, color=c)

# --------------------------------------------------------------------------------

import matplotlib
import numpy as np

X = [1, 2, 3, 4]
Ys = np.array([[4, 8, 12, 16],
               [1, 4, 9, 16],
               [17, 10, 13, 18],
               [9, 10, 18, 11],
               [4, 15, 17, 6],
               [7, 10, 8, 7],
               [9, 0, 10, 11],
               [14, 1, 15, 5],
               [8, 15, 9, 14],
               [20, 7, 1, 5]])
nCols = len(X)
nRows = Ys.shape[0]
colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(Ys)))
cs = [colors[i // len(X)] for i in range(len(Ys) * len(X))]  # could be done with numpy's repmat
Xs = X * nRows  # use list multiplication for repetition
matplotlib.pyplot.scatter(Xs, Ys.flatten(), color=cs)

# --------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from random import randint
import numpy as np

# Let's generate some random X, Y data X = [ [frst group],[second group] ...]
X = [[randint(0, 50) for i in range(0, 5)] for i in range(0, 24)]
Y = [[randint(0, 50) for i in range(0, 5)] for i in range(0, 24)]
labels = range(1, len(X) + 1)
fig = plt.figure()
ax = fig.add_subplot(111)
for x, y, lab in zip(X, Y, labels):
    ax.scatter(x, y, label=lab)
# Now this is actually the code that you need, an easy fix your colors just cut and paste not you need ax.
colormap = plt.cm.gist_ncar  # nipy_spectral, Set1,Paired
colorst = [colormap(i) for i in np.linspace(0, 0.9, len(ax.collections))]
for t, j1 in enumerate(ax.collections):
    j1.set_color(colorst[t])
ax.legend(fontsize='small')

# --------------------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
ys = [i + x + (i * x) ** 2 for i in range(10)]
plt.figure()
for y in ys:
    plt.plot(x, y, 'o')
plt.show()

# --------------------------------------------------------------------------------


df = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1], [6.4, 3.2, 1], [5.9, 3.0, 2]],
                  columns=['length', 'width', 'species'])
ax1 = df.plot.scatter(x='length', y='width', c='DarkBlue')
ax2 = df.plot.scatter(x='length', y='width', c='species', colormap='viridis')

library(plotly)
head(iris)
plot_ly(iris, x=~Petal.Length, y=~Petal.Width, type="scatter", mode="markers",
        marker=list(color="purple", size=20, opacity=0.5))
# left
plot_ly(iris, x=~Petal.Length, y=~Petal.Width, type="scatter", mode="markers", color=~Species,
        marker=list(size=20, opacity=0.5))
# right
plot_ly(iris, x=~Petal.Length, y=~Petal.Width, type="scatter", mode="markers", color=~Species, colors="Set1",
        marker=list(size=20, opacity=0.5))
# left
plot_ly(iris, x=~Petal.Length, y=~Petal.Width, type="scatter", mode="markers", marker=list(size=20, opacity=0.5),
        color=~Sepal.Length)
# right
plot_ly(iris, x=~Petal.Length, y=~Petal.Width, type="scatter", mode="markers", marker=list(size=20, opacity=0.5),
        color=~Sepal.Length, colors=c("green", "blue"))

# --------------------------------------------------------------------------------
image_path = "HOPE.png"
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot
from PIL import Image

fig = pyplot.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")  # 3D plot with scalar values in each axis
im = Image.open(image_path)
r, g, b = list(im.getdata(0)), list(im.getdata(1)), list(im.getdata(2))
axis.scatter(r, g, b, c="#ff0000", marker="o")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
pyplot.show()

# --------------------------------------------------------------------------------

import matplotlib.pyplot as plt

w = 4
h = 3
d = 70
plt.figure(figsize=(w, h), dpi=d)
plt.axis([0, 5, 0, 5])
x = [1, 2, 4]
y = [1, 3, 3]
size = 500
plt.scatter(x, y, s=size)
plt.savefig("out.png")

# --------------------------------------------------------------------------------

import PIL
from PIL import Image
from matplotlib import pyplot as plt

im = Image.open('./color_gradient.png')
w, h = im.size
colors = im.getcolors(w * h)


def hexencode(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return '#%02x%02x%02x' % (r, g, b)


for idx, c in enumerate(colors):
    plt.bar(idx, c[0], color=hexencode(c[1]))
plt.show()
for idx, c in enumerate(colors):
    plt.bar(idx, c[0], color=hexencode(c[1]), edgecolor=hexencode(c[1]))
plt.show()

# --------------------------------------------------------------------------------

import cv2
import numpy as np
from matplotlib import pyplot as plt

file0 = 'image.jpg'
img = cv2.imread(file0)
color = ('b', 'g', 'r')
plt.figure()
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()

# --------------------------------------------------------------------------------

import random


def colors(n):
    ret = []
    r = int(random.random() * 256)
    g = int(random.random() * 256)
    b = int(random.random() * 256)
    step = 256 / n
    for i in range(n):
        r += step
        g += step
        b += step
        r = int(r) % 256
        g = int(g) % 256
        b = int(b) % 256
        ret.append((r, g, b))
    return ret


def get_spaced_colors(n):
    max_value = 16581375  # 255**3
    interval = int(max_value / n)
    colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]

    return [(int(i[:2], 16), int(i[2:4], 16), int(i[4:], 16)) for i in colors]


# --------------------------------------------------------------------------------


# draw histogram in python.
import cv2
import numpy as np

img = cv2.imread('image.jpg')
h = np.zeros((300, 256, 3))
bins = np.arange(256).reshape(256, 1)
color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
for ch, col in enumerate(color):
    hist_item = cv2.calcHist([img], [ch], None, [256], [0, 255])
cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
hist = np.int32(np.around(hist_item))
pts = np.column_stack((bins, hist))
cv2.polylines(h, [pts], False, col)
h = np.flipud(h)
cv2.imshow('colorhist', h)
cv2.waitKey(0)

# --------------------------------------------------------------------------------


# convert the image to grayscale and create a histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

# --------------------------------------------------------------------------------


# convert the image to grayscale and create a histogram
import cv2
import numpy as np
from matplotlib import pyplot as plt

gray_img = cv2.imread('images/GoldenGateSunset.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('GoldenGate', gray_img)
hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.hist(gray_img.ravel(), 256, [0, 256])
plt.title('Histogram for gray scale picture')
plt.show()
while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27: break  # ESC key to exit
cv2.destroyAllWindows()

# --------------------------------------------------------------------------------


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/GoldenGateSunset.png', -1)
cv2.imshow('GoldenGate', img)
color = ('b', 'g', 'r')
for channel, col in enumerate(color):
    histr = cv2.calcHist([img], [channel], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.title('Histogram for color scale picture')
plt.show()
while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27: break  # ESC key to exit
cv2.destroyAllWindows()

# --------------------------------------------------------------------------------


# 2D Histogram in OpenCV

import cv2
import numpy as np

img = cv2.imread('home.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# 2D Histogram in Numpy

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('home.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist, xbins, ybins = np.histogram2d(h.ravel(), s.ravel(), [180, 256], [[0, 180], [0, 256]])

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('home.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist, interpolation='nearest')
plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('home.jpg', 0)
plt.hist(img.ravel(), 256, [0, 256]);
plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('home.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()

# --------------------------------------------------------------------------------

img = cv2.imread('home.jpg', 0)
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img, img, mask=mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [256], [0, 256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])
plt.show()

# --------------------------------------------------------------------------------


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('stinkbug.png')
imgplot = plt.imshow(img)
lum_img = img[:, :, 0]
plt.imshow(lum_img)
plt.imshow(lum_img, cmap="hot")
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
imgplot = plt.imshow(lum_img)
plt.colorbar()
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))

# from PIL import Image
img = Image.open('../_static/stinkbug.png')
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img)
imgplot = plt.imshow(img, interpolation="nearest")
imgplot = plt.imshow(img, interpolation="bicubic")

trace = dict(type='scatter3d',
             x=np.random.rand(25),
             y=np.random.rand(25),
             z=np.random.rand(25),
             mode='markers',
             marker=dict(
                 color=[f'rgb({np.random.randint(0, 256)}, {np.random.randint(0, 256)}, {np.random.randint(0, 256)})'
                        for _ in range(25)],
                 size=10)
             )

# --------------------------------------------------------------------------------

"""

https://www.php.net/manual/de/function.krsort.php
https://www.php.net/manual/de/function.arsort.php
https://www.php.net/manual/de/function.array-count-values.php
https://www.php.net/manual/de/function.array-values.php
https://unsplash.com/search/photos/blue-sky
https://www.php.net/manual/en/function.imagescale.php
https://www.php.net/manual/en/function.imagecopyresized.php
https://www.php.net/manual/en/function.imagecopyresized.php
https://www.php.net/manual/en/function.imagecopyresampled.php
https://canvasjs.com/php-charts/scatter-point-chart/
https://jpgraph.net/download/manuals/chunkhtml/ch15s05.html
https://jpgraph.net/

https://www.codediesel.com/php/6-excellent-charting-libraries-for-php/
https://www.edrawsoft.com/createscatterchart.php
https://demo.koolphp.net/Examples/KoolChart/ChartTypes/Scatter_Chart/index.php
https://www.fusioncharts.com/dev/chart-guide/standard-charts/select-scatter-chart
https://www.zingchart.com/docs/chart-types/scatter-plots/
http://pchart.sourceforge.net/documentation.php?topic=exemple25
https://www.highcharts.com/demo/scatter
http://www.jzy3d.org/tutorial.php
https://www.python-kurs.eu/matplotlib.php
https://matplotlib.org/users/colors.html
https://github.com/matplotlib/matplotlib/issues/5377



https://stackoverflow.com/questions/33287156/specify-color-of-each-point-in-scatter-plot-matplotlib
https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
https://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot-on-matplotlib
https://community.plot.ly/t/specifying-a-color-for-each-point-in-a-3d-scatter-plot/12652
https://franciscouzo.github.io/image_colors/
https://en.wikipedia.org/wiki/CIELAB_color_space
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
https://www.r-graph-gallery.com/121-manage-colors-with-plotly/
https://gist.github.com/Uberi/4885a318e7ef2afa7f22
https://kite.com/python/docs/matplotlib.pyplot.scatter
https://stackoverflow.com/questions/12182891/plot-image-color-histogram-using-matplotlib
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html
https://www.quora.com/How-do-I-generate-n-visually-distinct-RGB-colours-in-Python
https://pythonspot.com/image-histogram/
https://www.pyimagesearch.com/2014/01/22/clever-girl-a-guide-to-utilizing-color-histograms-for-computer-vision-and-image-search-engines/
https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_image_histogram_calcHist.php
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_2d_histogram/py_2d_histogram.html
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html
https://matplotlib.org/users/image_tutorial.html

"""
