import csv
import os

print (os.getcwd())




#with open('SpeakerResults.csv','rb') as csvfile:
#    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#    for row in reader:
#        print(row)
        #add data to list or other data structure


# Avoid these frequencies:

#freq = {
#		"E" : 82.24,
#		"A" : 110.0,
#		"d" : 146.83,
#		"g" : 195.998
#	}
freq= [82.24,110.0,146.83,195.998]
def calc_closest_value(listOfModes):
    shortest_distance = [9999,9999,9999,9999]
    percentage_deviation=[999,999,999,999]
    closest_frequency = [0,0,0,0]
    counter = 0
    for v in freq:
        for test_mode in listOfModes:

            if abs(test_mode-v) < shortest_distance[counter]:
                shortest_distance[counter] = abs(test_mode-v)
                percentage_deviation[counter] = ((shortest_distance[counter])/v)*100
                closest_frequency[counter] = test_mode
        counter += 1
    for i in range(len(shortest_distance)):
        shortest_distance[i] = round(shortest_distance[i],2)
        percentage_deviation[i] = round(percentage_deviation[i],2)

    return shortest_distance, percentage_deviation, closest_frequency

sd_i, pd_i, cf_i = calc_closest_value([81.43,119.821,122.935,136.298,149.285, 157.287,173.983,187.425,190.763,218.249,218.514,239.525,254.236,258.396])
sd_1, pd_1, cf_1 = calc_closest_value([84.7,114,129,155,173,179,193,205,219,228,239,264])
sd_2, pd_2, cf_2 = calc_closest_value([100,154,159,190,197,201,209,239,244,253,270,282,292,314])
#2 sd_2, pd_2, cf_2 = calc_closest_value([84.58868,119.1945,126.17,155.5039,171.2618,178.0062,192.0339,202.034,216.3787,228.0677,238.2435,256.6063,262.3457,273.5223])
#3 sd_3,pd_3,cf_3 = calc_closest_value([96.51,127.77,157.77,166.851,190.444,193.626,207.809,215.534,239.22,247.18,265.388,271.2,284.447,286.4])
#4 sd_4,pd_4,cf_4 = calc_closest_value([52.7,58.4,87,103,108,125,129,132,155,162,170,183,194])


print " "
print "Iteration 0: ", sd_i, ", Sum of all distances: ", round(sum(sd_i),2),"percentage_deviation_1", pd_i, "closest freq: ", cf_i
print "Iteration 1: ", sd_1, ", Sum of all distances: ", round(sum(sd_1),2),"percentage_deviation_1", pd_1, "closest freq: ", cf_1
print "Iteration 2: ", sd_2, ", Sum of all distances: ", round(sum(sd_2),2),"percentage_deviation_1", pd_2, "closest freq: ", cf_2
# print "Iteration 3: ", sd_3, ", Sum of all distances: ", round(sum(sd_3),2),"percentage_deviation_1", pd_3, "closest freq: ", cf_3 # Something is not right here...
# print "Iteration 4: ", sd_4, ", Sum of all distances: ", round(sum(sd_4),2),"percentage_deviation_1", pd_4, "closest freq: ", cf_4 # THis is the same as 3 but a little lighter
