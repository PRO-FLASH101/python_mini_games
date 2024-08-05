#fix to make not case sensitive

import random

Wordbank = ["Hello", "Apple", "Strawberry", "Shadow", "Clover", "Anime", "Naruto", "Bell", "Joshua", "Raja", "Spy", "Bored", "Python", "Coder", "IDK"]
print("This is the word bank for the guessing game. Try to figure it out!!!")
print(Wordbank)
print("")

# Parameters 
guesscount = 0 
part1 = random.randint(0, len(Wordbank) - 1)  # Adjusted to select a valid index
answer = Wordbank[part1]  # Get the word from the list, not the index
print(f"The answer (for debugging purposes) is: {answer}")  # Debugging line, can be removed later

# Game itself
while guesscount < 3:
    guess = input("What is your guess: ")
    if guess == answer:
        print("Wow, you guessed the word!!!")
        break 
    else:
        print("Oops, try again")
        guesscount += 1
else: 
    print(f'The right answer was "{answer}"!')
    print("Better luck next time!")
