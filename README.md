import matplotlib.pyplot
import matplotlib.patches
from PIL import Image
import numpy as np

im = np.array(Image.open('./PYUNIT.jpeg'), dtype=np.uint8)
fig,ax = matplotlib.pyplot.subplots(1)
rect = matplotlib.patches.Rectangle((560,779),678,232,linewidth=1,edgecolor='r',facecolor='none')
matplotlib.pyplot.show()
