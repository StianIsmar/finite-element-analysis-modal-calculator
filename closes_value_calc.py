import csv
import os

print (os.getcwd())




#with open('SpeakerResults.csv','rb') as csvfile:
#    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#    for row in reader:
#        print(row)
        #add data to list or other data structure


# Avoid these frequencies:

freq = {
		"E" : 82.24,
		"A" : 110.0,
		"d" : 146.83,
		"g" : 195.998
	}

def calc_closest_value(listOfModes):
    shortest_distance = [9999,9999,9999,9999]
    counter = 0
    for k, v in freq.items():
        avoid = v
        for test_mode in listOfModes:
            if abs(test_mode-v) < shortest_distance[counter]:
                shortest_distance[counter] = abs(test_mode-v)
        counter += 1
    for i in range(len(shortest_distance)):
        shortest_distance[i] = round(shortest_distance[i],2)
    return shortest_distance

initial_distance = calc_closest_value([81.43,119.821,122.935,136.298,149.285,
157.287,173.983,187.425,190.763,218.249,218.514,239.525,254.236,258.396])

iteration_1 = calc_closest_value([84.7,114,129,155,173,179,193,205,219,228,239,264])

print(initial_distance)
print(iteration_1)
