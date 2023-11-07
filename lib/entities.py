import random
import time

from Libraries.move_index import moves


class Entity:

    def __init__(self, name, level, max_health, health):
        self.name = name
        self.level = level
        self.maxHealth = max_health
        self.health = health
        self.Moves = []

    def heal(self, amount):
        health = self.health + amount

        if health > self.maxHealth:
            health -= health - self.maxHealth

        self.health = health

    def use_move(self, opponent, move):
        if move.moveType == "Attack":
            is_missed = bool(move.missChance >= random.randint(1, 100))
            if is_missed:
                print(f"{self.name} used {move.name} but it missed!")
                return
            is_crit = bool(move.critChance >= random.randint(1, 100))

            if is_crit:
                move.damage *= 1.3
                print(f"{self.name} hit a critical hit on "
                      f"{opponent.name} with {move.name}!!!")
            else:
                print(f"{self.name} used {move.name}")

            opponent.health -= move.damage

        else:
            self.heal(move.healthGiven)
            print(f"{self.name} Healed! Health: {self.health}")


class Character(Entity):

    def __init__(self, name, level, max_health, health, mana, max_mana, status):
        super().__init__(name, level, max_health, health)
        self.XP = 0  # sets the xp for the player
        self.status = status  # used for special statuses e.g. poison
        self.Mana = mana
        self.Helmet = None
        self.BodyArmour = None
        self.Leggings = None
        self.Boots = None
        self.Weapon = "Basic Sword"
        self.Moves = [moves["Slash"], moves["Breaking strike"], moves["Bite"], moves["Small heal"]]
        self.Coins = 0
        self.isDead = False
        self.maxMana = max_mana
        self.defense = 1

    def Check_Dead(self, opponent, go_to):
        if self.health <= 0:
            self.health = 0
            self.isDead = True
            self.Coins -= random.randint(1, opponent.level * 20)
            if self.Coins <= 0:
                self.Coins = 0
            print("SYRIS: Death is for pathetic people.")
            time.sleep(0.8)
            print("SYRIS: It seems you have joined them. Disappointing")
            go_to()

    def add_move(self, move):
        if move not in moves:
            return

        self.Moves.append(moves[move])


class Mob(Entity):

    def __init__(self, name, level, max_health, health, coins_on_death, mana):
        super().__init__(name, level, max_health, health)
        self.Mana = mana
        self.coinsOnDeath = coins_on_death
        self.isDead = False

    def Check_Dead(self, opponent, go_to):
        if self.health <= 0:
            opponent.Coins += self.coinsOnDeath
            print(f"Syris: Lucky you, here are some coins (+{self.coinsOnDeath} coins)")
            print("=" * 25)
            go_to()


class Skeleton(Mob):

    def __init__(self, name, level, max_health, health, coins_on_death, mana):
        super().__init__(name, level, max_health, health, coins_on_death, mana)
        self.name = "Skeleton"
        self.Moves = [
            moves["Eagle's sweep"], moves["Slash"], moves["Small heal"]
        ]
