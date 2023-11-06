moves = {}


class AttackingMove:
    def __init__(self, name, damage, miss_chance, crit_chance):
        self.Name = name
        self.Damage = damage
        self.missChance = miss_chance
        self.critChance = crit_chance


class RangedMove(AttackingMove):
    def __init__(self, name, damage, miss_chance, crit_chance, projectile_amount):
        super().__init__(name, damage, miss_chance, crit_chance)
        self.ProjectileAmount = projectile_amount
        self.missChance *= 0.5  # Less likely to do a crit but more likely to hit
        self.critChance *= 0.5


class PhysicalMove(AttackingMove):
    def __init__(self, name, damage, miss_chance, crit_chance):
        super().__init__(name, damage, miss_chance, crit_chance)
        self.missChance *= 1.5  # More likely to do a crit but less likely to hit
        self.critChance *= 1.5


class HealingMove:
    def __init__(self, name, health_healed):
        self.Name = name
        self.healthHealed = health_healed


class StatMove:
    def __init__(self, name, reduction):
        self.Name = name
        self.Reduction = reduction


# HEALTH MOVES (name, health healed)
moves["Small Heal"] = HealingMove("Small Heal", 40)
moves["Medium Heal"] = HealingMove("Medium Heal", 120)
moves["Big Heal"] = HealingMove("Big Heal", 400)

# STAT MOVES (name, damage reduction as a percentage)
moves["Damage Reduction"] = StatMove("Damage Reduction", 0.8)

# RANGED MOVES (name, damage, miss chance, crit chance, projectile amount)
moves["Flaming Cryo Blast"] = RangedMove("Flaming Cryo Blast", 40, 3, 4, 2)
moves["Omega Beam"] = RangedMove("Omega Beam", 80, 12, 2, 1)
moves["Spitting Firecrackers"] = RangedMove("Spitting Firecrackers", 30, 8, 4, 3)
moves["Bubble Blast"] = RangedMove("Bubble Blast", 5, 2, 2, 12)
moves["Zeus' Blessings"] = RangedMove("Zeus' Blessings", 40, 6, 4, 1)

# PHYSICAL MOVES (name, damage, miss chance, crit chance)
moves["Brawler's Breakout"] = PhysicalMove("Brawler's Breakout", 65, 8, 6)
moves["Earthforce"] = PhysicalMove("Earthforce", 70, 9, 6)
moves["EMP Slam"] = PhysicalMove("EMP Slam", 55, 6, 7)
moves["Zirconium Punch"] = PhysicalMove("Zirconium punch", 45, 4, 5)
moves["Bite"] = PhysicalMove("Bite", 30, 2, 4)
moves["Bird's Vision"] = PhysicalMove("Bird's Vision", 80, 7, 8)    # Acquired at a high level (top 3 move OP moves)
