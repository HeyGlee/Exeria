import Lib.move_lib as moves  # gets all the moves

move_list = {"Small heal": moves.HealthMove("Small heal", 20, "Healing", 30),  # Healing moves
             "Medium heal": moves.HealthMove("Medium heal", 39, "Healing", 60),
             "Big heal": moves.HealthMove("Big heal", 50, "Healing", 120),
             "Massive heal": moves.HealthMove("Massive heal", 70, "Healing", 300),
             "Half heal": moves.HealthMove("Half heal", 50, "Healing", 120),
             "Full heal": moves.HealthMove("Full heal", 100, "Healing", 240),
             "Eagle's sweep": moves.RangedAttack("Eagle's sweep", 40, "RAtk", 45, 5, 6, 0, 1),  # Ranged moves
             "Thunderbolt": moves.RangedAttack("Thunderbolt", 40, "RAtk", 45, 5, 6, 0, 1),
             "Icy wind": moves.RangedAttack("Icy wind", 35, "RAtk", 10, 5, 6, 0, 6),
             "Water beam": moves.RangedAttack("Water beam", 45, "RAtk", 45, 5, 6, 0, 1),
             "Hailing bows": moves.RangedAttack("Hailing bows", 35, "RAtk", 15, 5, 6, 0, 3),
             "Spiriblow ghast": moves.RangedAttack("Spiriblow ghast", 30, "RAtk", 25, 5, 6, 0, 2),
             "Lashing fireballs": moves.RangedAttack("Lashing fireballs", 32, "RAtk", 20, 5, 6, 0, 3),
             "Vacuum absorbant": moves.RangedAttack("Vacuum absorbant", 50, "RAtk", 50, 5, 6, 0, 1),
             "Pylon's reach": moves.RangedAttack("Pylon's reach", 25, "RAtk", 40, 5, 6, 0, 1),
             "Cultivated earth": moves.RangedAttack("Cultivated earth", 42, "RAtk", 55, 5, 6, 0, 1),
             "Continental collapse": moves.RangedAttack("Continental collapse", 60, "RAtk", 70, 5, 6, 0, 1),
             "Gust": moves.RangedAttack("Gust", 15, "RAtk", 35, 5, 6, 0, 1),
             "Finishing blow": moves.MeleeAttack("Finishing blow", 60, "MAtk", 70, 8, 3, 0, 1),  # Melee moves
             "Star-strike blitz": moves.MeleeAttack("Star-strike blitz", 40, "MAtk", 25, 8, 3, 0, 5), 
             "Inferno overdrive": moves.MeleeAttack("Inferno overdrive", 55, "MAtk", 65, 8, 3, 0, 1),
             "Inhaled launch": moves.MeleeAttack("Inhaled launch", 40, "MAtk", 55, 8, 3, 0, 1),
             "Super plummet": moves.MeleeAttack("Super plummet", 65, "MAtk", 80, 8, 3, 0, 1),
             "Plummet": moves.MeleeAttack("Plummet", 42, "MAtk", 52, 8, 3, 0, 1),
             "Slash": moves.MeleeAttack("Slash", 45, "MAtk", 50, 8, 3, 0, 1),
             "Super slash": moves.MeleeAttack("Super slash", 60, "MAtk", 65, 8, 3, 0, 1),
             "Aqua dash": moves.MeleeAttack("Aqua dash", 35, "MAtk", 45, 8, 3, 0, 1),
             "Flying peck": moves.MeleeAttack("Flying peck", 30, "MAtk", 40, 8, 3, 0, 1),
             "Bite": moves.MeleeAttack("Bite", 25, "MAtk", 35, 8, 3, 0, 1),
             "Attack reduce big": moves.StatMove("Attack reduce big", 50, "Stat", 0.7, "Attack"),   # Stat moves
             "Attack reduce small": moves.StatMove("Attack reduce small", 35, "Stat", 0.9, "Attack"),
             "Defense reduce big": moves.StatMove("Defense reduce big", 50, "Stat", 0.7, "Defense"),
             "Defense reduce small": moves.StatMove("Defense reduce small", 35, "Stat", 0.9, "Defense"),
             "Attack increase big": moves.StatMove("Attack increase big", 55, "Stat", 1.4, "Attack"),
             "Attack increase small": moves.StatMove("Attack increase small", 45, "Stat", 1.2, "Attack"),
             "Defense increase big": moves.StatMove("Defense increase big", 55, "Stat", 1.4, "Defense"),
             "Defense increase small": moves.StatMove("Defense increase small", 40, "Stat", 1.2, "Defense")}
