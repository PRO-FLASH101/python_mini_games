#Background info
print("")
print("DON'T USE COMMAS!!!!")
price = float(input("Enter your total house cost: "))
years = float(input("How many years do you have to pay of the house cost: "))
#Calculations
months = 12 * years
yearly = price / years
mortage = price/months
#final solution
print("")
print(f'You will pay ${mortage} every month and ${yearly} every year if you pay everything on time!!!')
print("THIS IS WITHOUT INTREST")
print('')




