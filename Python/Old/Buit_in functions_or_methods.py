#string build in Methods/Functions

message="corona vaccine is ready to use,most of them are more than 90% effective"
print(message)
print(message.capitalize())
Message=message.capitalize()
print(Message)
'''
#dir() function
print(dir([]))
print(dir(""))
print(dir(()))
print(dir({}))
#We can use any of the above format to list the built in methods
'''

'''
print(message.upper())
print(message.islower())
print(message.isupper())
'''
'''
print(message.find("ready")) #It will finD the particular word and it displays the staring number of the letter that is 18
print(message.find("not"))   #IF that particluar value/word is not there it will display -1 as the word position
'''

'''
#It joins the ech value specified in the variable

seq1=("192", "168", "40", "90")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))

'''


mountains=["Everest", "Sahyadri", "Himalaya", "Alps", "K2", "Mt Abu"]
print(mountains)

mountains.append("Kilimanjaro")
print(mountains)

mountains.extend(["Tirumala Hills", "Yadagiri gutta"])
print(mountains)

mountains.insert(2, "Abu dhabi")
print(mountains)

mountains.pop()
print(mountains)

mountains.pop(3)
print(mountains)


#Dictionary

cntr_emp1={"Name":"Santa", "Skill":"Blockchain", "Code":1024}
print(cntr_emp1.values())
print(cntr_emp1.keys())
cntr_emp1.clear()
print(cntr_emp1)