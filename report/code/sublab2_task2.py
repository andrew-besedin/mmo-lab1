def max_key(d):
    best = None
    for key in d:
        if best is None or d[key] > d[best]:
            best = key
    return best


def count_before_negative(numbers):
    count = 0
    for n in numbers:
        if n < 0:
            break
        count += 1
    return count


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def digit_sum(s):
    total = 0
    for c in s:
        if c.isdigit():
            total += int(c)
    return total


def process(value):
    if isinstance(value, dict):
        print("Key with max value:", max_key(value))
    elif isinstance(value, list):
        print("Elements before first negative:", count_before_negative(value))
    elif isinstance(value, int):
        print("Is prime:", is_prime(value))
    elif isinstance(value, str):
        print("Reversed:", value[::-1])
        print("Sum of digits:", digit_sum(value))


def main():
    pairs = input("Enter dictionary as key:value pairs separated by spaces: ").split()
    d = {}
    for pair in pairs:
        key, val = pair.split(":")
        d[key] = int(val)
    process(d)

    numbers = list(map(int, input("Enter list of numbers: ").split()))
    process(numbers)

    number = int(input("Enter a number: "))
    process(number)

    s = input("Enter a string: ")
    process(s)


main()
