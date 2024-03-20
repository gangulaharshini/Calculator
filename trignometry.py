import math

def sin(angle):
    return math.sin(math.radians(angle))

def cos(angle):
    return math.cos(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def main():
    try:
        angle = float(input("Enter the angle in degrees: "))
        print("Sin:", sin(angle))
        print("Cos:", cos(angle))
        print("Tan:", tan(angle))
    except ValueError:
        print("Please enter a valid angle.")

if __name__ == "__main__":
    main()
