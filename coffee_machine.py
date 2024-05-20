
def machine_has(water, milk, beans, cups_disposable,money):
    print("The coffe machine has:")
    print(f"{water} ml of water")
    print(f"{milk} ml of milk")
    print(f"{beans} g of coffee beans")
    print(f"{cups_disposable} disposable cups ")
    print(f"${money} of money")


def buy(water, milk, beans, cups_disposable, money):
    coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if coffee == "back":
        pass
    elif coffee == "1":
        if water < 250 or beans <16:
            print("Sorry, not enough water or milk!")
            return water, milk, beans, cups_disposable, money
        else:
            water -= 250
            beans -= 16
            cups_disposable -= 1
            money += 4
    elif coffee == "2":
        if water < 350 or milk < 75 or beans < 20:
            print("Sorry, not enough water or milk!")
            return water, milk, beans, cups_disposable, money
        else:
            water -= 350
            milk -= 75
            beans -= 20
            cups_disposable -= 1
            money += 7
    elif coffee == "3":
        if water < 200 or milk < 100 or beans < 12:
            print("Sorry, not enough water or milk!")
            return water, milk, beans, cups_disposable, money
        else:
            water -= 200
            milk -= 100
            beans -= 12
            cups_disposable -= 1
            money += 6
    print("I have enough resources, making you a coffee!")
    return water, milk, beans, cups_disposable, money

def fill(water, milk, beans, cups_disposable):
    water += int(input("Write how many ml of water you want to add:\n"))
    milk += int(input("Write how many ml of milk you want to add:\n"))
    beans += int(input("Write how many grams of coffee beans you want to add:\n"))
    cups_disposable += int(input("Write how many disposable cups you want to add:\n"))
    return water, milk, beans, cups_disposable

def take(money):
    print(f"I gave you ${money}")
    money = 0
    return money

def main():
    water = 400
    milk = 540
    beans = 120
    cups_disposable = 9
    money = 550

    while True:
        action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            print("")
            water, milk, beans, cups_disposable, money = buy(water, milk, beans, cups_disposable, money)
        elif action == "fill":
            print("")
            water, milk, beans, cups_disposable = fill(water, milk, beans, cups_disposable)
        elif action == "take":
            print("")
            money = take(money)
        elif action == "remaining":
            print("")
            machine_has(water, milk, beans, cups_disposable, money)
        elif action == "exit":
            return

main()