__author__ = 'Gabriel'

import numpy as np
import loadData as ld

import matplotlib.pyplot as plt

def temporalAround24removed(data):
    for i,l in enumerate(data):
        data[i][2] = float((l[2] % (24*60*60)) / 86400.)

    return data

def temporalAround7Daysremoved(data):
    for i,l in enumerate(data):
        data[i][2] = float((l[2] % (24*60*60*7)) / 86400.)

    return data

'''
Distance definition with small time difference
'''
def distance1(v1,v2):
    return (abs(v2[0]-v1[0]) + abs(v2[1]-v1[1]) + abs(v2[2]-v1[2])/10000.)

'''
Distance without time
'''
def distanceOnlyGeographique(v1,v2):
    return (abs(v2[0]-v1[0]) + abs(v2[1]-v1[1]))

'''
Remove Time
'''
def removeTime(data):
    data[:,2]=0
    return data


'''
Add distance columns
'''
def inputKmean(data,fdistance):
    lastColumn = np.zeros((len(data),1))
    data = np.append(data, lastColumn,1)

    first = True

    for i,l in enumerate(data):
        if first:
            vec1 = l
            data[i][3] =0
            first = False
        else:
            data[i][3] = fdistance(l,vec1)

    return data

def getThe80percentClosestToACenter(data,cluster, centerNumber):
    data_trans = cluster.transform(data)
    value80percent = []
    for i,l in enumerate(data):
        if(cluster.labels_[i] == centerNumber):
            value80percent.append([i,data_trans[i][centerNumber]])

    value80percent = np.array(value80percent)

    limitDistance = np.percentile(value80percent,q=80, axis=0)
    indexToKeep = []

    for l in value80percent:
        if l[1] < limitDistance[1]:
            indexToKeep.append(l[0])

    return np.take(data, indexToKeep, axis=0)

"""
Much required color for plotting
"""
colors = ['red', 'green', 'blue','yellow','black','brown','cyan','magenta','gray','firebrick']

def plotCluster(data,labels,nbCluster):
    for i in range(0,nbCluster):
        color = colors[i]
        x,y,t = ld.getXYTForClassI(data,i,labels)
        scale = 10
        x,y = ld.MillerProjection(x,y)
        plt.scatter(y, x, c=color, s=scale, label=color,alpha=1, edgecolors='none')

    plt.legend()
    plt.grid(True)
    plt.show()