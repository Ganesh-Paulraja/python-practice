tamil = int(input("Enter a mark for Tamil: \n"))
english = int(input("Enter a mark for English: \n"))
maths = int(input("Enter a mark for Maths: \n"))
science = int(input("Enter a mark for Science \n"))
social_science = int(input("Enter a mark for Social Science \n"))
print('\n')
subjects = {
    "Tamil  " : tamil,
    "English" : english,
    "Maths  " : maths,
    "Science" : science,
    "Social ": social_science,
}
total = 0

for item in subjects:
    total += subjects[item]
    if subjects[item] >= 35:
        print(f'{item}  {subjects[item]}marks  Pass')
    else:
        print(f'{item}  {subjects[item]}marks  Fail')

average = total / 5
print('\n')
print("Subjects Total: ", total)
print("Subjects Average: ", average)

if average > 60:
    print("Grade : A")
elif average > 50:
    print("Grade: B")
elif average > 45:
    print("Grade: C")
else:
    print('Grade: Nill')


#   if m1>= 35 and m2>=35 and m3 >=35 and m4 >= 35 and m5 >= 35
# res = "pass"  
# else :
# falil

# if avg >= 60 and res == pass:
#     cla = "Firs"
# elif avg >= 50 and avg < 60 and res == "Pass":
#     cla = "Secnod"
# elif  avg >=45 and avg < 50 and res == "Pass":
#     cla = "third"
# else:
#     cla = nill


# print("Tamil \t: ", tamil)
# print("English :f", english)
# print("Maths \t": maths)
# print("Science: ", m4)
# -----------------------------------

# total 
# average