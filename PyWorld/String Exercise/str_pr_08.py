# String Program to find out vowels presence in it 

# input = input("Enter the string: ")

# if('a', 'e', 'i', 'o', 'u' in input):
#     print("Output: Accepted")
#     print("Vowels are present in string\n")

def check(string):
    
    string = string.replace(' ', '')
    string = string.lower()
    vowel = [string.count('a'), string.count('e'), string.count(
    'i'), string.count('o'), string.count('u')]

	# If 0 is present int vowel count array
    if vowel.count(0) > 0:
        return('not accepted')
    else:
        return('accepted')


# Driver code
if __name__ == "__main__":

	string = "SEEquoiaL"

	print(check(string))
