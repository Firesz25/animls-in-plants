import entities.entities as ent
from world.world import World
import random

if __name__ == "__main__":
    world = World(width=20, height=20)

    animals = [
        ("wolf", 9, 5, 1, "red"),
        ("sheep", 2, 4, 2, "pink"),
        ("fox", 3, 7, 3, "orange"),
        ("snake",2, 3, 4, "yellow"),
        ("Horse", 5, 5, 5, "brown"),
        ("Hamster", 1, 2, 6, "black")
    ]

    for _ in range(10):
        x = random.randint(0, world.width - 1)
        y = random.randint(0, world.height - 1)
        animal_data = random.choice(animals)
        animal = ent.Animal(*animal_data, world)
        world.addentity(animal, x, y)

    for _ in range(5):
        x = random.randint(0, world.width - 1)
        y = random.randint(0, world.height - 1)
        weed = ent.Weed("weed", 0, 0, 1, "green", world)
        world.addentity(weed, x, y)

    world.start()
