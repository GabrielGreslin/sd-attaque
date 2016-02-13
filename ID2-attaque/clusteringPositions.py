__author__ = 'Gabriel'

'''
Kmean on position
'''
import sys
sys.path.append('../')

import loadData
import sklearn.cluster as cluster
from math import tan,log,pi

import matplotlib.pyplot as plt

data = loadData.getID2Data()

for d in data:
    data[3] = data[3] % (24 * 60 * 60)

#Trois endroits en dehors de toulouse
#Trois endroits dans Toulouse

kk = cluster.KMeans(n_clusters=6)
out = kk.fit(data)

colors = ['red', 'green', 'blue','yellow','black','brown']

def getXYTForClassI(out,data, classNumber):
    x,y,t = ([],[],[])
    for i,l in enumerate(data):
        if(out.labels_[i] == classNumber):
            x.append(l[0])
            y.append(l[1])
            t.append(l[2])

    return x,y,t

def fromDegreeToRad(degree):
    return degree/180*pi

def MillerProjection(lat,long):
    print(lat)
    x = [5/4 * log(tan(pi/4+2*fromDegreeToRad(l)/5)) for l in lat]
    y = [fromDegreeToRad(i) for i in long]
    return x,y

for i,color in enumerate(colors):
    x,y,t = getXYTForClassI(out,data,i)
    scale = 10
    x,y = MillerProjection(x,y)
    plt.scatter(y, x, c=color, s=scale, label=color,alpha=0.3, edgecolors='none')

plt.legend()
plt.grid(True)

plt.show()
