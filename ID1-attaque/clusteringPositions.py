__author__ = 'Gabriel'

'''
Kmean on position
'''

import loadData
import sklearn.cluster as cluster
from math import tan,log,pi
import numpy as np
from statistics import mean,median




import matplotlib.pyplot as plt

data = loadData.getID1Data()

def temporalAround24removed(data):
    for i,l in enumerate(data):
        data[i][2] = float((l[2] % (24*60*60)) / 86400.)

    return data

data = temporalAround24removed(data)

def distance1(v1,v2):
    return (abs(v2[0]-v1[0]) + abs(v2[1]-v1[1]) + abs(v2[2]-v1[2])/10000.)

def distanceOnlyGeographique(v1,v2):
    return (abs(v2[0]-v1[0]) + abs(v2[1]-v1[1]))

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

#data = inputKmean(data,distanceOnlyGeographique)
print(data)

#Trois endroits en dehors de toulouse
#Trois endroits dans Toulouse

kk = cluster.KMeans(n_clusters=10)
out = kk.fit(data)

colors = ['red', 'green', 'blue','yellow','black','brown','cyan','magenta','gray','firebrick']



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
    #print(lat)
    x = [5/4 * log(tan(pi/4+2*fromDegreeToRad(l)/5)) for l in lat]
    y = [fromDegreeToRad(i) for i in long]
    return x,y

for i,color in enumerate(colors):
    x,y,t = getXYTForClassI(out,data,i)
    scale = 10
    x,y = MillerProjection(x,y)
    plt.scatter(y, x, c=color, s=scale, label=color,alpha=1, edgecolors='none')

plt.legend()
plt.grid(True)


print(out.cluster_centers_)

data_trans = out.transform(data)
print(data_trans)


x,y,t = getXYTForClassI(out,data,1)

print("Annecy" + str(median(x))+" "+str(median(y)))


plt.show()

