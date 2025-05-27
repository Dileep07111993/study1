# modules ia a library containing one or more functions.
"""
import random #It will import all the functions related to random

coin=random.choice(["heads","tails"])
print(coin)

"""
"""
from random import choice #This will import only choice function from random module
coin=choice(["heads", "tails"])
print(coin)

"""
"""
import random

number = random.randint(1,10)

print(number)
"""
"""
import random
cards = ["jack", "king", "queen"]
random.shuffle(cards)
#print(cards) # It will shuffle 3 cards as list like ['king', 'jack', 'queen']
for card in cards:  #This will print the cards as one after other
    print(card)
"""
"""
import statistics

print(statistics.mean([100,90])) #Averages the values
"""
#command line-arguments

#agrv means argument vector
"""
import sys

print("hello, my name is", sys.argv[1]) # usage "python module.py dileep" output will be "hello, my name is dileep"
"""

#With this if you don't specify the argument it won't display the error message
"""
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""
"""
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello,my name is", sys.argv[1]) #If you want to use 2 words as name eg: dileep kumar you need to mention "python module.py "dileep kumar""
"""

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is", arg)