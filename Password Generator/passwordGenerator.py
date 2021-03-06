#Password Generator Project
#random använder Merseme Twiser som generar random numbers :) 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
lenght_password= int(input("What sieze would you like your password to be?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
nr_letters = lenght_password - nr_symbols - nr_numbers
password = ""
i = 0
#To long password maight couse this to take some time ;) sense i am not using any else and just repeating the loop
while i < lenght_password:
    order = random.randint(1,3)
    if order == 1 and nr_symbols > 0:
        password += random.choice(symbols)
        nr_symbols -= 1
        i += 1
    elif order == 2 and nr_numbers > 0:
        password += random.choice(numbers)
        nr_numbers -= 1
        i += 1
    elif order == 3 and nr_letters > 0:
        password += random.choice(letters)
        nr_letters -= 1
        i += 1
    
print(password)

#Alternativ 2 3 for loops spara i lista och använda random.shuffle(list) :) 
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
