import random
import hangmanAsci
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
#Can use comma to import multiple klasses/variabeles from a module :)
from wordlist import word_list

word = random.choice(word_list)
print(hangmanAsci.logo)
#for debugging
#print(word)


display_blank = []
for _ in word:
    display_blank += "_"

end_of_game = True
lives = 6
while end_of_game and lives != 0:
    print(f"{' '.join(display_blank)}")
    print(hangmanAsci.stages[lives])
    guess = input("Guess a letter: ").casefold()
    clearConsole()

    for pos in range(len(word)):
        letter = word[pos]
        if guess == letter:
            display_blank[pos] = letter

    if guess not in display_blank:
        lives -= 1
        print(f"You guess {guess} that's not in the word. You loose a life")
    end_of_game = "_" in display_blank

if lives == 0:
    print(f"You Loose, the word was: {word}")
    
else:
    print("You Win")

print(f"{' '.join(display_blank)}")