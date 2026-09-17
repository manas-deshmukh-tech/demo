while True:
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result =", a + b)

        case 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result =", a - b)

        case 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result =", a * b)

        case 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result =", a / b)

        case 5:
            n = int(input("Enter number: "))
            fact = 1

            for i in range(1, n + 1):
                fact = fact * i

            print("Factorial =", fact)

        case 6:
            print("Exiting...")
            break

        case _:
            print("Invalid choice")