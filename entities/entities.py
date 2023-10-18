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

    def __init__(self, entity, strength, initiation, weedid, color, world=None):  # Dodaj domyślny argument world=None
        super().__init__(entity, strength, initiation)
        self.weedid = weedid
        self.initiation = initiation
        self.color = color
        self.world = world  # Przypisz world po utworzeniu organizmu
        

    def action(self):
        # Logika działania rośliny
        pass


class Animal(Entities):
    animalid: int

    def __init__(self, entity, strength, initiation, animalid, color, world=None):  # Dodaj domyślny argument world=None
        super().__init__(entity, strength, initiation)
        self.animalid = animalid
        self.initiation = initiation
        self.color = color
        self.world = world  # Przypisz world po utworzeniu organizmu

        
        
    def move(self):
        if self.world:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            dx, dy = random.choice(directions)
            new_x, new_y = self.x + dx, self.y + dy

            if 0 <= new_x < self.world.width and 0 <= new_y < self.world.height:
                self.world.move_organism(self.x, self.y, new_x, new_y)




    def action(self):
        # Logika działania zwierzęcia
        pass


#wolf = Animal("wolf", 9, 5, 1, "red")
#sheep = Animal("sheep", 2, 4, 2, "blue")
#fox = Animal("fox", 3, 7, 3, "cyan")
#snake = Animal("snake", 6, 3, 4, "yellow")
#horse = Animal("Horse", 5, 5, 5, "magenta")
#hamster = Animal("Hamster", 1, 2, 6, "black")


#weed = Weed("weed", 0, 0, 1, "green")
#cocaine = Weed("cocaine", 0, 0, 2, "green")
#Belladonna = Weed("Belladonna", 0, 0, 3, "green")
