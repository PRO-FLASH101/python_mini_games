import pandas as pd
from datetime import datetime

# Number of employees
while True:
    try:
        amount = int(input("How many employees do you want to add?\nEnter here: "))
        break
    except ValueError:
        print("Enter an integer, no letters or special characters")

print(f'Okay, there are {amount} employees')
number = list(range(1, amount + 1))

# Data lists
name1 = []
id1 = []
dob1 = []
years = []
age = []

# Loop to collect employee data
for time in number:
    print(f'Employee {time}')
   
    # Collecting and validating employee name
    while True:
        name = input("Enter employee name: ")
        if name.isalpha():
            name1.append(name)
            break
        else:
            print("Use a name with no numbers or special characters!")

    # Collecting and validating employee ID
    while True:
        emp_id = input("Enter employee id: ")
        if emp_id.isdigit():
            id1.append(emp_id)
            break
        else:
            print("Use only numbers, no letters or special characters!")
    
    # Collecting and validating employee date of birth
    while True:
        dob = input("Enter employee dob (dd/mm/yyyy): ")
        try:
            dob_date = datetime.strptime(dob, "%d/%m/%Y")
            dob1.append(dob)
            break
        except ValueError:
            print("Enter in the proper format (dd/mm/yyyy)")
    
    # Extract year from dob
    dob_date = datetime.strptime(dob, "%d/%m/%Y") #converts string to int
    year = dob_date.year # extract year 
    years.append(year) # add year 
    
    # Calc the Age
    current_year = datetime.now().year #get year from current day
    employee_age = current_year - year #gets the current age
    age.append(employee_age) #adds current age 
    
    # Adds the data to a list so it can do to the dict
    name1.append(name) #adds name
    id1.append(emp_id) #adds id
    dob1.append(dob) #adds dob 

# Creating the DataFrame
data = {
    'S no': number, 
    'Name': name1,
    'Emp Id': id1,
    'Dob': dob1,
    'Age': age
}

df = pd.DataFrame(data) #makes the table from the data 
print(df)

