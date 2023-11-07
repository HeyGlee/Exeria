import random


class Move:
    def __init__(self, name, cost, move_type):
        self.name = name
        self.cost = cost
        self.move_type = move_type

    def use_move(self, entity):
        new_mana = entity.Mana - self.cost
        if new_mana < 0:
            new_mana = 0
        entity.mana = new_mana


class Attack(Move):
    def __init__(self, name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits):
        super().__init__(name, cost, move_type)
        self.damage = damage
        self.miss_chance = miss_chance
        self.crit_chance = crit_chance
        self.recoil = recoil
        self.hits = hits

    def calculate_damage(self) -> int:
        return self.damage * random.randint(1, self.hits)


class RangedAttack(Attack):
    def __init__(self, name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits):
        super().__init__(name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits)
        self.miss_chance *= 1.1


class MeleeAttack(Attack):
    def __init__(self, name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits):
        super().__init__(name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits)
        self.crit_chance *= 1.5


class StatMove(Move):
    def __init__(self, name, cost, move_type, amount, stat):
        super().__init__(name, cost, move_type)
        self.amount = amount
        self.stat = stat

    def stat_change(self, entity):
        if self.stat == "Attack":
            entity.damage_x *= self.amount
        else:
            entity.defense_x *= self.amount


class HealthMove(Move):
    def __init__(self, name, cost, move_type, health_given):
        super().__init__(name, cost, move_type)
        self.health_given = health_given
