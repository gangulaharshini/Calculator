def calculate_percentage(number, percent):
    return (number * percent) / 100

def main():
    try:
        number = float(input("Enter the number: "))
        percent = float(input("Enter the percentage: "))
        result = calculate_percentage(number, percent)
        print(f"{percent}% of {number} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
