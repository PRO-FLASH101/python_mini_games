
'''
items = ['Sword', 'Katana','Dagger', 'Pipe', 'Exablur', 'Thors hammer']
items[3:4] = ['Caps shield', 'War ax']
print(items)

items = ['Sword', 'Katana','Dagger', 'Pipe', 'Exablur', 'Thors hammer']
items.insert(4,'IDK')
print(items)
'''
'''
#workaround to changin tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
'''
'''
# Beginner ways
Names = ('Naruto', 'Izumi', 'Silas', 'Joshua', 'Shadow', 'Bell')
(Apple, Banna, Pear, Orange, Kiwi, Lemon) = Names
print(Apple)
print(Banna)
print(Pear)
print(Orange)
print(Kiwi)
print(Lemon)
---------------------------------------------------------------------
# Better ways
An = ('Naruto', 'Izumi', 'Silas', 'Joshua', 'Shadow', 'Bell')
(Watermelon, Peach, *Water) = An #Asterik * saves you a lot of space and lines

# If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.

print(Watermelon)
print(Peach)
print(Water)
'''
'''
# You can join tuples using + or multiply them using * #
idk = ('1','2','3')
idk2 = ('4','5','6')
idk3 = idk + idk2
print(idk3)
idkOG = idk * 2 
print(idkOG)
'''
'''
Bat = {
    "Age" : "21",
    "Height" : "6'0 ft" ,
    "Secret Identity" : "Batman"  
}
print(Bat)
# or you can use this way and make it on one line
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
'''
'''
# always use def in the beginning and () at the end of the function name****
def myfunction():
    print("My first function prollly not though")
    
myfunction() # run it without this and it won't work 

# this uses arguments?
def my_function(fname, lheight):
  print(fname + " Raja: " + lheight)

my_function("Emil", "5'7")
my_function("Tobias", "5'8")
my_function("Linus", "6'0")
'''
'''
import this # zen of python***************************************************

x = bytes(4)
print(x)
'''
'''
prices = [30, 40, 60, 70]
total = 0

for price in prices:
  total = total + price
total1 = str(total)
print("The total is: " + total1)
'''
'''
numbers = [5,2,5,2,2]

for num in numbers:
  print("x" * num)
'''
'''
message = input(">> ")
def emoji_converter(message): 
  words = message.split()
  emoji = {
    ":)":"😃",
    ":(":"😔",
    ":0":"😯"
  }
  output = ""
  for word in words:
    output += emoji.get(word, word) + " "
  return output

print(emoji_converter(message))
'''
'''
class Person:
  def __init__(self, name):
    self.name = name 
  def talk(self):
    print(f'Hi I am {self.name}')


John = Person("John Smith")
John.talk()

Bob = Person("Bob Smith")
Bob.talk()
'''


