# Dict program to sort the key elements 

def dictionary():
    key_value = {}

    #I Intializing the value in the key

    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:- ")
    print("Key_Values ",key_value)

    # IterKeys() returns an iterator over the dictionary's keys.
    print("\n")
    print("Sorted Manner: ")
    for i in sorted(key_value.keys()):
        print(i, end=", ")
    
def main():
    #funciton calling

    dictionary()

# Main function calling

if __name__ == "__main__":
    main()


# 2nd Situation 

from collections import OrderedDict

dict = {
    'Ravi': '10',
    'Rajnish': '9',
    'Sanjeev': '15',
    'Yash': '2',
    'Suraj': '32'
}

dict1 = OrderedDict(sorted(dict.items()))

print(dict1)
