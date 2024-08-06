#bug it says err try again after last try fix that

import random

#FOR STAGE 1
answer_for_easy = random.randrange(1,10)

# this is the parameter 
numberoftries = 3
guesscount = 0

# this is stage 1
print("")
print("Hint: The answer is under 15!")
while guesscount < numberoftries:
    guess = int(input("Guess the number: "))
    guesscount += 1
    if guess == answer_for_easy:
        print("YOU GUESSED THE NUMBER!!!!")
        print("You passed stage 1 welcome to stage 2")
        print('')
        print("STAGE 2: the harder guessing round same hints from stage 1 don't apply")
        print("")
       
        # this is how the solution is made for stage 2 
        partone = random.randrange(1,50)
        numberguess = int(input("Enter a random number: "))
        print("Your hint is the number you entered will be multiplied by a random number, so guess the number!!")
        print("Also you get 2 extra tries because it is harder!!!")
       
        # this is the solution for stage 2
        parttwo = partone * numberguess
        solution = parttwo
       
        # this is the parameter for stage 2
        numberoftries = 5
        guesscount = 0
       
        # this is the game for stage 2
        while guesscount < numberoftries:
            guess = int(input("Guess the number: "))
            guesscount += 1
            if guess == solution:
                print("YOU GUESSED THE NUMBER!!!!")
                print("If you entered 0 in for the random number than you are either lucky, or super intutive!")
                print("")
                print("--------------------------------------------------------------------------------------------------------------")
                print("BONUS ROUND UNLOCKED!!!!")
                print("In this bonus round both solutions will be added and multiplied by a number under 5!")
                print("You will only have 2 guesses in total this round...")
                print("If you make it past this round you are a true winner")
                print("")
                
                #solution for bonus round
                part = random.randrange(1,5)
                part1 = solution + answer_for_easy
                solution_for_bonus = part1 * part
                
                #parameters for bonus round 
                guesscount = 0
                numberoftries = 2
                
                #the game for bonus round
                while guesscount < numberoftries:
                    bonus_round_guess = int(input("Enter your guess for the bonus round: "))
                    if bonus_round_guess == solution_for_bonus:
                        print("Congratulations on completing both stages and the bonus round 🤯🥳🥵!!!")
                        print("And if this was on your first try your really good at guessing games 🐱‍👤🥱🤨🤔!!")
                        print("")
                        print("THE END")
                        print("--------------------------------------------------------------------------------------------------------------")
                        break              
                    # so they know they were wrong      
                    elif bonus_round_guess != solution_for_bonus and guesscount < numberoftries:
                        print("")
                        print("Errr try again.... ")
                        print('')
                # so they feel somewhat good
                else:
                    print("")
                    print("Sorry you didn't clear the bonus round 😭!!")
                    print("But at least you made it past the first to 2 levels 😅!!")
                    print("")
                    print("THE END")
                    print("--------------------------------------------------------------------------------------------------------------")
            # so they know they guessed wrong 
            elif guesscount < numberoftries and guess != solution:
                print("")
                print("Errr try again.... ")
                print('')
        # this way the person doesn't get angry at an impossible game 
        else:
            print("")
            print("The solution was", solution)
            print("Better luck next time!")
        break
    # so they know its wrong number 
    elif guesscount < numberoftries and guess != answer_for_easy:
        print("")
        print("Errr try again.... ")
        print('')
# so no one gets angry in stage 1 
else:
    print("")
    print("The solution was", answer_for_easy)
    print("Better luck next time!")
    