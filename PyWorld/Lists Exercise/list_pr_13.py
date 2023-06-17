# python program to find smallest number in the list 


def minNum(list1, n):
    min = 0

    min = list1[0]    
    for i in range(n):
        if(list1[i] < min):
            min = list1[i]
    
    return min




list1 = [34, 33, 12, 5, 35]
n = len(list1)

num = minNum(list1, n)

print(f"The minimum number in the list is {num}")