class MoneyMachine:

    def __init__(self):
        self.money_received = 0
        self.profit = 0

    CURRENCY = "$"

    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def process_coin(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += (
                int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
            )
        return self.money_received

    def report(self):
        """Prints the current profit"""
        print(f"Money: { self.CURRENCY}{self.profit:.2f}")

    def make_payment(self, cost):
        self.process_coin()

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
