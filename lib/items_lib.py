class Item:
    def __init__(self, name, price, rarity, buff):
        self.name = name
        self.price = price
        self.rarity = rarity
        self.buff = buff


    def increase_stat(self, stat, character):   # <- increases stat depending on its given param
        if stat == "defense":
            character.defense_x += self.buff / 20   # <- math for calculating buffs
        else:
            character.attack_x += self.buff / 20


    def equip_item(self, character, equipping, stat):
        result = None if not equipping else self   # <- uneqip is not equipping else add it to inv.
        self.increase_stat(stat, character)
        if "chestplate" in self.name:
            character.chestplate = result
        elif "leggings" in self.name:
            character.leggings = result
        elif "boots" in self.name:
            character.boots = result
        elif "helmet" in self.name:
            character.helmet = result
        else:
            character.weapon = result
    
    