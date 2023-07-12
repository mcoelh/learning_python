"""Write a function that accepts an array of 10 integers (between 0 and 9),
 that returns a string of those numbers in the form of a phone number."""
import sys

def create_phone_number(n):
	phone_nbr = "".join(map(str, n))
	format_nbr = "({}) {}-{}".format(phone_nbr[:3], phone_nbr[3:6], phone_nbr[6:])
	return format_nbr

"""
nbr_list = list(map(int, input("Insert the phone number digits separated by spaces: ").split()))
if (len(nbr_list)) != 10:
	print("You need to insert a valid phone number.\nA valid phone number should have 10 digits")
	sys.exit()

for i in nbr_list:
	if i > 9:
		print("A valid phone number should consist of exactly 10 digits ranging from 0 to 9.")
		sys.exit()
formated = create_phone_number(nbr_list)
print(formated)
"""
