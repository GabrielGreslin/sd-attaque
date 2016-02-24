

__author__ = 'Gabriel'

'''
Goals :
show speed
show dayweek day hours:minutes
'''

import loadData as ld
import numpy as np
import datetime
import math

#Get the data
data = ld.getID3Data()


def addSpeed(data):

    height,length = data.shape

    speedArray = np.zeros((height,1))

    def speed(lat1,long1,t1,lat2,long2,t2):
        if t1 != t2:
            return math.sqrt((lat1-lat2)**2 + (long1-long2)**2)/(t2-t1)
        else:
            return 0.0

    lat1,long1,t1 = tuple(data[0])

    for i,l in enumerate(data):
        lat2,long2,t2 = tuple(l)
        s = speed(lat1,long1,t1,lat2,long2,t2)
        lat1,long1,t1 = tuple(l)
        speedArray[i][0]=s*1000

    data = np.append(data,speedArray,1)

    return data

def changeTimePrintCsv(data,name,htimeShift = 1):
    file = open(name+'.csv',"w")
    file.write("latitude,longitude,time,speed\n")

    for i,l in enumerate(data):
        timeStr =  datetime.datetime.fromtimestamp(l[2] + htimeShift * 3600 ).strftime('%A %d %B %H:%M:%S')
        line = str(l[0]) + ","+str(l[1]) + "," + timeStr +","+str(l[3])+"\n"
        file.write(line)

    file.close()


data = addSpeed(data)

changeTimePrintCsv(data,"SpeedAndTime3",-8)