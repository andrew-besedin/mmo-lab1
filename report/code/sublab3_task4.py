class BankAccount:
    interest_rate = 5
    accounts_count = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.accounts_count += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount

    def add_interest(self):
        self.balance += self.balance * BankAccount.interest_rate / 100

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @classmethod
    def get_accounts_count(cls):
        return cls.accounts_count

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


def main():
    owner = input("Enter owner name: ")
    balance = float(input("Enter start balance: "))
    account = BankAccount(owner, balance)

    amount = float(input("Enter deposit amount: "))
    if BankAccount.is_valid_amount(amount):
        account.deposit(amount)
    else:
        print("Invalid amount")

    amount = float(input("Enter withdraw amount: "))
    if BankAccount.is_valid_amount(amount):
        account.withdraw(amount)
    else:
        print("Invalid amount")

    rate = float(input("Enter interest rate: "))
    BankAccount.set_interest_rate(rate)
    account.add_interest()

    print("Owner:", account.owner)
    print("Balance:", account.balance)
    print("Accounts count:", BankAccount.get_accounts_count())


main()
