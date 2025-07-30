import json


class MenuItem:

    def __init__(self, name: str, ingredients: dict[str, float], cost: float):
        self.name = name
        self.ingredients: dict[str, float] = ingredients
        self.cost = cost

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


class Menu:

    def __init__(self):
        self.menu = [
            MenuItem(
                "espresso",
                {
                    "water": 50,
                    "coffee": 18,
                },
                1.5,
            ),
            MenuItem(
                "latte",
                {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                2.5,
            ),
            MenuItem(
                "cappuccino",
                {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                3.0,
            ),
        ]

    def get_menu_options(self):
        return [drink.name for drink in self.menu]

    def drink_select(self, drink_name: str):
        for drink in self.menu:
            if drink.name == drink_name:
                return drink
        return None
