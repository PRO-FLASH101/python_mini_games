import random

def when_wrong():
    print("")
    print("Errr try again.... ")
    print('')

def Guessing_game():
    # FOR STAGE 1
    answer_for_easy = random.randrange(1, 10)

    # this is the parameter 
    numberoftries = 3
    guesscount = 0

    # this is stage 1
    name = input("What's your name?\nEnter Name: ")
    print("")
    print(f"Hello there {name} welcome to the guessing game I hve a hint for you the answer is under 15!")
    print("OH by the way here are the rules!")
    print("1. You will have 3 tries to guess the number \n2. There are hidden rules and levels \n3. If you make it to any hiddne levels no rules apply there\n4. You will not be told if your guess is too high or too low")
    print("")
    print("Bon Chance, Mon Ami!")
    # stage 1 game and total 
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
            partone = random.randrange(1, 50)
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
                    print("If you entered 0 in for the random number then you are either lucky, or super intuitive!")
                    print("")
                    print("--------------------------------------------------------------------------------------------------------------")
                    print("BONUS ROUND UNLOCKED!!!!")
                    print("In this bonus round both solutions will be added and multiplied by a number under 5!")
                    print("You will only have 2 guesses in total this round...")
                    print("If you make it past this round you are a true winner")
                    print("")

                    # solution for bonus round
                    part = random.randrange(1, 5)
                    part1 = solution + answer_for_easy
                    solution_for_bonus = part1 * part

                    # parameters for bonus round 
                    guesscount = 0
                    numberoftries = 2

                    # the game for bonus round
                    while guesscount < numberoftries:
                        bonus_round_guess = int(input("Enter your guess for the bonus round: "))
                        guesscount += 1  # Increment guesscount here
                        if bonus_round_guess == solution_for_bonus:
                            print("")
                            print("YOU WON THE ENTIRE GAME 😮😲🤯!!!")
                            print("Congratulations on completing both stages and the bonus round 🤯🥳🥵!!!")
                            print("And if this was on your first try your really good at guessing games 🐱‍👤🥱🤨🤔!!")
                            print("")
                            print("THE END")
                            print("--------------------------------------------------------------------------------------------------------------")
                            break
                        # to let user know they were wrong 
                        elif bonus_round_guess != solution_for_bonus:
                            when_wrong()
                    # so user feel somewhat good
                    else:
                        print("")
                        print("Sorry you didn't clear the bonus round 😭!!")
                        print("But at least you made it past the first 2 levels 😅!!")
                        print(f'The answer was {solution_for_bonus}')
                        print("")
                        print("THE END")
                        print("--------------------------------------------------------------------------------------------------------------")
                    break
                # so user know they were wrong
                elif guesscount < numberoftries and guess != solution:
                    when_wrong()
            else:
                print("")
                print("The solution was", solution)
                print("Better luck next time!")
            break
        # so user know they were wrong 
        elif guesscount < numberoftries and guess != answer_for_easy:
            when_wrong()
    else:
        print("")
        print("The solution was", answer_for_easy)
        print("Better luck next time!")

Guessing_game()
