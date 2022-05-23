from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
mn = Menu()


def machine_on():
    choice = input(f"What would you like? ({mn.get_items()}) ").lower()
    if choice == "off":
        return
    if choice == "report":
        cm.report()
        mm.report()
    else:
        drink_choice = mn.find_drink(choice)
        if not drink_choice:
            machine_on()
        check_resources = cm.is_resource_sufficient(drink_choice)
        if check_resources:
            payment = mm.make_payment(drink_choice.cost)
        else:
            machine_on()
        if payment:
            cm.make_coffee(drink_choice)
        machine_on()


machine_on()
