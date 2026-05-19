from calculator import add, subtract, multiply, divide

def main():
    print("Smart Calculator")
    print("Operations: +, -, *, /")
    try:
        a = float(input("First number: "))
        op = input("Operator (+, -, *, /): ")
        b = float(input("Second number: "))

        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        else:
            print("Unknown operator")
            return

        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()