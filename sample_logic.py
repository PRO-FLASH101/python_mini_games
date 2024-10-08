import pandas as pd
from datetime import datetime

# Number of employees
while True:
    try:
        employee_amount = int(input("How many employees do you want to add?\nEnter here: "))
        break
    except ValueError:
        print("Enter an integer, no letters or special characters")

print(f'Okay, there are {employee_amount} employees')
number = list(range(1, employee_amount + 1))

# Data lists
employee_list = [
    [], # name
    [], # id1
    [], # dob1
    [], # years
    []  # age 
]

# Loop to collect employee data
for time in number:
    print(f'Employee {time}')
   
    # Collecting and validating employee name
    while True:
        name = input("Enter employee name: ")
        if name.isalpha():
            employee_list[0].append(name)
            break
        else:
            print("Use a name with no numbers or special characters!")
    
    # Collecting and validating employee ID
    while True:
        emp_id = input("Enter employee id: ")
        if emp_id.isdigit():
            employee_list[1].append(emp_id)
            break
        else:
            print("Use only numbers, no letters or special characters!")
    
    # Collecting and validating employee date of birth
    while True:
        dob = input("Enter employee dob (dd/mm/yyyy): ")
        try:
            dob_date = datetime.strptime(dob, "%d/%m/%Y") # change str to int
            
            if dob_date > datetime.now():
                print("Enter a valid year that is not in the future!")
            else:
                employee_list[2].append(dob)
                year = dob_date.year
                employee_list[3].append(year)
                break
        except ValueError:
            print("Enter in the proper format (dd/mm/yyyy)")
    
    # Calculate the age
    current_year = datetime.now().year
    employee_age = current_year - year
    if employee_age == 0:
        employee_list[4].append(0)
    else:
        employee_list[4].append(employee_age)

# Creating the DataFrame
data = {
    'S no': number, 
    'Name': employee_list[0],
    'Emp Id': employee_list[1],
    'Dob': employee_list[2],  # Use dob (day/month/year)
    'Year': employee_list[3],  # Add year as separate column if needed
    'Age': employee_list[4]
}

df = pd.DataFrame(data)
print(df)
