# A module will be python scriot or package that has some functions or methods avialable in that eg:random
# we call it like this "import raandom"
# We can make our own modules like adding all the previously created function in one file and calling it.
# Now, we are going to add all the functions in one file "modules.py" file and we are going to call in "modules2.py" file

import random

def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy < 75):
        print("Seems not so effective, Needs more trial")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy > 90:
        print("We can take this vaccine")
    else:
        print("Don't take the vaccine")

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Enjoy your food")

def time_activity(*args, **kwargs):
    '''
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes+random minute spent on a random activity
    '''
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0, 60)  # Random number between 0-60 added to args
    print(min)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You have spent {min} for {kwargs[choice]}")

if __name__ == "__main__":
    print("Module 'modules' is being run directly")
else:
    print("Module 'modules' has been imported")
