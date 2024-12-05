#Generate random password of a specified length.
import random
import string



lengthOfPassword = input("Enter length of password that you like to generate ")
if lengthOfPassword:
    lengthOfPassword_ = int(lengthOfPassword)
else:
    lengthOfPassword = 8

def passwordGenerator(lengthOfPassword):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(lengthOfPassword))
    return password

password = passwordGenerator(int(lengthOfPassword))
print(f"The password is {password}")



