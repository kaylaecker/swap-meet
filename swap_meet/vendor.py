class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item

    def get_by_category(self, category):
        items_in_category = []
        for thing in self.inventory:
            if thing.category == category:
                items_in_category.append(thing)
        return items_in_category

    def swap_items(self, vendor, item_to_give, item_to_receive):
        if item_to_give in self.inventory and item_to_receive in vendor.inventory:
            self.inventory.remove(item_to_give)
            self.inventory.append(item_to_receive)
            vendor.inventory.remove(item_to_receive)
            vendor.inventory.append(item_to_give)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        [self.inventory[0], vendor.inventory[0]] = [
            vendor.inventory[0],
            self.inventory[0],
        ]
        return True

    def get_best_by_category(self, item_category):
        applicable_items = self.get_by_category(item_category)

        if not applicable_items:
            return None

        highest_item = applicable_items[0]

        for current_item in applicable_items:
            if highest_item.condition < current_item.condition:
                highest_item = current_item

        return highest_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best, their_best)
