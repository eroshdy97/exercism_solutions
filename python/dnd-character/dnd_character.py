import random
import math
class Character:
    def __init__(self):
        self.strength = [random.randint(1, 6) for i in range(4)]
        self.strength = sum(self.strength) - min(self.strength)

        self.dexterity = [random.randint(1, 6) for i in range(4)]
        self.dexterity = sum(self.dexterity) - min(self.dexterity)

        self.constitution = [random.randint(1, 6) for i in range(4)]
        self.constitution = sum(self.constitution) - min(self.constitution)

        self.intelligence = [random.randint(1, 6) for i in range(4)]
        self.intelligence = sum(self.intelligence) - min(self.intelligence)

        self.wisdom = [random.randint(1, 6) for i in range(4)]
        self.wisdom = sum(self.wisdom) - min(self.wisdom)

        self.charisma = [random.randint(1, 6) for i in range(4)]
        self.charisma = sum(self.charisma) - min(self.charisma)

        self.constitution_modifier = math.floor((self.constitution - 10 ) / 2)
        self.hitpoints = 10 + self.constitution_modifier

    def ability(self):
        return self.charisma

def modifier(x):
    return math.floor((x - 10 ) / 2)