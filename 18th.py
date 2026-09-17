def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("----- Calculator -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice != 5:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

match choice:
    case 1:
        print("Result =", add(a, b))

    case 2:
        print("Result =", subtract(a, b))

    case 3:
        print("Result =", multiply(a, b))

    case 4:
        if b != 0:
            print("Result =", divide(a, b))
        else:
            print("Cannot divide by zero")

    case 5:
        print("Thank you!")

    case _:
        print("Invalid choice")