# Python program to print all Negative numbers in a range 

from xml.dom.minidom import Element

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# iterating each number in list
for num in range(start, end + 1):
	# checking condition
	if num < 0:
		print(num, end = " ")