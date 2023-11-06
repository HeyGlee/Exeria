from Libraries.moves import moves   # Imports all the moves in the database from the lib

class Entity:
    def __init__(self, max_health, health, name, level):   # this will be the basic stats that every character has
        self.MaxHP = max_health
        self.Health = health
        self.Name = name
        self.Level = level
        self.Alive = True

    def take_damage(self, damage: int) -> None:
        self.Health -= damage
        if self.Health <= 0:
            self.Alive = False

    def heal_health(self, health_amount: int) -> None:
        added_health = self.Health + health_amount
        if added_health > self.MaxHP:
            added_health -= added_health - self.MaxHP
        self.Health = added_health


class Fighter(Entity):
    def __init__(self, max_health, health, name, level):
        super().__init__(max_health, health, name, level)
        self.Moves = []
        self.baseDamage = 1

    def add_move(self, move):
        if move not in moves:
            return  # breaks out of function if wanted move isn't in the moves list
        else:
            self.Moves.append(moves[move])


class Character(Fighter):
    def __init__(self, max_health, health, name, level, xp, coins):
        super().__init__(max_health, health, name, level)
        self.XP = xp
        self.Coins = coins
        self.Location = "Fukuoka Springs"

    def faint(self):
        if not self.Alive:
            self.Coins *= 0.8

    def level_up(self, xp_required: dict):
        if xp_required[self.Level] >= self.XP:
            self.Level += 1



