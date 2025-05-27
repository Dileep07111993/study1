"""
x=int(input("Enter the number: "))
if x >= 90 and x<100:
    print ("A grade")
elif x > 80 and x < 89:
    print ("B grade")
else:
    print ("failed")"

"""
"""
x = int(input("What is x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
"""
"""
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
"""
"""
name = input("What's your name? ")

if name == "Ab" or name == "Dinesh" or name == "MK":
    print("They are from old team")
elif name == "Phani":
    print("They are from new team")
else:
    print("They are not from both teams")"
"""

# Match also we can use as conditions
"""
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffinder")
    case "Hermione":
        print("Gryffinder")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
"""

