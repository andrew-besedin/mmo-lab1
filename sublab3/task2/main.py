class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (100 - discount) / 100


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


class Human:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.house = None

    def __make_deal(self, house, price):
        self.money -= price
        self.house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.money < price:
            print("Not enough money to buy the house")
        else:
            self.__make_deal(house, price)
            print("House bought for", price)


def main():
    name = input("Enter your name: ")
    money = float(input("Enter your money: "))
    price = float(input("Enter small house price: "))
    discount = float(input("Enter discount in percent: "))
    human = Human(name, money)
    house = SmallHouse(price)
    human.buy_house(house, discount)
    print("Money left:", human.money)
    print("Has house:", human.house is not None)


main()
