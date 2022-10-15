
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

availability = {
    'water':250,
    'milk':100,
    'coffee':24
}
profit = 0


def process():
    print('please insert coins !')
    total = int(input('How many quarters ? ')) * 0.25
    total += int(input('How many dimes ? ')) * 0.1
    total += int(input('How many nickles ? ')) * 0.05
    total += int(input('How many pennies ? ')) * 0.01
    return total


def is_transaction_successful(money_received ,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost ,2)
        print(f'Here is change ${change}')
        global profit
        profit += drink_cost
        return True
    else:
        print('So sorry that is not enough money . Money refunded. ')
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        availability[item]-=order_ingredients[item]
    print(f'Here is your {drink_name}! ')


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > availability[item]:
            print(f'sorry there is not enough {item} .')
            return False
        return True


end_coffee = False

while not end_coffee:
    user_choice = input('What would you like ? (espresso/latte/cappuccino): ').lower()
    if user_choice == 'off':
        end_coffee = False
    elif user_choice == 'report':
        print(f"Water: {availability['water']}ml")
        print(f"Milk: {availability['milk']}ml")
        print(f"Coffee: {availability['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process()
            if is_transaction_successful(payment ,drink['cost']):
                make_coffee(user_choice, drink['ingredients'])



