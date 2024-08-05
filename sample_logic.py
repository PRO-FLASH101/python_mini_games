import pandas as pd

# Number of employees
amount = int(input("How many employees do you want to add?\nEnter here: "))
number = list(range(1, amount + 1))

# Data lists
name1 = []
id1 = []
dob1 = []

# Loop to collect employee data
for time in number:
    print(f'Employee {time}')
    name = input("Enter employee name: ")
    emp_id = input("Enter employee id: ")
    dob = input("Enter employee dob(dd/mm/yyyy): ")
    
    name1.append(name)
    id1.append(emp_id)
    dob1.append(dob)

# Creating the DataFrame
data = {
    'S no': number, 
    'Name': name1,
    'Emp Id': id1,
    'Dob': dob1,
}

df = pd.DataFrame(data)
print(df)

# For debugging
print(name1)
print(id1)
print(dob1)
print(data)
