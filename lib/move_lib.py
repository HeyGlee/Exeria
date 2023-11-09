import random


class Move:    # base class for all moves (never actually used but only used as a template for all others)
    def __init__(self, name, cost, move_type):
        self.name = name
        self.cost = cost
        self.move_type = move_type

    def use_move(self, entity):    # this takes the entity which is the 'thing' using the move and calculates the mana.
        new_mana = entity.Mana - self.cost
        if new_mana < 0:
            new_mana = 0    # <- just in case mana is smaller than 0 after a move it will set it to 0
        entity.mana = new_mana


class Attack(Move):    # base class for all attacking moves (ranged & physical)
    def __init__(self, name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits):
        super().__init__(name, cost, move_type)
        self.damage = damage
        self.miss_chance = miss_chance
        self.crit_chance = crit_chance
        self.recoil = recoil
        self.hits = hits

    def calculate_damage(self, user, opponent) -> int:    # takes into account the attack stat of the character and the defense stat of the opponent + projectile amount
        return self.damage * random.randint(1, self.hits) * user.damage_x * opponent.defense_x    # returns the damage


class RangedAttack(Attack):    # if the move is a ranged move it is more likely to miss as you are using a projectile
    def __init__(self, name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits):
        super().__init__(name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits)
        self.miss_chance *= 1.1    # may need buff as it has no current effect like melee moves


class MeleeAttack(Attack):    # if you are using a physical move then you are more likely to get a crit as if you land it will be more powerful
    def __init__(self, name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits):
        super().__init__(name, cost, move_type, damage, miss_chance, crit_chance, recoil, hits)
        self.crit_chance *= 1.5  
        self.miss_chance *= 1.3


class StatMove(Move):    # these moves increase the stat of the user
    def __init__(self, name, cost, move_type, amount, stat):
        super().__init__(name, cost, move_type)
        self.amount = amount
        self.stat = stat

    def stat_change(self, entity):
        if self.stat == "Attack":    # checks if the move is increasing attack or defense
            entity.damage_x *= self.amount
        else:
            entity.defense_x *= self.amount


class HealthMove(Move):
    def __init__(self, name, cost, move_type, health_given):
        super().__init__(name, cost, move_type)
        self.health_given = health_given    # the health given is all calculated in the entity_lib as that is where the heal() method is actually defined.
