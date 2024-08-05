import pandas as pd

#how many employee
amount = input("How many employees you want to add?\n Enter here: ")
x = len(amount)
number = []

for num in x:
    number.append(num)

#the times the loop ran
time = 1

#data
name1 = []
id1 = []
dob1 = []

data = {
    'S no': number, 
    'Name': name1,
    'Emp Id': id1,
    'Dob': dob1,
    # 'Age': 
}

#loop
while time <= amount:
    print(f'Employee {time}')
    name = input("Enter employee name: ")
    id = input("Enter employee id: ")
    dob = input("Enter employee dob(dd/mm/yyyy): ")
    time += 1 
    name1.append(name)
    id1.append(id)
    dob1.append(dob)

#for debugging
print(name1)
print(id1)
print(dob1)
print(data)