# Python program to count Even and Odd numbers in a List 

# method-1: normal way in main function 

    
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(list1)

count_even = 0
count_odd = 0

for num in list1:
    if(num%2==0):
        count_even += 1
    else:
        count_odd += 1

print(f"Total number of even numbers in the list: {count_even}")
print(f"Total number of odd numbers in the list: {count_odd}")

# method-2: using function  

# def countElement(list1):
#     countE = 0
#     for num in list1:
#         if(num%2==0):
#             countE += 1
    
#     return countE

# def countElement2(list1):
#     countO = 0
#     for num in list1:
#         if(num%2==1):
#             countO += 1
    
#     return countO

# result1 = countElement(list1)
# result2 = countElement2(list1)

# print(f"Total number of even numbers in the list: {result1}")
# print(f"Total number of odd numbers in the list: {result2}")