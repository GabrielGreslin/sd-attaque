'''
Convert the raw ID2.txt to a csv file
Remove the boolean value
'''

file = open("Raw_Data\\ID2.txt","r")
dest = open("Trans_Data\\ID2_new.csv","w")
dest.write("latitude,longitude,time\n")

#Number of line to keep
nbLineTODo = 10000000
i=0

for l in file:
	if i>nbLineTODo:
		break
	i += 1
	pieces = l.split(" ")
	newL = "+"+",".join([x for i,x in enumerate(pieces) if i in (0,1,3)])
	dest.write(newL)

file.close()
dest.close()

