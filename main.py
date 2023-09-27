import entities.entities as ent
from world.world import World
import random

if __name__ == "__main__":
    world = World(width=20, height=20)

    # Dodaj zwierzęta i rośliny do świata
    for _ in range(10):
        x = random.randint(0, world.width - 1)
        y = random.randint(0, world.height - 1)
        animal = ent.Animal("wolf", 9, 5, 1, world)  # Przekaz obiekt world
        world.addentity(animal, x, y)

    for _ in range(5):
        x = random.randint(0, world.width - 1)
        y = random.randint(0, world.height - 1)
        weed = ent.Weed("weed", 0, 0, 1, world)  # Przekaz obiekt world
        world.addentity(weed, x, y)

    world.start()

