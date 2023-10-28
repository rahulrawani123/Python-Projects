// In this program we have created a password generator in which we have to enter the length of the desired password on the main input, after that our program will automatically generate a new password everytime.

import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = input("How many characters do you want in your password :- ")

while (True):

	try:

		character = int(user_input)

		if (character < 6):

			print("Your number should be at least 6")

			user_input = input("Please Enter your number again :- ")

		else:

			break

	except:

		print("Please Enter numbers only ")

		user_input = input("Please Enter your number again :- ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character * (30/100))
part2 = round(character * (20/100))

result = []

for x in range(part1):

	result.append(s1[x])
	result.append(s2[x])

for x in range(part2):

	result.append(s3[x])
	result.append(s4[x])

random.shuffle(result)

password = "".join(result)
print("Password is generating .....")
print("Your Password is succesfully generated ")
print("Your Password is :- ", password)
