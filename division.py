def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = divide(num1, num2)
        print("Result:", result)
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

if __name__ == "__main__":
    main()
num 3