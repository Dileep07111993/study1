#Here we are going to write our own function. Main purpoose is the reusuability.

#Definition function

'''
def add(arg1, arg2): # Here add is a naming convention we can use any like addd, aaadd
    total=arg1+arg2
    return total
out=add(2,3)         # wE are reclling that add here.
print(out) 
'''
'''
#We can call the function like aabove or below.
def adder(arg1, arg2):
    total=arg1+arg2
    print(total)
adder(10,50)
'''
'''

def add(arg1, arg2):
    total=arg1+arg2

out=add(2,3)
print(out)
#The output of the above one is 'None'.Because we have not written 'return total'.
#Need to check this
'''


#It's adding the values

def summ(arg):
    x=0
    for i in arg:
        x=x+i
    return x
out = summ([10,20,30])
print(out)

#Output is 60 need to check in depth

'''
#How to pass multiple arguments like summ([10,20],[20,30])

#Default Argument

def greeting(MSG):
    print(f"Good {MSG}")
greeting("morning")

#Here above we have given the argument as 'morning'. If we don't give anything it will trigger the error. For that we will give a default value.

def greeting(MSG="morning"):
    print(f"Good {MSG}")
greeting()

# In above example you can see the arg is empty since it's empty the arg took the default value. If you want overwrite it just fill it like greeting(evening).

'''

'''
#Now we will pass the two args.

def vac_feedback(vac,efficacy):
    print(f"{vac} Vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy < 75):
        print("Seems not so effective, Needs more trial")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy > 90:
        print("We can take this vaccine")
    else:
        print("Don't take the vaccine")

vac_feedback("Sputnik V",30)

#Here in vac_feedback the vac is a string and efficacy is an integer. If we change the order like 'vac_feedback(30,"Sputnik V") it it will trigger an error because efficacy is doing arithemetic operation.
#If we want pass arguments in any order we need to mention keywords arguments like vac_feeback(efficacy=34,vac="unknown").

'''

'''
# We will see how to pass multiple arguments.
# Variable Length Arguments *args (Non keyword Arguments)

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Enjoy your food")
order_food("Salad", "Pizza", "Biryani", "Soup")

#*args can be anything like *dileep but args is regularly used.

#Variable Length Arguments *kwargs (keyword Arguments)
#This will take both Non Keyword and Keyword Arguments.

'''

import random
def time_activity(*args, **kwargs):
    '''
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes+random minute spent on a random activity
    '''
    print(args)
    print(kwargs)
    min = sum(args)+ random.randint(0,60)  # It's going to give a random number between 0-60 and that number will be aadded to args
    print(min)
    choice=random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You have spent {min} for {kwargs[choice]}")
time_activity(10,20,30, hobby="Dance", sport="cricket", fun="Driving", work="Driving")
