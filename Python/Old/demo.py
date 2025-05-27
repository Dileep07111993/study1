print("hello")
#variables
str1 = "Take the order at table number:"
num1 = 5

#List/collection of multi datatype, ecnlosed in square brackets.
first_list = [str1, "DevOps", num1, 1.5]

print(first_list)

first_tuple = (str1, "DevOps", num1, 1.5)

print(first_tuple)


#slicing

planet1="closest of sun"

print(planet1[0])

#slicing a string

print(planet1[0:7])

first_dir={"first_var":"value1", "second_var":35,"third_var":5.5}
print(first_dir)

print(type(first_list))
print(type(first_tuple))
print(type(first_dir))


#Slicing the list and tuple so here we are going to see slicing for tuple

devops=("Linux","vagrant", "Bash Scripting","AWS","Jenkins","Python","Ansible")

print(devops[0])
print(devops[1:4])
print(devops[1:4][1])
print(devops[1:4][1][0:4])

#Slicing using Dictionary

skills={"DevOps" : ("AWS","Jenkins","Python","Ansible"), "Development" : ["Java", "NodeJs", ".net"]}
print(skills)
print(skills["DevOps"])
print(skills["Development"])
print(skills["DevOps"][0:2])
print(skills["DevOps"][1][0:4])