'''
class Monster():
    # These are the attributes
    # health = 90 this is no longer nessary due to the __init__
    # energy = 40 this is no longer nessary due to the __init__
    # damage = int(input("The amount of damge dealt is: "))
    
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy 
    
    def __len__(self):
        return 5
    
    # These are the methods
    def attack(self, amount):
        print("")
        print("The monster has attacked")
        print(f'The amount of damage dealt was {amount}')
    
    def move(self, speed):
        print("The monster has moved")
        print(f"The monster has moved at {speed} miles per hour")
        print("")

monster = Monster(90,50)
print(len(monster))
'''
'''
monster.attack(monster.damage)
print("")
monster.move(5)
'''
'''
# This is without composition
class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price
        
        self.authorfname = authorfname
        self.authorlname = authorlname
        
        self.chapters =[]
    
    def addchapter(self, name, pages):
        self.chapters.append((name, pages))

b1 = Book("War and Peace", 39.0, "Leo", "Volt")

b1.addchapter("Chapter 1", 125)
b1.addchapter("Chapter 2", 97)
'''
# This is with composition
class Book:
    def __init__(self, title, price, author =None):
        self.title = title
        self.price = price
        self.author = author
        self.chapters =[]
    
    def addchapter(self, chapter):
        self.chapters.append(chapter)
    
    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result
        
class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

auth = Author("Leo", "Volt")
b1 = Book("War and Peace", 39.0, auth)


b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())






