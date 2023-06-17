# Python program to print negative numbers in a list 

list1 = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

n = len(list1)

print("The negative numbers are: \n")
for num in list1:
    if(num < 0):
        print(num, end=" ")

