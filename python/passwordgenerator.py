import random
import string

password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
print(password)

# Save the password to a text file
file_path = r'C:\Users\godsu\Desktop\python\New folder\psw.txt'
with open(file_path, 'w') as file:
    file.write(password)
