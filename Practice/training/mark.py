m1 = int(input("Enter your mark for Tamil: "))
m2 = int(input("Enter your mark for English: "))
m3 = int(input("Enter your mark for Math: "))
m4 = int(input("Enter your mark for Science: "))
m5 = int(input("Enter your mark for Tamil: "))

if m1 > 35 and m2 > 35 and m3 > 35 and m4 > 35 and m5 > 35:
    res = "Pass"
else:
    res = "Fail"

total = m1 + m2 + m3 + m4 + m5
average = total/5

if average >= 60 and res == "Pass":
    cla = "First"
elif average >= 50 and res == "Pass":
    cla = "Second"
elif average >=45 and res == "Pass":
    cla = "Thired"
else: 
    cla = "Nill"


print("Tamil \t: ", m1)
print("English : ", m2)
print("Maths \t: ", m3)
print("Science : ", m4)
print("Social \t: ", m5)
print("-------------------------------------")
print("Total\t: ", total)
print("Average\t: ", average)
print("Result\t: ", res)
print("Class\t: ", cla)