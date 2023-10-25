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

class Weed(Entities):
    weedid: int

    def __init__(self, entity, strength, initiation, weedid, color, world=None):
        super().__init__(entity, strength, initiation)
        self.weedid = weedid
        self.initiation = initiation
        self.color = color
        self.world = world

    def move(self):
        # Organizm Weed nie porusza się, więc pozostawiamy tę metodę pustą.
        pass

    def action(self):
        # Logika działania rośliny
        pass

class Animal(Entities):
    animalid: int

    def __init__(self, entity, strength, initiation, animalid, color, world=None):
        super().__init__(entity, strength, initiation)
        self.animalid = animalid
        self.initiation = initiation
        self.color = color
        self.world = world

    def move(self):
        if self.world:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            dx, dy = random.choice(directions)
            new_x, new_y = self.x + dx, self.y + dy

            if 0 <= new_x < self.world.width and 0 <= new_y < self.world.height:
                target_organism = self.world.organisms[new_y][new_x]
                if not target_organism:
                    # Jeśli pole jest puste, po prostu przesuń organizm
                    self.world.move_organism(self.x, self.y, new_x, new_y)
                elif self._strength >= target_organism._strength:
                    # Jeśli organizm jest silniejszy, "zjada" organizm na polu docelowym
                    self.world.removeentity(new_x, new_y)
                    self.world.move_organism(self.x, self.y, new_x, new_y)
                else:
                    # Jeśli organizm jest słabszy, to zostaje "zjedzony"
                    self.world.removeentity(self.x, self.y)

    def action(self):
        if self._entity == "fox":
            self.sniff()
        else:
            # Domyślna akcja dla innych zwierząt
            self.move()
    def sniff(self):
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = direction
            new_x, new_y = self.x + dx, self.y + dy

            if (
                    0 <= new_x < self.world.width
                    and 0 <= new_y < self.world.height
                    and self.is_weaker_than_organism(new_x, new_y)
            ):
                self.world.move_organism(self.x, self.y, new_x, new_y)
                return

    def is_weaker_than_organism(self, x, y):
        # Sprawdź, czy organizm na danym polu jest silniejszy
        if (
                self.world.organisms[y][x]
                and self.world.organisms[y][x].strength > self._strength
        ):
            return False
        return True



#wolf = Animal("wolf", 9, 5, 1, "red")
#sheep = Animal("sheep", 2, 4, 2, "blue")
#fox = Animal("fox", 3, 7, 3, "cyan")
#snake = Animal("snake", 6, 3, 4, "yellow")
#horse = Animal("Horse", 5, 5, 5, "magenta")
#hamster = Animal("Hamster", 1, 2, 6, "black")


#weed = Weed("weed", 0, 0, 1, "green")
#cocaine = Weed("cocaine", 0, 0, 2, "green")
#Belladonna = Weed("Belladonna", 0, 0, 3, "green")
