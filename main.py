from random import randint as random

inventory_path = "Tacos/inventory.txt"
inventory: dict[str] = {}

def save_inventory():
    with open(inventory_path, "w") as file:
        for k, v in inventory.items():
            file.write(f"{k}:{v}\n")

def load_inventory():
    with open(inventory_path, "r") as file:
        for line in file:
            split_line = line.split(":")
            inventory[split_line[0]] = int(split_line[1])

def sell_tacos():
    if inventory["tacos"] <= 0:
        return "You have no tacos!\n"
    amount = int(input(f"How many tacos do you want to sell? (You can sell {inventory['tacos']} tacos): "))
    if inventory["tacos"] >= amount:
        inventory["tacos"] -= amount
        inventory["cash"] += inventory["taco_price"] * amount
        save_inventory()
        return f"\nSold {amount} tacos\nTacos in inventory: {inventory['tacos']}"
    else:
        return f"\nNot enough tacos!\nThere are {inventory['tacos']} in inventory"

def buy_tacos():
    price = random(10, 40)
    print(f"A vendor is offering at ${price} each")
    decision = input("Accept the offer? [Y/N]: ")
    match decision.lower():
        case "y":
            if inventory["cash"] <= price:
                return "You don't have enough money to buy tacos!\n"
            available_money: int = inventory["cash"]
            available_tacos: int = 0
            while available_money >= 0:
                available_tacos += 1
                available_money -= price
            quantity = int(input(f"How many tacos do you want to buy? (You can buy {available_tacos-1} tacos): "))
            total = quantity * price
            if inventory["cash"] >= total:
                inventory["cash"] -= total
                inventory["tacos"] += quantity
                save_inventory()
                return f"\nBought {quantity} tacos\nNow there are {inventory['tacos']} tacos in inventory"
            else:
                return f"\nYou don't have enough money to buy {quantity} tacos!\nYou have ${inventory['cash']}, you need ${abs(inventory['cash']-total)} more\n"
        case "n":
            return "\n"
        case _:
            return "\nOption out of range"

def change_price(price: int):
    inventory["taco_price"] = price
    save_inventory()
    return "Price changed successfully!"

def main() -> None:
    load_inventory()
    print("Welcome to the taco sales program!")

    continue_program = True
    while continue_program:
        print("What do you want to do?\n", "1-Sell tacos   2-Buy tacos   3-Change taco price   4-View inventory   5-Exit")
        decision = int(input(""))

        match decision:
            case 1:
                print(sell_tacos())
            case 2:
                print(buy_tacos())
            case 3:
                print(change_price(int(input("What price do you want to set?: "))))
            case 4:
                for k, v in inventory.items():
                    if k == "taco_price":
                        continue
                    print(f"{k}: {v}.", end=" ")
                print("\n")
            case 5:
                continue_program = False

if __name__ == "__main__":
    main()
