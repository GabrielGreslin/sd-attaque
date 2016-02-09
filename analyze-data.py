from numpy import genfromtxt
import datetime
import sklearn.cluster as cluster
import matplotlib.pyplot as plt

data = genfromtxt('Raw_Data/ID1.txt', delimiter=',', skip_header = 1)
time_data = data[:,2]

print(type(time_data))
print(type(time_data[0]))

min_time = min(time_data)
max_time = max(time_data)
scope = max_time - min_time

min_date = datetime.datetime.fromtimestamp(min_time).strftime('%Y-%m-%d %H:%M:%S')
max_date = datetime.datetime.fromtimestamp(max_time).strftime('%Y-%m-%d %H:%M:%S')

day = 24 * 60 * 60
hours = 60 * 60

time_data_elapsed_day = [(x-min_time)/day for x in time_data.tolist()]

# Cluster time
#kk = cluster.KMeans(n_clusters=6)
#out = kk.fit(data)

print('min_time:')
print(min_time)
print(min_time/day)
print(min_date)

print('max_time:')
print(max_time)
print(max_time/day)
print(max_date)

print('scope:')
print(scope)
print(scope/day)

# Plot time
plt.plot(time_data_elapsed_day, '.')
plt.show()