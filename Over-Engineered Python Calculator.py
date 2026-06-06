import math


operator = input("Enter the Operator ( + , - , * , / , ** , sqrt ): ")

# Addition Function
if operator == "+":                                                                         
    num1 = input("Enter the First Number: ")
    num2 = input("Enter the Second Number: ")

    valid = True

    # Checks if the user have entered the number or not
    if not num1 or not num2:
        print("Enter the BOTH the Numbers first!")                                     
        valid = False

    # Checks the Validity
    elif valid:
        try:
            num1 = float(num1)  # Checking and Trying to change the input (First Number) to a Floating Point  

        except ValueError:
            print(f"'{num1}' is not a Valid Number!")
            valid = False

        try:                       
            num2 = float(num2)  # Checking and Trying to change the input (Second Number) to a Floating Point 

        except ValueError:
            print(f"'{num2}' is not a Valid Number!")
            valid = False
        
    # Finally the Actual Calculator itself
    if (num1 and num2) and valid:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 + num2
        result = str(result)     
        print(f"The Answer is: {result}")
    
# Subtraction Function   
elif operator == "-":
    num1 = input("Enter the First Number: ")
    num2 = input("Enter the Second Number: ")

    valid = True
    
    # Checks if the user have entered the number or not
    if not num1 or not num2:
        print("Enter the BOTH the Numbers first!")
        valid = False

    # Checks the Validity
    elif valid:
        try:
            num1 = float(num1)  # Checking and Trying to change the input (First Number) to a Floating Point  

        except ValueError:
            print(f"'{num1}' is not a Valid Number!")
            valid = False

        try:
            num2 = float(num2)  # Checking and Trying to change the input (Second Number) to a Floating Point 

        except ValueError:
            print(f"'{num2}' is not a Valid Number!")
            valid = False



    # Finally the Actual Calculator itself
    if (num1 and num2) and valid:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 - num2
        result = str(result)     
        print(f"The Answer is: {result}")

# Multiplication Function
elif operator == "*":
    num1 = input("Enter the First Number: ")
    num2 = input("Enter the Second Number: ")

    valid = True
    
    # Checks if the user have entered the number or not
    if not num1 or not num2:
        print("Enter the BOTH the Numbers first!")
        valid = False

    # Checks the Validity
    elif valid:
        try:
            num1 = float(num1)  # Checking and Trying to change the input (First Number) to a Floating Point  

        except ValueError:
            print(f"'{num1}' is not a Valid Number!")
            valid = False

        try:
            num2 = float(num2)  # Checking and Trying to change the input (Second Number) to a Floating Point 

        except ValueError:
            print(f"'{num2}' is not a Valid Number!")
            valid = False

    # Finally the Actual Calculator itself
    if (num1 and num2) and valid:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 * num2
        result = str(result)     
        print(f"The Answer is: {result}")

# Division Function
elif operator == "/":
    num1 = input("Enter the Main Number (Dividend): ")
    num2 = input("Enter the Number by which you want to divide the main number (Divisor): ")

    valid = True
    
    # Checks if the user have entered the number or not
    if not num1 or not num2:
        print("Enter the BOTH the Numbers first!")
        valid = False

    # Checks the Validity
    elif valid:
        try:
            num1 = float(num1)  # Checking and Trying to change the input (First Number) to a Floating Point  

        except ValueError:
            print(f"'{num1}' is not a Valid Number!")
            valid = False

        try:
            num2 = float(num2)  # Checking and Trying to change the input (Second Number) to a Floating Point 

        except ValueError:
            print(f"'{num2}' is not a Valid Number!")
            valid = False

    # Finally the Actual Calculator itself
    if (num1 and num2) and valid:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 / num2
        result = str(result)     
        print(f"The Answer is: {result}")

# Exponent Function
elif operator == "**":
    base = input("Enter the Base Number: ")
    power = input("Enter the POWER to which you want to raise the base number: ")

    valid = True

    # Checks if the user have entered the number or not
    if not base or not power:
        print("Enter the BOTH the Numbers first!")                                     
        valid = False

    # Checks the Validity
    elif valid:
        try:
            base = float(base)  # Checking and Trying to change the input (Base Number) to a Floating Point  

        except ValueError:
            print(f"'{base}' is not a Valid Number!")
            valid = False

        try:                       
            power = float(power)  # Checking and Trying to change the input (Power Number) to a Floating Point 

        except ValueError:
            print(f"'{power}' is not a Valid Number!")
            valid = False

    # Finally the Actual Calculator itself
    if (base and power) and valid:
        base = float(base)
        power = float(power)
        result = pow(base, power)
        result = str(result)     
        print(f"The Answer is: {result}")

# Square root Function
elif operator == "sqrt":
    try:
        num = int(input("Enter the number: ").strip())  # Takes input and tries to convert it to an int number

        if num < 0:  # Prevents the user from entering a Negative Number
            print("Negative numbers not allowed.")
        else:
            print("The Answer is:", math.sqrt(num))

    except ValueError:
        print("Invalid input! Enter a whole number.")

# Else statement for an invalid operator
else:
    print(f"'{operator}' is not a Valid OPERATOR")
