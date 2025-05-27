#While loop
"""
i=0
while i < 3:
    print("meow")
    i = i+1
"""

#For loop
"""
for _ in [0,1,2]: #you can use either i or _ or any name
    print("meow")
"""
"""
for i in range(3):
    print("meow")"
"""
"""
while True:
    n = int(input("Eneter the value n "))
    if n > 0:
        break
for i in range(n):
    print ("meow")
"""

"""
student = ["Dileep", "kumar"]

for students in student:
    print(students)
"""
#Len

"""
student = ["Dileep", "kumar", "Ravi"]

for i in range(len(student)): #Range will only take the integer not string. To overcome we use len
    print(i) #This will ouptut the position of name like 0,1,2
    print(student[i]) #This will give the each name
"""
"""
students = {"Dileep": "ECE", "kumar": "EEE", "Ravi": "CSE"}

for student in students:
    #print(student) # This will print the keys

    name=input("Enter the student name: ")
    print(name, students[name]) # This will print both keys and values
"""

# dictonraies in list
students = [
    {"name": "Ravi", "surname": "adepudi", "branch": "EEE"},
    {"name": "Dileep", "surname": "malepati", "branch": "ECE"},
    {"name": "Jagadeesh", "surname": "Nasina", "branch": "CSE"}
]

for student in students:
    print(student["name"], student["surname"], student["branch"], sep=",") # It will print like Ravi,adepudi,EEE

