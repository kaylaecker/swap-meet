from swap_meet.item import Item


class Clothing(Item):
    def __init__(self, category="Clothing", condition=0, age=None):
        super().__init__(category, condition, age)

    def __str__(self):
        return super().__str__("The finest clothing you could wear.")

    def condition_description(self):
        return super().condition_description()
