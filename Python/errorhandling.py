"""

try:
    x=int(input("What's x? "))
    print(f"x is {x}")
except ValueError:     # When you expect input as integer when you give string it will throw an error to except that error we are using it
    print("x is not an integer")
"""
"""
try:
    x=int(input("what's x? "))
except ValueError:
    print("x is not an integer")

#print(f"x is {x}") #If you use this it will show integer as output but not for string.
else:
    print(f"x is {x}") #First it will check the above code if it satisfies it will come to here
"""

#The below one will retry until it get satisfied with integer

"""
while True:
    try:
        x=int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break #If you put the below print line here, even if it gets satisfy it will retry continously cause there is not break
print(f"x is {x}")
"""
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x=int(input("what's x? "))
        except ValueError:
            #print("x is not an integer") #Here print is necessary to mention otherwise it will through an error instead of print you can use 'pass'
            pass #This will just pass until it receives input as integer
        else:
            return x #return will do output of the function and break the loop. But we can  only use it under a function.
main()
"""

def main():
    x = get_int("What's x? ") #We are calling the varibale via word prompt
    print ("x is {x}")

def get_int(prompt): # Here word prompt can be any word
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()