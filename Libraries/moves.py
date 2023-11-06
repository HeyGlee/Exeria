moves = {}


class Move:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.moveType = "Nothing"

    def use_move(self, entity):
        new_mana = entity.Mana - self.cost
        if new_mana < 0:
            new_mana = 0
        entity.mana = new_mana


class Attack(Move):

    def __init__(self, name, cost, damage, miss_chance, crit_chance, recoil):
        super().__init__(name, cost)
        self.damage = damage
        self.missChance = miss_chance
        self.critChance = crit_chance
        self.recoil = recoil
        self.moveType = "Attack"


class HealingMove(Move):

    def __init__(self, name, cost, health_given):
        super().__init__(name, cost)
        self.healthGiven = health_given
        self.moveType = "healUp"

# Adding in moves


# -- health moves --
moves["Small heal"] = HealingMove("Small heal", 20, 30)
moves["Medium heal"] = HealingMove("Medium heal", 50, 60)
moves["Big heal"] = HealingMove("Big heal", 70,
                                120)  # <-- least common healing move

# -- attacking moves --
moves["Breaking strike"] = Attack("Breaking strike", 40, 60, 5, 3, 0.08)
moves["Eagle's sweep"] = Attack("Eagle's sweep", 30, 55, 3, 4, 0)
moves["Bite"] = Attack("Bite", 25, 30, 0, 7, 0)
moves["Lightning spell"] = Attack("Lightning spell", 25, 40, 4, 3, 0)
moves["Super slash"] = Attack("Super slash", 50, 70, 9, 2, 0.12)
moves["Slash"] = Attack("Slash", 35, 45, 0, 4, 0)
moves["Barrage"] = Attack("Barrage", 45, 65, 6, 3, 0.1)  # Acquired at a high level (top 3 move OP moves)
