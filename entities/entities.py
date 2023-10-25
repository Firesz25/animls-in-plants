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
        pass

    def action(self):
        if self._entity == "weed":
            if random.random() < 0.03:
                self.spread()
        elif self._entity == "Belladonna":
            self.kill()
        elif self._entity == "guarana":
            self.extrastrength()
        else:
            pass

    def extrastrength(self):
        if self.world and 0 <= self.x < self.world.width and 0 <= self.y < self.world.height:
            target_organism = self.world.organisms[self.y][self.x]
            if isinstance(target_organism, Animal):
                target_organism._strength += 3


    def kill(self):

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = direction
            new_x, new_y = self.x + dx, self.y + dy

            if (
                    0 <= new_x < self.world.width
                    and 0 <= new_y < self.world.height
            ):
                target_organism = self.world.organisms[new_y][new_x]
                if isinstance(target_organism, Animal):

                    self.world.removeentity(target_organism.x, target_organism.y)

                    self.world.removeentity(self.x, self.y)
                    return

    def spread(self):

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy

            if (
                0 <= new_x < self.world.width
                and 0 <= new_y < self.world.height
                and not self.world.organisms[new_y][new_x]
            ):
                new_weed = Weed("weed", 0, 0, self.weedid, self.color, self.world)
                self.world.addentity(new_weed, new_x, new_y)
                return

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

                    self.world.move_organism(self.x, self.y, new_x, new_y)
                elif self._strength >= target_organism._strength:

                    if self._entity != target_organism._entity:
                        self.world.removeentity(new_x, new_y)
                        self.world.move_organism(self.x, self.y, new_x, new_y)
                else:

                    self.world.removeentity(self.x, self.y)
    def action(self):
        if self._entity == "fox":
            self.sniff()
            if self.is_collision():
                if random.random() < 0.5:
                    self.reproduce()
                self.move()
        elif self._entity == "snake":
            self.bite()
            if self.is_collision():
                if random.random() < 0.5:
                    self.reproduce()
                self.move()
        elif self._entity == "Horse":
            self.horse_move()
            if random.random() < 0.5:
                self.escape()
            if self.is_collision():
                if random.random() < 0.5:
                    self.reproduce()
                self.horse_move()
        else:
            if self.is_collision():
                if random.random() < 0.5:
                    self.reproduce()
                self.move()
            self.move()

    def is_collision(self):
        x, y = self.x, self.y
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (
                    0 <= new_x < self.world.width
                    and 0 <= new_y < self.world.height
                    and self.world.organisms[new_y][new_x]
                    and self.world.organisms[new_y][new_x]._entity == self._entity
            ):
                return True
        return False

    def reproduce(self):
        x, y = self.x, self.y
        empty_cells = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (
                    0 <= new_x < self.world.width
                    and 0 <= new_y < self.world.height
                    and not self.world.organisms[new_y][new_x]
            ):
                empty_cells.append((new_x, new_y))

        if empty_cells:
            new_x, new_y = random.choice(empty_cells)
            child = Animal(self._entity, self._strength, self._iniciation, self.animalid, self.color, self.world)
            self.world.addentity(child, new_x, new_y)

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
    def bite(self):
        if self.world:

            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = direction
                new_x, new_y = self.x + dx, self.y + dy

                if (
                        0 <= new_x < self.world.width
                        and 0 <= new_y < self.world.height
                ):
                    target_organism = self.world.organisms[new_y][new_x]
                    if isinstance(target_organism, Animal):

                        if self._strength >= target_organism._strength:

                            self.world.removeentity(new_x, new_y)
                        else:

                            self.world.removeentity(self.x, self.y)
                            self.world.removeentity(new_x, new_y)
                            return
    def horse_move(self):
        if self.world:

            steps = random.randint(1, 2)
            for _ in range(steps):

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                dx, dy = random.choice(directions)
                new_x, new_y = self.x + dx, self.y + dy

                if (
                        0 <= new_x < self.world.width
                        and 0 <= new_y < self.world.height
                ):
                    target_organism = self.world.organisms[new_y][new_x]
                    if not target_organism:
                        self.world.move_organism(self.x, self.y, new_x, new_y)
    def escape(self):

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy

            if (
                0 <= new_x < self.world.width
                and 0 <= new_y < self.world.height
                and not self.world.organisms[new_y][new_x]
            ):
                self.world.move_organism(self.x, self.y, new_x, new_y)
                return
    def is_weaker_than_organism(self, x, y):
        # Sprawdź, czy organizm na danym polu jest silniejszy
        if (
                self.world.organisms[y][x]
                and self.world.organisms[y][x]._strength > self._strength
        ):
            return False
        return True


