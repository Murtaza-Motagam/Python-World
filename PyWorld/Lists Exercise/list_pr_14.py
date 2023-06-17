# python program to find largest number in the list 


def maxNum(list1, n):
    max = 0

    max = list1[0]    
    for i in range(n):
        if(list1[i] > max):
            max = list1[i]
    
    return max




list1 = [34, 33, 12, 5, 35]
n = len(list1)

num = maxNum(list1, n)

print(f"The maximum number in the list is {num}")