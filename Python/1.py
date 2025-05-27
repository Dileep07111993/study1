"""

name=input("Enter the name: ")

name=name.strip().title()

print(f"My name is {name}")

"""
"""
x=float(input("Enter the value of x: "))
y=float(input("Enter the value of y: "))

z=round(x+y, 3)
print(f"{z:,}")
"""

# when we use this kind in def the variable 'name' value become 'to' value for hello def.
#  The output will be like "What's your name?: Dileep" if you give input as 'Dileep'
"""
def hello(to):
    print("hello", to)

name = input("What's your name?: ")
hello(name)

name= input ("What's you age?: ")
hello(name)
"""
# When we use below one fist output will be 'hello world' and the second outpu will be 'hello dileep'
# First def function will check within the function the later it will execute where it's calling.
"""
def hello(to="world"):
    print("hello", to)
hello()
name = input("What's your name?: ")
hello(name)
"""
#Note:- The function should already be existing by the time you caall it
"""
def main():
    name = input("Waht's your name?: ")
    hello(name)

def hello(to = "world"):
    print("Hello", to)
main()    
hello()
"""
#remember you can't use the one def function's attribute in anothe def function
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x) )
def square(n):
    return n * n #you can use this or 'return pow(n, 2)'

main()