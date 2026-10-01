def divide(a, b):
    try:
        result = int(a) / int(b)
        print("Result:", result)
    except ValueError:
        print("Error: please enter integers")
    except ZeroDivisionError:
        print("Error: division by zero")
    finally:
        print("Finally block executed")


def main():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    divide(a, b)


main()
