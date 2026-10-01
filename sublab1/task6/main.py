def find_max(numbers):
    result = numbers[0]
    for x in numbers:
        if x > result:
            result = x
    return result


def find_min(numbers):
    result = numbers[0]
    for x in numbers:
        if x < result:
            result = x
    return result


def main():
    numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Maximum element:", find_max(numbers))
    print("Minimum element:", find_min(numbers))


main()
