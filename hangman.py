import random

# Word bank for random phrases
wordbank = ['Apple A Day Keeps The Doctor Away', 'Laughing Out Loud', 'Jesus Loves You', 'One of The Best Anime Is MHA', "The Bell's Are Ringing", "IDK"]

# Generating answer
part1 = random.randint(0, 5)  # Corrected to select a valid index
answer = wordbank[part1].lower()  # Converting to lower case for uniformity

# 1. Creating the final list of letters
final = [char for char in answer if char.isalpha()]
# print(final)  # for debugging purposes, delete after completion


# 2. Variables for tracking mistakes and tries
NumberOfWrong = 0
NumberOfTries = 6

# The rules for the game
print('')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------')
print("Hello there and welcome to the game called Hardcore Hangman!!!")
print("Let me explain the rules for you if you don't know already, its similar to normal hangman!")
print("")
print("1. You will have infinite tries to guess a letter in the phrase or word, if you get a letter wrong you will lose a limb")
print("2. You will only be able to make 6 mistakes in total, as you only have 4 limbs and a head + middle section")
print("3. The answer is different each time the program is restarted! So you won't be able to cheat and know the answer after you played once.")
print("4. You will not be able to see how long the word is or were the letters are, all you can do is guess if the letter is in the phrase or not.")
print('   Thats why its called hardcore hangman....')
print('')
print("IMPORTANT RULE!")
print("5. You MUST TYPE IN ONLY LETTERS NO WORDS ONLY A SING LETTER UPPER OR LOWERCASE DOES NOT MATTER!!!!!!!")
print('')
print("P.S. The easiest one is IDK, I felt bad since it took me about 10 times to win!")
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------')

# The guess
print("***ENTER ONLY A LETTER NOT A WORD***")
x = input("Type in okay if you read the rules above and understand them: ")

# Set of guessed letters to avoid repetition
guessed_letters = set()

# Set of wrong guessed letters
wrong = set()

#The actual game
if x.lower() == "okay": 
    while NumberOfWrong < NumberOfTries:
        guess = input("Enter A Guess: ").lower()

        if guess in guessed_letters:
            print(f'You already guessed the letter {guess}. Try again.')
            continue

        guessed_letters.add(guess)
        print(f"The guessed letters so far are {guessed_letters}.")

        if guess in final:
            print(f'The letter {guess} is in the answer.')
            # Remove the guessed letter from final
            final = [char for char in final if char != guess]
            if not final:  # If all letters are guessed correctly
                print("Congratulations! You've guessed the letters in the phrase!", answer.upper())
                break

        elif guess not in final:
            print(f'Nope! The letter {guess} is not in the answer.')
            NumberOfWrong += 1
            wrong.add(guess)
            print('')
            print(f'The wrongly guessed letters so far is {wrong}')


    if NumberOfWrong == NumberOfTries:
        print(f'Sorry, you lost! The answer was: {answer}')
