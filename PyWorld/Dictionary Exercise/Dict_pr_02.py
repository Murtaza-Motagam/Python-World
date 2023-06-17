# Dict program to demonstrate the dictionary having multiple values or inputs in the keys 

import random as rn

dict = {}

# insert first triplet in the dictionary 

x, y, z  = 10, 20, 30
dict[x, y, z] = x + y - z;

# insert second triplet in the dictionary 

x, y, z  = 5, 2, 4
dict[x, y, z] = x + y - z;

# Printing the dictionary 

print(dict)

# 2nd Situation 

places = {
    ("19.07'53.2", "72.54'51.0"): "Mumbai", 
    
    ("28.33'34.1", "77.06;16.6"): "Delhi"
}

# print(places)
print('\n')

# trasversing dictionary with multiple keys and creating different list from it 

lat = []
long = []
plc  = []

for i in places:
    lat.append(i[0])
    long.append(i[1])
    plc.append(places [i[0], i[1]])


print(lat)
# print(long)
# print(plc)