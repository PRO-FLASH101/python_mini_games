import pandas as pd
from datetime import datetime

# Number of employees
amount = int(input("How many employees do you want to add?\nEnter here: "))
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
    name = input("Enter employee name: ")
    emp_id = input("Enter employee id: ")
    dob = input("Enter employee dob(dd/mm/yyyy): ")
    
    # Extract year from dob
    dob_date = datetime.strptime(dob, "%d/%m/%Y")
    year = dob_date.year
    years.append(year)
    
    # Calc the Age
    current_year = datetime.now().year
    employee_age = current_year - year
    age.append(employee_age)
    
    # Adds the data to a list so it can do to the dict
    name1.append(name)
    id1.append(emp_id)
    dob1.append(dob)

# Creating the DataFrame
data = {
    'S no': number, 
    'Name': name1,
    'Emp Id': id1,
    'Dob': dob1,
    'Age': age
}

df = pd.DataFrame(data)
print(df)

