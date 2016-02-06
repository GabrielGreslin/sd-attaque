__author__ = 'Gabriel'

import numpy as np
import os

def getID1Data():
    dir = os.path.dirname(__file__)
    filename = os.path.realpath("{0}\\Raw_Data\\ID1.txt".format(dir))
    out = np.loadtxt(filename,delimiter=",",skiprows=1)
    return out