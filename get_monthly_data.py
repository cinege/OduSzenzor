import os

directory = "/home/pi/sensors/data"
filenames = os.listdir(directory)

dict = {}

for filename in sorted(filenames):
	with open(directory + "/" + filename,"r") as f:
		lines  = f.readlines()
		for line in lines:
			if len(line) > 3:
				entries = line.split(",")
				month = entries[0][:7]
				if not month in dict:
					a = []
					dict[month] = a
				temp = entries[1]
				dict[month].append(float(temp))
for month in sorted(dict):
	monthly = dict[month]
	max_value = max(monthly)
	min_value = min(monthly)
	avg_value = round(sum(monthly)/len(monthly),1)
	print(month)
	print(min_value)
	print(avg_value)
	print(max_value)
