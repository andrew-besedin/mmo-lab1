def sum_negative(numbers):
    total = 0
    for x in numbers:
        if x < 0:
            total += x
    return total


def sum_between_zeros(numbers):
    if numbers.count(0) < 2:
        return 0
    first = numbers.index(0)
    second = numbers.index(0, first + 1)
    return sum(numbers[first + 1:second])


def main():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Sum of negative elements:", sum_negative(numbers))
    print("Sum between the first two zeros:", sum_between_zeros(numbers))


main()
