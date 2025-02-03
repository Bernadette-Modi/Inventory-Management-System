class Inventory:
    def __init__(self):
        self.items = {}

    def add_items(self, name, quantity, price):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'quantity': quantity, 'price': price}
            print(f"{quantity} of {name} added to inventory.")

    def update_item(self, name, quantity, price):
        if name in self.items:
            self.items[name] = {'quantity': quantity, 'price': price}
            print(f"{name} updated successfully.")
        else:
            print(f"{name} not fount in inventory.")
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} removed from inventory.")
        else:
            print(f"{name} not found in inventory.")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("\ncurrent Inventory: ")
            for name, details in self.items.items():
                print(f"{name} - Quantity: {details['quantity']}, Price: ${details['price']}")
    
