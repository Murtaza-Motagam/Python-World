# python code to reverse the string 

print("Enter the string: ")
string = str(input()) # Taking input of string from user.

s = string.split()[::-1] # code for reversing the string using split function ::-1 indicates a particular words not character.
l = [] # assigning a null list to further store reverse string

for i in s:
    l.append(i) # inserting the new string after reversing

print("\n")
print("The reverse string: ")
print(" ".join(l)) # joining every words of a string for reversing.