# Python program to count positive and negative numbers in a list 

list1 = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10]
n = len(list1)

count_pos = 0
count_neg = 0

for num in list1:
    if(num > 0):
        count_pos += 1
    else:
        count_neg += 1

print(f"Total number of even numbers in the list: {count_pos}")
print(f"Total number of odd numbers in the list: {count_neg}")