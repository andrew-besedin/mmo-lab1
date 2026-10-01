def count_even_odd(number):
    even = 0
    odd = 0
    for d in number:
        if d.isdigit():
            if int(d) % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd


def main():
    number = input("Enter a number: ")
    even, odd = count_even_odd(number)
    print("Even digits:", even)
    print("Odd digits:", odd)


main()
