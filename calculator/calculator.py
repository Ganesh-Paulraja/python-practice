from art import logo
print(logo)

continue_loop = True
first_number = float(input("What's first number?: "))
while continue_loop:
    print("+\n-\n*\n/")
    operation = input("Pick an operation:  ")
    next_number = float(input("What's the next number?: "))
    number_operations = {
        "+" : first_number + next_number,
        "-" : first_number - next_number,
        "*" : first_number * next_number,
        "/" : first_number / next_number,
    }
    result = number_operations[operation]
    print(f"{first_number} {operation} {next_number} = {result}")
    continue_calc = input("Type 'y' to continue calculating with 60.0, or type 'n' to start a new calculation:")
    if continue_calc == 'y':
        first_number = result
    else:
        continue_loop = False