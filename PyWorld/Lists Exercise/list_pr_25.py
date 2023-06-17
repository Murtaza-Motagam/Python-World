# Remove multiple elements from a list in Python

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"List before removing element: {list1}\n")

# for num in list1:
#     if(num % 2 == 0):
#         list1.remove(num)

unwanted_num = [1, 3, 5]
list1 = [ele for ele in list1 if ele not in unwanted_num]
 

print(f"List After removing element: {list1}")