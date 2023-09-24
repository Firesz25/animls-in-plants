import random
class Entities:
    _id: int
    _entity: str
    _strength: int
    _initiation: int
    

    def __init__(self, entity, strength, initiation):
        self._entity = entity
        self._strength = strength
        self._iniciation = initiation
        self.x = None
        self.y = None
        self.age = 0
    
    def move(self):
        pass

    def action(self):
        pass

class Weed(Entities):
    weedid: int

    def __init__(self, entity, strength, initiation, weedid):
        super().__init__(entity, strength, initiation)
        self.weedid = weedid
        self.initiation = initiation

    def action(self):
        # Logika działania rośliny
        pass


class Animal(Entities):
    animalid: int

    def __init__(self, entity, strength, initiation, animalid):
        super().__init__(entity, strength, initiation)
        self.animalid = animalid
        self.initiation = initiation  # Dodaj atrybut initiation

    def move(self, world):
        # Organizmy zwierzęce poruszają się na podstawie inicjatywy
        # Im wyższa inicjatywa, tym organizm rusza się wcześniej
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = random.choice(directions)
        new_x, new_y = self.x + dx, self.y + dy

        if 0 <= new_x < world.width and 0 <= new_y < world.height:
            world.move_organism(self.x, self.y, new_x, new_y)


    def action(self):
        # Logika działania zwierzęcia
        pass


wolf = Animal("wolf", 9, 5, 1)
sheep = Animal("sheep", 2, 4, 2)
fox = Animal("fox", 3, 7, 3)
snake = Animal("snake", 6, 3, 4)
horse = Animal("Horse", 5, 5, 5)
hamster = Animal("Hamster", 1, 2, 6)

weed = Weed("weed", 0, 0, 1)
cocaine = Weed("cocaine", 0, 0, 2)
Belladonna = Weed("Belladonna", 0, 0, 3)

color_weed = ["green"]

color_animals = ["red"]
