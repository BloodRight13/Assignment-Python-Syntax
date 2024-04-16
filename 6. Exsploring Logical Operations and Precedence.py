#Task 1: Validating Calculaitons
#Formula for arithmetic is an=a1+(n-1)*d
a1 = 5
n = 10
d= 2
#an = 5+(10-1)*2 = 5+9*2 = 5+18 = 23
an=a1+(n-1)*d 
print(an)
#without the parentheses
#an = 5+10-1*2 = 5+10-2 = 15-2 = 13
an=a1+n-1*d
print(an)
#the code follows PEMDAS. 
#So when there are no parentheses is does the multiplying first

#Task 2: Mix and Match
x, y, z = 2 , 4, 6
if x < y or y < z and z < x:
    print("This comparrison is true.")