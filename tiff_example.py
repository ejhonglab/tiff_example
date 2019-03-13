#!/usr/bin/env python3

"""
Loads TIFFs, max projects them, and averages that.
"""

from os.path import join, expanduser
import glob

import numpy as np
import tifffile
import matplotlib.pyplot as plt


# expanduser just converts ~ to /home/<username> on Linux systems
tiff_dir = expanduser('~/src/tiff_example')
tiff_suffix = '.tif'

projections = []

# Loops over all files with this suffix in tiff_dir.
for f in glob.glob(join(tiff_dir, '*' + tiff_suffix)):
    print('loading stack from:', f)

    stack = tifffile.imread(f)

    print('stack dimensions:', stack.shape)
    # Assumes Z-axis is the first (0th) axis.
    # (i.e. stack.shape is (n, 512, 512) or something)
    # Equivalent to np.max(stack, axis=0)
    projection = stack.max(axis=0)

    projections.append(projection)

plt.imshow(np.mean(projections, axis=0))
plt.axis('off')
plt.show()

