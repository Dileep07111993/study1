#IF condition

x=30

if x < 30:
    print(f"{x} is less than 30")
print("printed")

#IF/Else condition

if x < 20:
    print(f"{x} is less than 20")
else:
    print(f"{x} is not less than 20")

#IF/ELIF/ELSE condition

if x < 30:
    print(f"{x} is less than 30")
elif x == 30:
    print(f"{x} is equal to 30")
else:
    print(f"{x} is greater than 30")
    



#Conditions vars

print("This IT Operastions has various skill set")
print("Find out your match")

print("Enter captilised values: ")

DevOps=["Jenkins", "Ansible", "Git", "Maven", "Python", "Puppet", "EKS", "Terraform"]
Development=("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1={"Name":"Santa", "Skill":"Blockchain", "Code":1208}
cntr_emp2={"Name":"Rocky", "Skill":"AI", "Code":1218}

usr_skill=input("Enter you desired skill: ")

#print(usr_skill)

#Check if the databasehave that skill

if usr_skill in DevOps:
    print(f"{usr_skill} is present in DevOps team")
elif usr_skill in Development:
    print(f"{usr_skill} is present on Development")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with this skill")
else:
    print("Skill not found")
    print("Please check you have used the capitalize letter")