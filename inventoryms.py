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
