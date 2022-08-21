import random

title = "Welcome to the Password Generator"
print(title)  

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

no_letters = int(input("How many letters would you like on your password..?\n"))
no_symbols = int(input("How many symbols would you like on your password..?\n")) 
no_numbers = int(input("How many numbers would you like on your password..?\n"))

random_letters = random.sample(letters,no_letters)
random_symbols = random.sample(symbols,no_symbols) 
random_numbers = random.sample(numbers,no_letters)
new_password = random_letters + random_symbols + random_numbers 
shuffled_password  = random.shuffle(new_password)
password_string = ''.join(new_password)
print(password_string)