# python program to swap two elements in a list 

def swap(arr1):
    temp = arr1[0]
    arr1[0] = arr1[1]
    arr1[1] = temp

    return arr1

arr1 = [1, 3]

print(arr1)

print(swap(arr1))