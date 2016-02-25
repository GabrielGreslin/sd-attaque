__author__ = 'Gabriel'

import numpy as np
import os
from math import tan,log,pi

import time
'''
Load the data as a three column numpy array
Lat, Long, time
'''
def getID1Data():
    dir = os.path.dirname(__file__)
    filename = os.path.realpath("{0}\\Raw_Data\\ID1.txt".format(dir))
    out = np.loadtxt(filename,delimiter=",",skiprows=1)
    return out

def getID2Data():
    dir = os.path.dirname(__file__)
    filename = os.path.realpath("{0}\\Trans_Data\\ID2_new.txt".format(dir))
    out = np.loadtxt(filename,delimiter=",",skiprows=1)
    return out

def getID2DataOrdered():
    dir = os.path.dirname(__file__)
    filename = os.path.realpath("{0}\\Trans_Data\\ID2_ordered.csv".format(dir))
    out = np.loadtxt(filename,delimiter=",",skiprows=1)
    return out

def getID3Data():
    dir = os.path.dirname(__file__)
    filename = os.path.realpath("{0}\\Trans_Data\\ID3_new.csv".format(dir))
    out = np.loadtxt(filename,delimiter=",",skiprows=1)
    return out

'''
Convert degree to rad
'''
def fromDegreeToRad(degree):
    return degree/180*pi

'''
Lat, long in degrees
'''
def MillerProjection(lat,long):
    #print(lat)
    x = [5/4 * log(tan(pi/4+2*fromDegreeToRad(l)/5)) for l in lat]
    y = [fromDegreeToRad(i) for i in long]
    return x,y


'''
For plotting purpose
'''
def getXYTForClassI(data, classNumber,labels=None):

    x,y,t = ([],[],[])
    for i,l in enumerate(data):
        if labels is not None:
            if(labels[i] == classNumber):
                x.append(l[0])
                y.append(l[1])
                t.append(l[2])
        else:
            x.append(l[0])
            y.append(l[1])
            t.append(l[2])

    return x,y,t

def fromDataClusterToCsv(data,labels,name="dataToPlot"):
    file = open(name+'.csv',"w")
    file.write("latitude,longitude,cluster\n")

    for i,l in enumerate(data):
        line = str(l[0]) + ","+str(l[1]) + "," + str(labels[i]) + "\n"
        file.write(line)

    file.close()

def dataSelectTime(data,hourBegin, hourEnd,day=[0,1,2,3,4,5,6],hoursShift=1):

    mask = []

    for i,l in enumerate(data):
        t= l[2]
        t += hoursShift*60*60
        st = time.gmtime(t)

        if not (st.tm_hour >= hourBegin and hourEnd >= st.tm_hour and st.tm_wday in day):
            mask.append(i)

    return np.delete(data, mask,0)
