import math

def square_root(number):
    if number < 0:
        raise ValueError("Square root of a negative number is undefined")
    return math.sqrt(number)

def sin(angle):
    return math.sin(math.radians(angle))

def cos(angle):
    return math.cos(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def main():
    print("Calculator Menu:")
    print("1. Calculate Square Root")
    print("2. Calculate Trigonometric Functions")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        try:
            number = float(input("Enter a number: "))
            result = square_root(number)
            print("Square root:", result)
        except ValueError as e:
            print(e)
    elif choice == '2':
        try:
            angle = float(input("Enter the angle in degrees: "))
            print("Sin:", sin(angle))
            print("Cos:", cos(angle))
            print("Tan:", tan(angle))
        except ValueError:
            print("Please enter a valid angle.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
