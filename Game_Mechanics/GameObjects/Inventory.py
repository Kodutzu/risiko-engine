class Inventory:

    def __init__(self):
        self.items = []

    def addItem(self, item_obj):
        self.items.append(item_obj)

    def removeItem(self, item_obj):
        if item_obj in self.items:
            self.items.remove(item_obj)
        else:
            raise Exception(f"Item {item_obj} not found in inventory.")

    def hasItem(self, item):
        return item in self.items
