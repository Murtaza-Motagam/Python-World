# python program to cloning or copying the list 

def cloneList(list1):
    list1_copy = list1[:]
    return list1_copy



list1 = [23, 24, 54, 22, 26]
list2 = cloneList(list1)

print(f"Original string is: {list1}")
print(f"Clonign string is: {list2}")