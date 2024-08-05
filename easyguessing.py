import random
# this is a guessing game based of a while loop

# this is how the solution is made
# partone = random.randrange(1,100)
# numberguess = int(input("Enter a random number: "))
#print("Your hint is the number you entered will be multiplied by a random number, so guess the number!!")

# this is the solution
# parttwo = partone * numberguess
solution = 27 #parttwo

# this is the parameter 
numberoftries = 3
guesscount = 0
# this is the game
print("")
print("Hint: the answer is under a 100 but is greater than 10")
while guesscount < numberoftries:
    guess = int(input("Guess the number: "))
    guesscount += 1
    if guess == solution:
        print("YOU GUESSED THE NUMBER!!!!")
        break
else:
    print("")
    print("The solution was", solution)
    print("Better luck next time!")
# this way the person doesn't get angry at an impossible game 