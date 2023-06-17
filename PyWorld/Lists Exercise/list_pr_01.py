# python program to swap the list or array 


def swaplist(list1):

    size = len(list1)

    # swapping
    temp = list1[0]
    list1[0] = list1[size-1]
    list1[size-1] = temp
        
    return list1




list1 = [1, 2, 3, 4, 5, 6]

print(swaplist(list1))
