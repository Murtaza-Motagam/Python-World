# python program to check occurrence of an element in the list

def check(list1, n, num):
    count = 0
    for i in range(0, n):
        if(list1[i] == num):
            count = count + 1
    
    return count




list1 = [21, 22, 23, 24, 22, 25, 22, 26]

n = len(list1)

num = int(input("Enter the number from list you want to check occurence: "))

result = check(list1, n, num)

print(f"{num} is occurred {result} times in list")