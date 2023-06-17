# Python program to remove i'th character from string 

# method-1: 

str = "Hello there"

new_str = "" # declaring a null string to further assign new string in it.

for i in range(len(str)):
    if i != 3: # removing of character using index of string or position in the string character holds
        new_str = new_str + str[i] # assigning every character to new_str except charcter which is in 3rd position


print("The new string after removal of i'th element is: ", new_str)

# method-2: 

str2 = "Hello there"

# new_str2 = str2.replace('e', '') # replacing e from full string means no occurrence of e will be there in string 

# print("The string after removal of i'th element character(doesn't work):  ", new_str2)


new_str2 = str2.replace('e', '', 1) # removing of character e from only particular position from string

print("The string after removal of i'th element character(worked):  ", new_str2)