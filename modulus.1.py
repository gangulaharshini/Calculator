# include def modulus(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 % num2

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = modulus(num1, num2)
        print("Result:", result)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
