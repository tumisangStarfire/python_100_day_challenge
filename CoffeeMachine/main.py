from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
monies = MoneyMachine()


def print_machine_report():
    return coffee_maker.report(), monies.report()


def begin_order():
    machine_is_on = True
    while machine_is_on:
        drink_choices = menu.get_items()
        order = input(f"What would you like..? {drink_choices}:")
        if order == "off":
            machine_is_on = False
        elif order == "report":
            print_machine_report()
        else:
            selected_drink = menu.find_drink(order)
            if selected_drink is not None:
                can_make_drink = coffee_maker.is_resource_sufficient(selected_drink)
                if can_make_drink:
                    transaction_status = monies.make_payment(selected_drink.cost)
                    if transaction_status:
                        coffee_maker.make_coffee(selected_drink)
                else:
                    machine_is_on



begin_order()
