#Ask the user to input two numbers
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

#Ask for the type of operation
operation_type = input("Choose the operation (+, -, *, /):")

#Perform the Calculation Using Match Case
match operation_type:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")

    case "-":
        result = num1 - num2
        print(f"The result is {result}")

    case "*":
        result = num1 * num2
        print(f"The result is {result}")

    case "/":
        if num2 == 0:
            print ("cannot divide by zero")
        else :
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation selected.")