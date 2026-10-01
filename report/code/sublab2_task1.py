def is_password_good(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_digit = False
    for c in password:
        if c.isupper():
            has_upper = True
        if c.isdigit():
            has_digit = True
    return has_upper and has_digit


def main():
    password = input("Enter a password: ")
    print("Password is good:", is_password_good(password))


main()
