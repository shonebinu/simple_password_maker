#Password generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','@','#','$','%','^','&','*','+']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

import random 

print("Welcome to the PyPassword Generator!")
lets = int(input("How many letters would you like in your password?"))
sym = int(input("How many symbols would you like?"))
nums = int(input("How many numbers would you like?"))

password=''


for i in range(0, lets):
    password += letters[random.randint(0, len(letters)-1)]
for i in range(0, sym):
    password += symbols[random.randint(0, len(symbols)-1)]
for i in range(0, nums):
    password += (random.choice(numbers)) # or use choice in lists


new_pass = list(password)
lat_pass = ''
for i in range(0, len(new_pass)):
    lat_pass += new_pass[random.randint(0, len(new_pass)-1)]

print(lat_pass)
