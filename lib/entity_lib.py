import random


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

    def use_move(self, move, opponent, func) -> None:
        if self.mana <= 0:
            return
        try:
            if bool(move.miss_chance <= random.randint(1, 100)):
                return
            elif bool(move.crit_chance <= random.randint(1, 100)):
                move.damage *= 1.3
        except AttributeError:
            move.use_move(self)
        if move.move_type == "Healing":
            self.heal(move.amount)
        elif move.move_type == "Stat":
            move.stat_change(self)
        else:
            move.damage = move.calculate_damage()
            opponent.health -= move.damage
            if not func:
                return
            opponent.check_dead(func)

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

    def level_up(self, xp_required):
        if self.xp >= xp_required[self.level + 1]:
            self.level += 1


class Mob(Entity):
    def __init__(self, name, level, health, max_health, mana, max_mana, coins_on_death):
        super().__init__(name, level, health, max_health, mana, max_mana)
        self.coins_on_death = coins_on_death

