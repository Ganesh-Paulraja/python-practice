# print(5 + 5)

# n1 = int(input("Enter first number"))
# n2 = int(input("Enter second number")) 

# print('Sum is : ', n1+n2)
# print('Sub is : ', n1-n2)
# print('mul is : ', n1*n2)
# print('div is : ', n1/n2)
# print('mod is : ', n1%n2)
# print('pow is : ', n1**n2)


#pi *r*r

# pi = 3.14

# rad = float(input('enter the radious'))
# ac = pi * rad ** 2

# print ("area: ", ac)

# simple_interest = p*n*r/100

# p = float(input('Enter the principle amount: '))
# n = float(input('Enter the number of years: '))
# r = float(input('Enter the rate of interest: '))

# simple_interes = p*n*r/100

# print("interest: ", simple_interes)

# --------------------------------------------------------------------

# opening_stock = int(input("Enter the opening stock: "))
# purchased_stock = int(input("Enter the purchase value: "))
# sale = int(input("Enter the sale qty: "))

# closing_stock = opening_stock + purchased_stock - sale

# print("Closing stock: ", closing_stock)

# ---------------------------------------------------------------

#conditions

#if statement

#**simple if 
# if condition: 
#     execute

# n1 = int(input("Enter a number"))
# n2 = int(input("Enter another number"))
# if n1 > n2:
#     print("n1 is big: ", n1)
# if n2 > n1:
#     print("n2 is big: ", n2)

#**common if
#   if <condition>:
#     statemet(s)
# else:
#     statement(s)

# if n1 > n2: 
#     print("n1 is big: ", n1)
# else:
#     print("n2 is big: ", n2)

#nested if statement
# n1 = int(input("Enter a number"))
# n2 = int(input("Enter another number"))
# n3 = int(input('Enter thired number'))

# if n1 > n2 and n1 > n3:
#     print("n1 is big: ", n1)
# elif n2 > n1 and n2 > n3:
#     print("n2 is big: ", n2)
# else:
#     print("n3 is big: ", n3)

# -------------------------------------------------
bp = 20000
# trg:  < 50000   4% comission
#       >= 50000 and < 100000   5%
#     >= 1000000   6%

trg = int(input("Enter the target"))

if trg < 50000:
    com = trg *4/100
elif trg >= 50000 and trg < 1000000:
    com = trg * 5/100
else:
    com = trg * 6/100

gp = bp + com

print("Basic pay: ", bp)
print("Targeet Achieved: ", trg)
print("Commission: ", com)
print("Gross Pay: ", gp)

# -------------------------------------------------------

# 5 sub total and average 

# sub mark --> pass or fail
# total
# averag
# class
#     above 60 1st class
#     above 50 2nd 
#     above 45 3rd 
#     or nilll