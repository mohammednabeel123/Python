print("~~~Welcome to the Simple Calculator~~~")

while True:
    user_input1 = int(input("Enter your first number: "))
    user_input2 = int(input("Enter your second number: "))

    print("Select an operation: *, +, -, /")
    operation = input("Enter the operation: ")

    # calculations using operators
    if operation == "+":
        calculation = user_input1 + user_input2
        print("Result:", calculation)

    elif operation == "-":
        calculation = user_input1 - user_input2
        print("Result:", calculation)

    elif operation == "*":
        calculation = user_input1 * user_input2
        print("Result:", calculation)

    elif operation == "/":
        calculation = user_input1 / user_input2
        print("Result:", calculation)

    else:
        print("Invalid operation")

    repeat = input("Do you want to repeat the program? (yes/no): ")
    if repeat.lower() != 'yes':
        break

    