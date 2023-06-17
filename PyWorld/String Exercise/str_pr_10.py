# Python| Count the number of vowels in the string 

def countVowel(str):
    count = 0
    result = 0
    for char in str:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            count+=1
        else:
            pass

    result = print("Total Number of the vowels in the string: ", count)
    return result


str = "Hello there how are you doing, Considering it fair!!!"
countVowel(str)