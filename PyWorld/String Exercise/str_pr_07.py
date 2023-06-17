# Python program to check if a string has at least one letter and one number 

def checkString(str):
    Str_true = False
    Str_false = False
    
    for i in str:
        if i.isalpha():
            Str_true = True

        if i.isdigit():
            Str_false = True

    return Str_true and Str_false



print(checkString('Hello There21'))
print(checkString('Hello There'))