#!python3
"""
##### Task 5
create a dictionary for an inventory of items in a game.  Ask the user for input,
and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' 
remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""
possible_items = {
    "food": "food",
    "water": "water",
    "rope": "rope",
    "torch": "torch",
    "sack": "sack",
    "wood": "wood",
    "iron": "iron",
    "steel": "steel",
    "ginger": "ginger",
    "garlic": "garlic",
    "fish": "fish",
    "stone": "stone",
    "wool": "wool"
}

inventory = {}

while True:
    action = input("Enter an action (get item, drop item, inventory, possible, or exit): ").lower()
    
    if action == "get item":
        print("Possible items to get:")
        for item in possible_items.values():
            print(item)
        
        item = input("Enter the item you want to add to your inventory: ").lower()
        quantity = 1
        parts = item.split()
        
        if len(parts) > 1 and parts[0].isdigit():
            quantity = int(parts[0])
            item = " ".join(parts[1:])
        
        # Check if the entered item is a known item or an abbreviation
        for known_item, full_name in possible_items.items():
            if item in known_item or item in full_name:
                item = full_name
                break
        else:
            print("Unknown item. Please enter a valid item.")
            continue
        
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        print(f"You got {quantity} {item}.")
    
    elif action == "drop item":
        item = input("Enter the item you want to drop from your inventory: ").lower()
        
        # Check if the entered item is a known item or an abbreviation
        for known_item, full_name in possible_items.items():
            if item in known_item or item in full_name:
                item = full_name
                break
        else:
            print("Unknown item. Please enter a valid item.")
            continue
        
        if item in inventory:
            quantity = int(input(f"How many {item} do you want to drop? (You have {inventory[item]}): "))
            if quantity >= inventory[item]:
                del inventory[item]
            else:
                inventory[item] -= quantity
                print(f"You dropped {quantity} {item}.")
        else:
            print("You don't have that item in your inventory.")
    
    elif action == "inventory":
        if inventory:
            print("You have:")
            for item, quantity in inventory.items():
                print(f"{quantity} {item}")
        else:
            print("Your inventory is empty.")
    
    elif action == "possible":
        print("Possible items to get:")
        for item in possible_items.values():
            print(item)
    
    elif action == "exit":
        break
    
    else:
        print("Invalid action. Please choose from 'get item', 'drop item', 'inventory', 'possible', or 'exit'.")