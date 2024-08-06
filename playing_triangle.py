'''
1. get input choices 1-6
2. generate the input using loop
3. no built in 
'''
# The info for the triangle
which_type = int(input("Which type of triangle do you want?\nEnter Here: "))
print("")
if which_type == 1 or which_type == 2 or which_type == 3:
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

    # How to access the option
    if which_type == 1:
        choice1()
    elif which_type == 2:
        choice2()
    elif which_type == 3:
        choice3()


