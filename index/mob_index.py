from lib.entity_lib import Mob as Mob        # Gets the Mob class
from index.move_index import move_list as move_list        # Gets all the moves

mobs = {"skeleton": Mob("Skeleton", 1, 100, 100, 120, 120, 50, 20),
        "zombie": Mob("Zombie", 1, 90, 90, 130, 130, 60, 40), 
        "spider": Mob("Spider", 1, 60, 60, 90, 90, 45, 25),
        "goblin": Mob("Goblin", 1, 80, 80, 100, 100, 35, 30),
        "dragon": Mob("Dragon", 1, 130, 130, 130, 130, 100, 70),
        "wyvern": Mob("Wyvern", 1, 110, 110, 120, 120, 75, 60),
        "imp": Mob("Imp", 1, 40, 40, 130, 130, 25, 25),
        "bulky_skeleton": Mob("Bulky skeleton", 1, 130, 130, 120, 120, 70, 50),
        "bulky_zombie": Mob("Bulky zombie", 1, 120, 120, 130, 130, 80, 90),
        "bulky_spider": Mob("Bulky spider", 1, 90, 90, 90, 90, 65, 55),
        "bulky_goblin": Mob("Bulky goblin", 1, 110, 110, 100, 100, 55, 60),
        "bulky_dragon": Mob("Bulky dragon", 1, 170, 170, 130, 130, 120, 100),
        "bulky_wyvern": Mob("Bulky wyvern", 1, 140, 140, 120, 120, 95, 90),
        "bulky_imp": Mob("Bulky imp", 1, 80, 80, 120, 120, 45, 55),
        "smart_skeleton": Mob("Smart skeleton", 1, 100, 100, 200, 200, 60, 60),
        "smart_zombie": Mob("Smart zombie", 1, 90, 90, 210, 210, 70, 80),
        "smart_spider": Mob("Smart spider", 1, 60, 60, 170, 170, 55, 65),
        "smart_goblin": Mob("Smart goblin", 1, 80, 80, 180, 180, 45, 70),
        "smart_dragon": Mob("Smart dragon", 1, 130, 130, 210, 210, 110, 110),
        "smart_wyvern": Mob("Smart wyvern", 1, 110, 110, 200, 200, 100),
        "smart_imp": Mob("Smart imp", 1, 40, 40, 210, 210, 35, 65)
}

