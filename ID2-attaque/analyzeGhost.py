# Import
import sys
sys.path.append('../')
import loadData
import datetime

# Data
data = loadData.getID2DataOrdered()
#data = data[0:50]
groups = []

# Generate diff
m = 60
h = 60 * 60
d = 24 * 60 * 60
T = 5 * m # en secondes (s)
i = 1
a = 0
while i < len(data):

    b = i - 1

    previous = data[i-1]
    current = data[i]
    diff_t = current[2] - previous[2]

    if diff_t > T:
        groups.append([a, b])
        a = i

    i += 1

print("Groups")
print(groups)

points_begin = []
points_end = []
for g in groups:
    first = g[0]
    last = g[1]
    points_begin.append(data[first])
    points_end.append(data[last])

if T > h:
    file_id = str(T/h) + "h"
else:
    file_id = str(T/m) + "min"

file = open("groups-end-" + file_id + ".csv", "w")
file.write("latitude,longitude,time\n")
for p in points_begin:
    file.write(str(p[0]) + ',' + str(p[1]) + ',' + str(p[2]) + "\n")
file.close()

file = open("groups-begin-" + file_id + ".csv", "w")
file.write("latitude,longitude,time\n")
for p in points_end:
    file.write(str(p[0]) + ',' + str(p[1]) + ',' + str(p[2]) + "\n")
file.close()
