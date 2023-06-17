# Dict program to sum all the items present in the dictionary 

Dict = {
    'a': 200,
    'b': 100,
    'c': 50
}

sum = 0

for i in Dict:
    sum += Dict[i]


print(sum)


# alternative method 

# Dict = {
#     'a': 200,
#     'b': 100,
#     'c': 50
# }

# list = []

# for i in Dict:
#     list.append(Dict[i])
#     final = sum(list)


# print(final)