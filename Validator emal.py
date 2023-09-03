import re

#Enter your name
name = input("Enter your full name:")
print("hello!"+ name)

#Email section
def is_valid_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email):
        return True
    else:
        return False

email = input("Enter your email: ")
if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")


# Your password is 

 
import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these :
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		# Adding letters to possible characters
		characterList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		characterList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	# Picking a random character from our
	# character list
	randomchar = random.choice(characterList)
	
	# appending a random character to password
	password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))

