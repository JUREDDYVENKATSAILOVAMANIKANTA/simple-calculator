
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error! Division by zero."

print("Welcome to Simple Calculator")

while True:
    choice = input("Choose an operation (1: Addition, 2: Subtraction, 3: Multiplication, 4: Division, 5: Quit): ")

    if choice == '5':
        print("Thank you for using Simple Calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        
        # Format the result to remove trailing ".0" for whole numbers
        formatted_result = result if result % 1 != 0 else int(result)
        print("Result:", formatted_result)

    else:
        print("Invalid input! Please choose a valid operation.")