# Eb reading

# ct      u                 chr

# House  <500              0.75
#        >=500 and <1000   1.25
#        >=1000            1.75

# Shop   <1000              2.00
#        >=1000 and <2500   3.00
#        >=2500             4.00

# inudstry  <2500               4.00
#           >=2500 and <4000     6.00
#           >=4000               7.50



customer_type = input("Enter Electicity Type House/Shop/Industry: ").lower()
unit = float(input("Enter Electicity Measure: "))

if customer_type == "house":
    if unit < 500:
        bill = 0.75 * unit
    elif 500 <= unit < 1000:
        bill = 1.25 * unit
    else:
        bill = 1.75 * unit
elif customer_type == "shop":
    if unit < 1000:
        bill = 2.00 * unit
    elif 1000 <= unit < 2500:
        bill = 3.00 * unit
    else:
        bill = 4.00 * unit
else: 
    if unit < 2500:
        bill = 4.00 * unit
    elif 2500 <= unit < 4000:
        bill = 6.00 * unit
    else:
        bill = 7.50 * unit

print("-------------------------------------")
print("Your Electricity bill type: ", customer_type)
print("Your Electricity Amount: ", unit , "Unit")
print("-------------------------------------")
print("Your Electricity Bill is :",  bill)