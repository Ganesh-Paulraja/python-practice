from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# result = operations["*"](2,3)

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pikc an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n * 5")
            calculator() #--> It will rull this code again recursion

calculator()