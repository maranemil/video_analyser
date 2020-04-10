from __future__ import print_function
import binascii
import struct
from PIL import Image,ImageEnhance
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 2

print('reading image')
im = Image.open('../split/out042.png')
converter = ImageEnhance.Color(im)
im2 = converter.enhance(2.0)
im = im2.resize((150, 150))  # optional, to reduce time
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

print('finding clusters')
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print('cluster centres:\n', codes)

vecs, dist = scipy.cluster.vq.vq(ar, codes)  # assign codes
counts, bins = np.histogram(vecs, len(codes))  # count occurrences

index_max = np.argmax(counts)  # find most frequent
peak = codes[index_max]
colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
print('most frequent is %s (#%s)' % (peak, colour))

"""
# bonus: save image using only the N most common colours
import imageio
c = ar.copy()
for i, code in enumerate(codes):
    c[scipy.r_[scipy.where(vecs==i)],:] = code
imageio.imwrite('clusters.png', c.reshape(*shape).astype(np.uint8))
print('saved clustered image')
"""


from colorthief import ColorThief
color_thief = ColorThief('../split/out003.png')
# get the dominant color
dominant_color = color_thief.get_color(quality=6)
print('most dominant color is ', dominant_color)
# top 6
palette = color_thief.get_palette(color_count=6)
print('top palette is ', palette)

from colormap import rgb2hex
import matplotlib.pyplot as plt
#import matplotlib._color_data as mcd
import matplotlib.patches as mpatch

fig = plt.figure(figsize=[4, 4])
ax = fig.add_axes([0, 0, 1, 1])
for j, ngb in enumerate(sorted(palette, reverse=True)):
    # print(rgb2hex(0, 128, 64))
    r = round(ngb[0])
    g = round(ngb[1])
    b = round(ngb[2])
    n = rgb2hex(r, g, b)
    #print(n)
    r1 = mpatch.Rectangle((0, j), 1, 1, color=n)  # #00008B
    txt = ax.text(2, j + .5, '  ' + n, va='center', fontsize=10)
    ax.add_patch(r1)
    ax.axhline(j, color='k')

ax.text(.5, j + 1.5, 'top color', ha='center', va='center')
ax.set_xlim(0, 3)
ax.set_ylim(0, j + 2)
ax.axis('off')
plt.show()

"""
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 2.5))
plt.subplot(131)
plt.imshow(im, cmap='gray')
plt.axis('off')
plt.subplot(132)
plt.imshow(im, cmap='nipy_spectral')
plt.axis('off')
plt.subplot(133)
plt.imshow(im, cmap='nipy_spectral')
plt.axis('off')
plt.tight_layout()
plt.show()
"""

"""
https://stackoverflow.com/questions/32031078/matplotlib-pcolormesh-using-rgb-tuples
https://pythoninformer.com/python-libraries/numpy/numpy-and-images/
https://stackoverflow.com/questions/7762948/how-to-convert-an-rgb-image-to-numpy-array
https://stackoverflow.com/questions/32031078/matplotlib-pcolormesh-using-rgb-tuples
https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html
https://pythoninformer.com/python-libraries/numpy/numpy-and-images/
https://matplotlib.org/3.1.1/gallery/axes_grid1/demo_axes_rgb.html
https://matplotlib.org/3.1.1/gallery/axes_grid1/demo_axes_rgb.html
https://stackoverflow.com/questions/16070078/change-saturation-with-imagekit-pil-or-pillow
https://stackoverflow.com/questions/3380726/converting-a-rgb-color-tuple-to-a-six-digit-code-in-python
https://matplotlib.org/3.1.1/tutorials/colors/colors.html
"""

"""
import numpy as np
import pylab as plt
from mpl_toolkits.axes_grid1.axes_rgb import RGBAxes
rgb = np.random.random((5, 5, 3))
fig = plt.figure()
ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8])
ax.imshow_rgb(rgb[:,:,0],rgb[:,:,1],rgb[:,:,2],interpolation='none')
plt.figure()
plt.imshow(rgb,interpolation='none')
"""
