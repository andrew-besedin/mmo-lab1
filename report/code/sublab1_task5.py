products = {
    "filter": ["oil filter, steel and paper", 450, 20],
    "pads": ["brake pads, steel and friction lining", 2300, 12],
    "spark plug": ["spark plug, ceramic and iridium", 600, 40],
    "battery": ["car battery, lead and electrolyte", 7800, 5],
    "belt": ["timing belt, reinforced rubber", 1900, 8],
}


def show_description():
    for name in products:
        print(name, "-", products[name][0])


def show_price():
    for name in products:
        print(name, "-", products[name][1])


def show_count():
    for name in products:
        print(name, "-", products[name][2])


def show_all():
    for name in products:
        print(name, "-", products[name][0], "- price:", products[name][1], "- quantity:", products[name][2])


def buy():
    total = 0
    while True:
        name = input("Product name (n - exit): ")
        if name == "n":
            break
        if name not in products:
            print("No such product")
            continue
        count = int(input("Quantity: "))
        if count > products[name][2]:
            print("Not enough in stock, available:", products[name][2])
            continue
        products[name][2] -= count
        total += products[name][1] * count
    print("Purchase total:", total)
    print("Left in the shop:")
    show_count()


def main():
    while True:
        print("\n1. View descriptions")
        print("2. View prices")
        print("3. View quantities")
        print("4. All information")
        print("5. Purchase")
        print("6. Goodbye")
        choice = input("Choose an option: ")
        if choice == "1":
            show_description()
        elif choice == "2":
            show_price()
        elif choice == "3":
            show_count()
        elif choice == "4":
            show_all()
        elif choice == "5":
            buy()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


main()
