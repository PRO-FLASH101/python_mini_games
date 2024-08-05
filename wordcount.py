doc = input("Enter A Sentence: ")
print("")
newdoc = doc.split()

def wordcounter():  
    counter = 0
    for word in newdoc:
        counter = counter + 1
    print(f'The amount of words are {counter}') 
    print("")


wordcounter()
