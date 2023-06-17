# Python program to print even length words in a string 

# method-1: 

str = "How can i help you"

new_str = ""

for i in range(len(str)):
    if(i % 2 == 0):  # condition to choose only even number of position in the array which is i.
        new_str = new_str + str[i]    # assigning character by character only of even position of a string and store it in new_str


print("String1 of only even indexes is: ", new_str) # displaying of a string of only even postion values

# method-2: 

# Obtain same output using a function

def evenDisplay(str1): 
    str2 = "" # creation of a null value string which is further stores the new string of even position elements

    # code condition same as above method displays here.
    for i in range(len(str1)):
        if(i % 2 == 0):
            str2 = str2 + str1[i]
        
    return str2 # return of a new string as output


str1 = "Sure You Can"

str2 = ""

print("String2 of only even indexes is: ", evenDisplay(str1))