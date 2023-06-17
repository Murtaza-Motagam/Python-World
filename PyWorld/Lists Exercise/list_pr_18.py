# Python program to print Even Numbers in given range

from xml.dom.minidom import Element

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# iterating each number in list
for num in range(start, end + 1):
	
	# checking condition
	if num % 2 == 0:
		print(num, end = " ")

print("\n")
# for odd elements 

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# iterating each number in list
for num in range(start, end + 1):
	
	# checking condition
	if num % 2 == 1:
		print(num, end = " ")
