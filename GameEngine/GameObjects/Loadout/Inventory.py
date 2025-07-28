class Inventory:

#make sure that only Item are being Added - Exception Handling!
    def __init__(self):
        self.items = []

    def add(self, item_obj):
        self.items.append(item_obj)

    def remove(self, item_obj):
        if item_obj in self.items:
            self.items.remove(item_obj)
        else:
            raise Exception(f"Item {item_obj} not found in inventory.")

    def has(self, item_obj):
        return item_obj in self.items
    
    def show(self):
        return [item.name for item in self.items]
