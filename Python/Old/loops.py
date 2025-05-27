#For Loop

PLANET="Earth"
for i in PLANET:
    print(f"{i}")

VACCINE=["Moderna", "Pfizer", "Sputnik V", "Covaxin", "Astrazeneca"]

for vac in VACCINE:
    print(f"{vac}")


#While Loop

x=0
while x<=10:
    print(f"Value of X is {x}")
    print("looping")
    x += 1 #IF you don't mention this the loop will run until it matches the value. In this process it will do inifinty times. So we used this to end at 10+1

print("Rest of the code")

#Nested For Loop

VACCINE=["Moderna", "Pfizer", "Sputnik V", "Covaxin", "Astrazeneca"]

for vac in VACCINE:
    print(f"{vac}")
    for i in vac:
        print(i)

#The below script will triger the loop evry 2 seconds with multiple of 2. It will trigger in incremental order like 2 4 8 etc,.
import time
x=2
while True:
    print(f"Value of x is: {x}")
    print("looping")
    x*=2
    time.sleep(2)
    x+1