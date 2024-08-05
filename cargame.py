# this is the engine for a car game
command = ""
started = False
while True:  
    command = input("> ")
    if command == "help" or command == "Help":
        print("Start - to start the car")
        print("Stop - to stop the car")
        print("Quit - to exit the game")
    elif command == "Start":
        if started:
            print("The car is already started!!!!!")
        else:
            started = True
            print("Car has started....")
    elif command == "Stop":
        if not started:
            print("Car is already stopped!!!")
        else:
            started = False 
            print("Car stopped awaiting command")
    elif command == "Quit":
        break
    else:
        print("Sorry, I don't understand that... please use the correct word try help")
