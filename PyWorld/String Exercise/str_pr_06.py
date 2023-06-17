# Python – Uppercase Half String 

str = "geeksforgeeks"

hlf_indx = len(str) // 2 # breaking the string from middle 

res = '' # creating the null string for storing new str which display the letter in uppercase

for i in range(len(str)):

    if(i >= hlf_indx): # if i is greater than or equal to half index then characters will transform to uppercase.
        res+=str[i].upper() # transform in uppercase
    else:
        res+=str[i] # store as it is as it before


print("The string after transformation is: ",res) # display the transformed string
