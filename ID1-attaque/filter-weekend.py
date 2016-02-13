# Import
import sys
sys.path.append('../')
import loadData
import datetime

# Data
data = loadData.getID1Data()
data_filtered = []
data_weekday = []

for p in data:
    ts = p[2]
    day = datetime.datetime.fromtimestamp(ts).strftime('%w')
    if day == '6' or day == '7' :
        data_filtered.append(p)
    else:
        data_weekday.append(p)

file = open("weekend.csv", "w")
file.write("latitude,longitude,time\n")
for p in data_filtered:
    file.write(str(p[0]) + ',' + str(p[1]) + ',' + str(p[2]) + "\n")
file.close()

file = open("weekday.csv", "w")
file.write("latitude,longitude,time\n")
for p in data_weekday:
    file.write(str(p[0]) + ',' + str(p[1]) + ',' + str(p[2]) + "\n")
file.close()

print("len(data):" + str(len(data)))
print("len(data_filtered):" + str(len(data_filtered)))
print("len(data_weekday):" + str(len(data_weekday)))
