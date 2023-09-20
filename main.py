from entities import entities as ent
from world.world import World
import random

if __name__ == "__main__":
    world = World()

    # Dodaj zwierzęta i rośliny do świata
    for _ in range(10):
        x = random.randint(0, world.width - 1)
        y = random.randint(0, world.height - 1)
        animal = ent.Animal(world, x, y, animalid=1)
        world.addentity(animal, x, y)

    for _ in range(5):
        x = random.randint(0, world.width - 1)
        y = random.randint(0, world.height - 1)
        weed = ent.Weed(world, x, y, weedid=1)
        world.addentity(weed, x, y)

    world.start()
