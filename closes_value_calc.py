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

# The guitar frequencies to be avoided:
freq= [82.24,110.0,146.83,195.998]

# Function takes in list of eigenfrequencies and loops through them to find:
## - The distance between the closest frequency to each guitar string
## - The percentage deviation between the closest value to each guitar frequency
## - The closest eigenfrequency to each guitar string
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

# Initial
sd_i, pd_i, cf_i = calc_closest_value([81.43,119.821,122.935,136.298,149.285, 157.287,173.983,187.425,190.763,218.249,218.514,239.525,254.236,258.396])
# Iteration 1:
sd_1, pd_1, cf_1 = calc_closest_value([84.7,114,129,155,173,179,193,205,219,228,239,264])

# Iteration 2:
sd_2, pd_2, cf_2 = calc_closest_value([100,154,159,190,197,201,209,239,244,253,270,282,292,314])

# Itearasjon 3:
sd_3,pd_3,cf_3 = calc_closest_value([103,158,163.7,191.3,200.5,204.6,210.3,243.4,243.9,263.0,276.2,284.0,293.7,316.8])

# Iteration 4:
sd_4,pd_4,cf_4 = calc_closest_value([108.5,165.9,168.8,194.61,207.788,210.789,215.073,245.372,250.341,269.366,280.791,291.153,296.252,327.251])

# Iteration 5:
sd_5,pd_5,cf_5 = calc_closest_value([109.3,166.5,170.9,205.437,209.7,213.327,225.071,247.489,251.488,270.748,282.817,294.158,297.834])

# Iteration 6:
# Tykkere stjerne og ekstra bjelke:
sd_7,pd_7,cf_7 = calc_closest_value([112.705,173.102,173.922,206.121,212.514,220.889,226.37,248.156,256.608,280.569,284.818,287.188,301.011,334.288])

# Tykkere stjerne:
# sd_6,pd_6,cf_6 = calc_closest_value([111.168,170.705,173.732,205.937,212.338,216.525,225.881,247.204,254.626,278.666,284.748,295.958,300.859,332.537])

# Tykkere stjerne og ekstra bjelke:
sd_7,pd_7,cf_7 = calc_closest_value([112.705,173.102,173.922,206.121,212.514,220.889,226.37,248.156,256.608,280.569,284.818,287.188,301.011,334.288])


#2 sd_2, pd_2, cf_2 = calc_closest_value([84.58868,119.1945,126.17,155.5039,171.2618,178.0062,192.0339,202.034,216.3787,228.0677,238.2435,256.6063,262.3457,273.5223])
#3 sd_3,pd_3,cf_3 = calc_closest_value([96.51,127.77,157.77,166.851,190.444,193.626,207.809,215.534,239.22,247.18,265.388,271.2,284.447,286.4])
#4 sd_4,pd_4,cf_4 = calc_closest_value([52.7,58.4,87,103,108,125,129,132,155,162,170,183,194])


print " "
print "Iteration 0: ", sd_i, ", Sum of all distances: ", round(sum(sd_i),2),"percentage_deviation_1", pd_i, "closest freq: ", cf_i
print "Iteration 1: ", sd_1, ", Sum of all distances: ", round(sum(sd_1),2),"percentage_deviation_1", pd_1, "closest freq: ", cf_1
print "Iteration 2: ", sd_2, ", Sum of all distances: ", round(sum(sd_2),2),"percentage_deviation_1", pd_2, "closest freq: ", cf_2
print "Iteration 3: ", sd_3, ", Sum of all distances: ", round(sum(sd_3),2),"percentage_deviation_1", pd_3, "closest freq: ", cf_3 # Something is not right here...
print "Iteration 4: ", sd_4, ", Sum of all distances: ", round(sum(sd_4),2),"percentage_deviation_1", pd_4, "closest freq: ", cf_4 # THis is the same as 3 but a little lighter
print "Iteration 5: ", sd_5, ", Sum of all distances: ", round(sum(sd_5),2),"percentage_deviation_1", pd_5, "closest freq: ", cf_5
print "Iteration 7: ", sd_7, ", Sum of all distances: ", round(sum(sd_7),2),"percentage_deviation_1", pd_7, "closest freq: ", cf_7
