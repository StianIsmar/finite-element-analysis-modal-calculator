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
    return shortest_distance
initial_distance = calc_closest_value([81.43,119.821,122.935,136.298,149.285,157.287,173.983,18])
print(initial_distance)
