
#Logical operations AND and OR
x=1
y=2
a=40
b=60

out = (a < b) and (x > y)

print(out)

out=not(a>b)
print(out)

#Membership operators
first_tuple=("King", "queen", "soldier",35,5.5)
ans = "King" in first_tuple
print(ans)

#Identity operators
a=12
b=13

result= a is not b
print(result)
