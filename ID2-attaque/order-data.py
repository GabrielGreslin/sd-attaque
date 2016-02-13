# Import
import sys
sys.path.append('../')
import loadData
import datetime

# Data
data = loadData.getID2Data()
data_ordered = []

N = len(data)
i = N - 1
while i >= 0:
    data_ordered.append(data[i])
    i -= 1

file = open("../Trans_Data/ID2_ordered.csv", "w")
file.write("latitude,longitude,time\n")
for p in data_ordered:
    file.write(str(p[0]) + ',' + str(p[1]) + ',' + str(p[2]) + "\n")
file.close()
