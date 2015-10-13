import sys, re, collections
from os import listdir
from os.path import isfile, join
import numpy as np
from operator import itemgetter

k = 0.0 
k +=2
m = np.ones((3, 4))
m[2,:] /=k
print m