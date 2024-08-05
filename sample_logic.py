import pandas as pd
from datetime import datetime

# Number of employees
try:
    amount = int(input("How many employees do you want to add?\nEnter here: "))
except:
    print("Enter a integar no letters or special characters")
    amount = int(input("How many employees do you want to add?\nEnter here: "))
else:
    print(f'Okay there are {amount} employees') 
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
    try:
        name = input("Enter employee name: ")
    except: 
        print("Use a name no numbers or special character!")
        name = input("Enter employee name: ")
    else: 
        continue 
    try:
        emp_id = input("Enter employee id: ")
    except:
        print("use only numbers no letters or strings")
    else:
        continue 
    try:
        dob = input("Enter employee dob(dd/mm/yyyy): ")
    except:
        print("Enter in the proper values in the right order")
        dob = input("Enter employee dob(dd/mm/yyyy): ")
    else:
        continue
    
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

