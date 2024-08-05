#how many employee
amount = input("How many employees you want to add?\n Enter here: ")

#the times the loop ran
time = 1

#loop
while time <= amount:
    print(f'Employee {time}')
    name = input("Enter employee name: ")
    id = input("Enter employee id: ")
    dob = input("Enter employee dob(dd/mm/yyyy): ")
    time += 1 
    
