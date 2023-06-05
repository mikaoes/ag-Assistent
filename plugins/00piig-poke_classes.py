import random

class pikachu:
     def __init__(self, spieler_level) -> None:
        self.level = int(random.randint(1, 10) * (spieler_level/10))-1
        self.kp = 