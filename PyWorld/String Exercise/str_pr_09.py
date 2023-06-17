# Python | Count the Number of matching characters in a pair of string 

def count(str1, str2):
    i = j = 0
    set = []
    c = 0
    for i in str1:
        if(str1.find(i) >= 0 and j == str1.find(i)):
            c+=1
        j+=1
    
    print(f"No. of matching characters are: {c}")
      


str1 = "Hello there"
str2 = "Have we met before"

count(str1, str2)