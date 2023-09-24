from typing import List
from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        phone_number = [n for n in self.clients_list if n.phone_number == client_phone_number]

        if phone_number:
            raise Exception('The client has already been registered!')

        result = Client(client_phone_number)
        self.clients_list.append(result)
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        return '\n'.join([meal.details() for meal in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        meals = []
        current_bill = 0

        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        existing_client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if not existing_client:
            client = Client(client_phone_number)
            self.clients_list.append(client)
        else:
            client = existing_client[0]

        for meal_name, meal_qty in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_qty:
                        meals.append(meal)
                        current_bill += meal.price * meal_qty
                        break
                    else:
                        raise Exception(f'Not enough quantity of {type(meal).__name__}: {meal_name}!')
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        for meal_name, meal_qty in meal_names_and_quantities.items():
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_qty
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_qty

        client.shopping_cart.extend(meals)
        client.bill += current_bill
        return f"Client {client_phone_number} successfully ordered" \
               f" {', '.join([meal for meal in client.ordered_meals])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        for meal, qty in client.ordered_meals.items():
            for menu_meal in self.menu:
                if meal == menu_meal.name:
                    menu_meal.quantity += qty
        client.shopping_cart.clear()
        client.bill = 0
        return f'Client {client_phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number][0]

        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')

        total_paid = client.bill
        client.shopping_cart = []
        client.bill = 0
        self.receipt_id += 1

        return f'Receipt #{self.receipt_id} with total amount of {total_paid:.2f} was successfully paid for {client_phone_number}.'

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."





