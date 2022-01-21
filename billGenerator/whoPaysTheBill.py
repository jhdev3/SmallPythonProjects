#Instructions
#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random

names_string = input("Give me everybody's names, separated by a comma and space. ")
names = names_string.split(", ")

#print(len(names))
#print(names.__len__()) Same as Len.
r_number = random.randint(0, len(names)-1)

print(f"{names[r_number]} is going to buy the meal today!")