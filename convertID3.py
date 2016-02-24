'''
Convert the raw ID3.txt to a csv file
Remove the boolean value
'''

file = open("Raw_Data\\ID3.txt", "r")
dest = open("Trans_Data\\ID3_new.csv", "w")
dest.write("latitude,longitude,time\n")
destList= []
# Number of line to keep
nbLineTODo = 10000000
i = 0

for l in file:
    if i > nbLineTODo:
        break
    elif i == 0:
        i += 1
        continue
    pieces = l.split(",")
    newL = "+" + ",".join([x for i, x in enumerate(pieces) if i in (0, 1, 3)])
    destList.append(newL)

destList.reverse()
for l in destList:
    dest.write(l)

file.close()
dest.close()
