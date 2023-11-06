class Entity:
    def __init__(self, name, level, health, max_health, mana, max_mana):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.is_dead = False
        self.moves = []

    def heal(self, amount: int) -> None:
        heal = self.health + amount
        if heal > self.max_health:
            heal -= heal - self.max_health
        self.health = heal

    def use_move(self, move: object, opponent: object) -> None:
        pass

    def check_dead(self, func) -> None:
        if self.health <= 0:
            self.is_dead = True
            func()


class Character(Entity):
    def __init__(self, name, level, health, max_health, mana, max_mana, xp, coins, damage_x, defense_x,
                 helmet, chestplate, leggings, boots, weapon):
        super().__init__(name, level, health, max_health, mana, max_mana)
        self.xp = xp
        self.coins = coins
        self.damage_x = damage_x
        self.defense_x = defense_x
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.weapon = weapon
    
    def level_up(self):
        pass
    
