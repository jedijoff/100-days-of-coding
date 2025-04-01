from tokenize import endpats

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    for item in drink['ingredients']:
        if drink['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return
    return True


def process_coins(drink):
    print(f"Please insert coins to value of {drink['cost']}")
    quarters = int(input("how many quarters?: ").strip() or 0)
    dimes = int(input("how many dimes?: ").strip() or 0)
    nickles = int(input("how many nickles?: ").strip() or 0)
    pennies = int(input("how many pennies?: ").strip() or 0)
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total < drink['cost']:
        print("Sorry that's not enough money. Money refunded.")
        prompt_user()
    change = round(total - drink['cost'], 2)
    print("Here is %.2f in change." % change)
    return True


def make_coffee(drink, user_input):
    for item in drink['ingredients']:
        resources[item] -= drink['ingredients'][item]
    print(f"Here is your {user_input}. Enjoy!")
    return


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    return


def turn_off():
    global machine_is_on
    machine_is_on = False
    return


machine_is_on = True

while machine_is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").strip()

    if user_input.lower() == "report":
        report()
    elif user_input.lower() == "off":
        turn_off()
    elif user_input.lower() in MENU:
        drink = MENU[user_input.lower()]
        if check_resources(drink):
            if process_coins(drink):
                make_coffee(drink, user_input)



