__author__ = 'Gabriel'

'''
Kmean on position
'''

import loadData as ld
import clustering as clus

import sklearn.cluster as cluster
import numpy as np
from statistics import mean,median



data = ld.getID2Data()

######If you want to select particular moments in the day
timeShift= -8 #San Francisco
data = ld.dataSelectTime(data,0,24,[0,1,2,5,6],timeShift)

####### Modulo 24 hours
#data = clus.temporalAround24removed(data)

#######Remove time
#data=clus.removeTime(data)

kk = cluster.KMeans(n_clusters=10,random_state=0)
out = kk.fit(data)

clus.plotCluster(data,out.labels_,10)
print("Cluster center " + str(out.cluster_centers_))
ld.fromDataClusterToCsv(data,out.labels_,"Raw")

###### Select a center and get the 80% closest values to this center removed to far points
partialdata = clus.getThe80percentClosestToACenter(data,out,0)

print(partialdata)

###### Second cluster on the partial data
'''
kk2 = cluster.KMeans(n_clusters=3,random_state=0)
out2 = kk2.fit(partialdata)

print(out2.cluster_centers_)


clus.plotCluster(partialdata,out2.labels_,3)

ld.fromDataClusterToCsv(partialdata,out2.labels_,"Home")
#x,y,t = ld.getXYTForClassI(partialdata,1)
'''


