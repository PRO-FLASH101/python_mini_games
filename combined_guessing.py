import random

#FOR STAGE 1
answer_for_easy = 27

# this is the parameter 
numberoftries = 3
guesscount = 0

# this is stage 1
print("")
print("Hint: the answer is under a 100 but is greater than 10")
while guesscount < numberoftries:
    guess = int(input("Guess the number: "))
    guesscount += 1
    if guess == answer_for_easy:
        print("YOU GUESSED THE NUMBER!!!!")
        print("You passed stage 1 welcome to stage 2")
        print('')
        print("STAGE 2: the harder guessing round same hints from stage 1 don't apply")
        print("")
        # this is how the solution is made
        partone = random.randrange(1,50)
        numberguess = int(input("Enter a random number: "))
        print("Your hint is the number you entered will be multiplied by a random number, so guess the number!!")
        # this is the solution
        parttwo = partone * numberguess
        solution = parttwo
        # this is the parameter 
        numberoftries = 3
        guesscount = 0
        # this is the game
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
        break
else:
    print("")
    print("The solution was", answer_for_easy)
    print("Better luck next time!")
    