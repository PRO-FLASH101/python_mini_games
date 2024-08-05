#Background info
print("")
x = ","
price = input("Enter your total house cost: ")

#Exceptions
if x in price:
    print("Don't enter commas!!!")
    price = float(input("Enter your total house cost: "))
    price1 = int(price)
else:
    price1 = int(price)

#Backgorund info
years = float(input("How many years do you have to pay of the house cost: "))

#Calculations
months = 12 * years
yearly = price1 / years
mortage = price1/months

#final solution
print("")
print(f'You will pay ${mortage} every month and ${yearly} every year if you pay everything on time!!!')
print("THIS IS WITHOUT INTREST")
print('')