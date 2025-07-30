from .menu import Menu
from .money_machine import MoneyMachine

money_machine = MoneyMachine()


class CoffeeMachine:

    def __init__(self):
        self.is_machine_on = True
        self.resources = [
            {
                "name": "water",
                "quantity": 300,
                "unit": "ml"
            },
            {
                "name": "milk",
                "quantity": 200,
                "unit": "ml"
            },
            {
                "name": "coffee",
                "quantity": 100,
                "unit": "g"
            },
        ]

    def report(self):

        for resource in self.resources:
            name = resource.get("name", "unknown").strip().capitalize()
            quantity = resource.get("quantity", 0)
            unit = resource.get("unit", "")
            print(f"{name}: {quantity}{unit}")

        money_machine.report()

    def is_resource_sufficient(self, drink_details):

        for ingredient, required_qty in drink_details.ingredients.items():
            found = False
            for resource in self.resources:
                if resource["name"] == ingredient:
                    found = True
                    if resource["quantity"] < required_qty:
                        print(
                            f"❌ Not enough {ingredient}. Needed: {required_qty}, Available: {resource['quantity']}"
                        )
                        return False
                    break
            if not found:
                print(f"⚠️ Ingredient '{ingredient}' not found in resources.")
                return False
        print("✅ Resources are sufficient.")
        return True

    def make_coffee(self, drink):
        for ingredient, required_qty in drink.ingredients.items():
            for resource in self.resources:
                if resource["name"] == ingredient:
                    resource["quantity"] -= required_qty
                    break
        print(f"Here is your {drink.name} ☕️. Enjoy!")

    def run(self):
        menu = Menu()
        options = "/".join(menu.get_menu_options())
        while self.is_machine_on:
            choose_drink = input(f"What would you like? ({options}): ")

            if choose_drink not in menu.get_menu_options() + ["end", "report"]:
                raise ValueError("Please choose valid options")

            try:
                if choose_drink == "end":
                    self.is_machine_on = False
                    print("coffee machine is off now ")
                    break
                elif choose_drink == "report":
                    self.report()
                else:
                    drink_details = menu.drink_select(choose_drink)

                    if self.is_resource_sufficient(
                            drink_details) and money_machine.make_payment(
                                drink_details.cost):
                        self.make_coffee(drink_details)
            except ValueError as error:
                print(error)
        # self.is_machine_on = False
