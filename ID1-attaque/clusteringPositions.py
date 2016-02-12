from sklearn.utils.validation import DataConversionWarning

__author__ = 'Gabriel'

'''
Kmean on position
'''

import loadData as ld
import clustering as clus

import sklearn.cluster as cluster
import numpy as np
from statistics import mean,median




data = ld.getID1Data()

data = ld.dataSelectTime(data,10,16,[0,1,2,3,4],1)

data = clus.temporalAround24removed(data)

#data = clus.inputKmean(data,clus.distanceOnlyGeographique)
#print(data)

#Trois endroits en dehors de toulouse
#Trois endroits dans Toulouse



data=clus.removeTime(data)



kk = cluster.KMeans(n_clusters=10,random_state=0)
out = kk.fit(data)

clus.plotCluster(data,out.labels_,10)
print("Cluster center " + str(out.cluster_centers_))
ld.fromDataClusterToCsv(data,out.labels_,"Work")

partialdata = clus.getThe80percentClosestToACenter(data,out,0)

print(partialdata)

kk2 = cluster.KMeans(n_clusters=3,random_state=0)
out2 = kk2.fit(partialdata)

print(out2.cluster_centers_)


clus.plotCluster(partialdata,out2.labels_,3)

ld.fromDataClusterToCsv(partialdata,out2.labels_,"Home")
#x,y,t = ld.getXYTForClassI(partialdata,1)


