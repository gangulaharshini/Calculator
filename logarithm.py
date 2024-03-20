import math

def calculate_logarithm(number, base):
    return math.log(number, base)

def main():
    try:
        number = float(input("Enter the number: "))
        base = float(input("Enter the base of the logarithm: "))
        
        if number <= 0 or base <= 0:
            print("Both number and base must be positive.")
            return
        
        result = calculate_logarithm(number, base)
        print(f"The logarithm of {number} with base {base} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
