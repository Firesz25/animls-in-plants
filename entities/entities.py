class Entities:
    _id: int
    _entity: str
    _strength: int
    _iniciation: int

    def __init__(self, entity, strength, iniciation):
        self._entity = entity
        self._strength = strength
        self._iniciation = iniciation

    def move(self):
        pass

    def actiov(self):
        pass


class Weed(Entities):
    weedid: int

    def __init__(self, entity, strength, iniciation, weedid):
        super().__init__(entity, strength, iniciation)
        self.weedid = weedid


class Animal(Entities):
    animalid: int

    def __init__(self, entity, strength, iniciation, animalid):
        super().__init__(entity, strength, iniciation)
        self.animalid = animalid


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
