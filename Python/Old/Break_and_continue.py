#Break
for i in "DevOps":
    print(i)
    if i=="p":
        print("Found my data.")
        break
print("Output of the loop is printed")


#continue

for i in "DevOps":
    if i=="O":
        print("Found the date")
        continue
    print(f"Value of i is {i}")  #if you give the print value here it will not display the 'O'.
print("Out of loop")

#Break& Continue examples

#Here we are going to send the data randomly using random function
#Here Break will stop loop once it matches with the lookup/expected value

'''
import random
VACCINES=["moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca", "CoronaVac"]
random.shuffle(VACCINES)
print(VACCINES)
LUCKY=random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"***** TESTING VACCINES {vac}")
    if vac==LUCKY:
        print(f"{LUCKY} Vaccine test successful")
        break      #it's going to verify whole list until it get matches with the expected value then it's going to break.
    print("Test failed")

'''
#Continue will continue the loop even after the lookup/expected value found it will loop until the end of the data.

import random
VACCINES=["moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca", "CoronaVac"]
random.shuffle(VACCINES)
print(VACCINES)
LUCKY=random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"***** TESTING VACCINES {vac}")
    if vac==LUCKY:
        print(f"{LUCKY} Vaccine test successful")
        continue      
    print("Test failed")
