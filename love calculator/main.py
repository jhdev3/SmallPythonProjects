#You are going to write a program that tests the compatibility between two people.

#To work out the love score between two people:

#Take both people's names and check for the number of times the letters in the word TRUE occurs. 

#Then check for the number of times the letters in the word LOVE occurs. 

#Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = 0
love = 0
def lettersInName(name, word):
    numberOfTimes = 0
    for c in name:
        for l in word:
            if c == l:
                numberOfTimes += 1
    return numberOfTimes      

love += lettersInName(name1.casefold(), "love")
love += lettersInName(name2.casefold(), "love")
true += lettersInName(name1.casefold(), "true")
true += lettersInName(name2.casefold(), "true")

trueLove = int(f"{true}{love}")

if trueLove < 10 or trueLove > 90:
    print(f"Your score is {trueLove}, you go together like coke and mentos.")
elif trueLove >= 40 and trueLove <= 50:
    print(f"Your score is {trueLove}, you are alright together.")
else:
    print(f"Your score is {trueLove}.")