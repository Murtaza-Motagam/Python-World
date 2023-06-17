# python program to check whether an element is exist in a list or not 

def check(list1, size, element):

    for i in range(0, size):
        if(list1[i] == element):
            return i

    
    return -1






list1 = [21, 23, 4, 45, 5, 66, 222]

size = len(list1)

element = int(input("Enter the element of a list you want to check: "))

result = check(list1, size, element)

print(f"{element} is exist in a list at {result} position\n")