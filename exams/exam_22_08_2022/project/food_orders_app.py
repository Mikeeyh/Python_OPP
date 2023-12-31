from project.client import Client
from project.meals.meal import Meal
from typing import List


class FoodOrdersApp:
    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        pass

    def add_meals_to_menu(self, *meals: Meal):
        pass

    def show_menu(self):
        pass

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        pass

    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        pass
