# Python program to print positive numbers in a list 

list1 = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

n = len(list1)

for num in list1:
    if(num > 0):
        print(num, end=" ")

