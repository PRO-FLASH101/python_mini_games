'''
1. get input choices 1-6
2. generate the input using loop
3. no built in 
'''
# The info for the triangle
which_type = int(input("Which type of triangle do you want? (1-6)\n1. Half Pyramid\n2. Inverted Half Pyramid\n3. Hollow Inverted Half Pyramid\n4. Full Pyramid\n5. Inverted Full Pyramid\n6. Hollow Full Pyramid\nEnter Here: "))
print("")
height = int(input("How long do you want the triangle to be? \nEnter Here: "))
print("")

# List for iterating
the_height = list(range(1, height + 1))
inverted_height = list(reversed(the_height))

print(the_height)  # for debugging
print(inverted_height)  # for debugging 

# The options
def choice1():
    for num in the_height:
        for x in range(num):
            print("* ", end="")  # the end="" is to make sure it is joined
        print("")  # move to next line after printing stars for the current row 

def choice2():
    for num in inverted_height:
        for x in range(num):
            print("* ", end="")
        print("")

def choice3():
    for num in inverted_height:
        if num == height or num == 1:
            # Print full row of stars for the first and last row
            print('* ' * num)
        else:
            # Print star, spaces, and star for the hollow part
            print('* ' + ' ' * (2 * (num - 2)) + '* ')

def choice4():
    for i in range(height):
        print("  " * (height - i - 1) + '* ' * (i + 1))

def choice5():
    for i in range(height, 0, -1):
        print('  ' * (height-1) + '* ' * i)

def choice6():
    for i in range(height):
        if i == height - 1: #checks current row is last row
            print('* ' * (i + 1))
        else: #other rows 
            print(' ' * (height - i - 1) + '*', end='')
            if i > 0: #for rows other than the first row
                print(' ' * (2 * i - 1) + '*', end='')
            print()

# How to access the option
if which_type == 1:
    choice1()
    
elif which_type == 2:
    choice2()

elif which_type == 3:
    choice3()

elif which_type == 4:
    choice4()

elif which_type == 5:
    choice5()

elif which_type == 6:
    choice6()
else: 
    print("INVALID CHOICE: Please chose between 1 to 6!")

