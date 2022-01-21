import random

asciiArt = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

choice = input("Write: Rock, Paper or Scissor: ").casefold()
player_nr = 0
if choice == "paper":
    player_nr = 1
elif choice == "scissor":
    player_nr = 2

compChoice = ["scissor", "rock", "paper"]

comp_nr = random.randint(0, 2)
print(asciiArt[player_nr])
#print(f"{comp_nr} : {compChoice[comp_nr]}")
print("\n Computer chose: " + compChoice[comp_nr]  + "\n" + asciiArt[comp_nr -1])

if compChoice.count(choice) == 0:
    print(f"{choice} not valid/ part of the game")
else:
    if compChoice[comp_nr] == choice:
        print("Its even both chose the same")
    else:
        if player_nr == comp_nr:
            print("You Win")
        else:
            print("You Loose")

#My thoughts for rules se the input as list and compChoice as a list then map em in the head.
#If its the same number then player always win if its even i check before and if player is not winning he is loosing :) 