# python program to multiply all elements in the list 

def mulList(list1, n):
    count = 1
    for i in range(0, n):
        count = count * list1[i]
    return count



list1 = [3, 2, 4, 5, 6]
n = len(list1)

result = mulList(list1, n)

print(f"multiplication of all number in the list is: {result}")