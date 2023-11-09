#!! CODE CAN BE SIMPLIFIED PLEASE REFACTOR !!
class Item:
    def __init__(self, name, price, rarity, buff, item_type):
        self.name = name
        self.price = price
        self.rarity = rarity
        self.buff = buff

    def equip_item(self, character):
        character.defense_x += self.buff / 20
        if "chestplate" in self.name:
            character.chestplate = self
        elif "leggings" in self.name:
            character.leggings = self
        elif "boots" in self.name:
            character.boots = self
        elif "helmet" in self.name:
            character.helmet = self
        else:
            character.weapon = self

    def unequipped_item(self, character):
        character.defense_x -= self.buff / 20
        if "chestplate" in self.name:
            character.chestplate = None
        elif "leggings" in self.name:
            character.leggings = None
        elif "boots" in self.name:
            character.boots = None
        elif "helmet" in self.name:
            character.helmet = None
        else:
            character.weapon = None
