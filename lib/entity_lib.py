import random


class Entity:    # this is the parent class for every character in the game
    def __init__(self, name, level, health, max_health, mana, max_mana):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.is_dead = False
        self.moves = []    # empty list used for the character's moves

    def heal(self, amount: int) -> None:    # function to heal the character
        heal = self.health + amount    # gets the added amount
        if heal > self.max_health:
            heal -= heal - self.max_health    # subtracts heal by the amount over the users max health
        self.health = heal    # adds the new health to the users health

    def use_move(self, move, opponent, func) -> None:
        if self.mana <= 0:    # if the character has 0 mana then it will just instantly return and not use the move
            return
        try:   
            if bool(move.miss_chance <= random.randint(1, 100)):    # if the move misses it will just return
                return
            elif bool(move.crit_chance <= random.randint(1, 100)):    # calculates for crit
                move.damage *= 1.3
        except AttributeError:
            continue
        move.use_move(self)    # uses the moves mana
        if move.move_type == "Healing":    # checks for the type of move
            self.heal(move.amount)
        elif move.move_type == "Stat":
            move.stat_change(self)
        else:
            move.damage = move.calculate_damage()    # <- ISSUE: function needs to be updated to include the attack and defense buffs
            opponent.health -= move.damage    # deals the damage
            opponent.check_dead(func)

    def check_dead(self, func) -> None:    # method to check if the character is dead, runs a function if they are
        if self.health <= 0:
            self.is_dead = True
            func()


class Character(Entity):    # class for the user 
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

    def level_up(self, xp_required):    # checks for a level up. the xp_required is a dictionary with each level and the amount of xp needed to level up. May need to add try!
        if self.xp >= xp_required[self.level + 1]:
            self.level += 1


class Mob(Entity):    # main mob class, i haven't added side effects into this game so there are no sub-classes e.g. skeleton or fire skeleton. currently just this.
    def __init__(self, name, level, health, max_health, mana, max_mana, coins_on_death, xp_dropped):    # has extra prop. of the coins & xp dropped on death
        super().__init__(name, level, health, max_health, mana, max_mana)
        self.coins_on_death = coins_on_death 
        self.xp_dropped = xp_dropped

