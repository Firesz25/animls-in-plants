import tkinter as tk
import entities.entities as ent
from entities.entities import Entities


class World:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.root = tk.Tk(className="Animals In Plants")
        self.root.title = "Animals In Plants"
        self.canvas = tk.Canvas(self.root, width=width * 20, height=height * 20)
        self.canvas.pack()
        self.organisms = [[None] * width for _ in range(height)]

    def addentity(self, organism, x, y):  # dodaj organizm
        self.organisms[x][y] = organism

    def removeentity(self, x, y):  # usuń organizm
        self.organisms[x][y] = None

    def draw_world(self):
        for y in range(self.height):
            for x in range(self.width):
                organism = self.organisms[y][x]
                if organism:
                    if isinstance(organism, ent.Animal):
                        fill = ent.color_animals[organism.animalid - 1]
                    else:
                        fill = ent.color_weed[organism.weedid - 1]
                    self.canvas.create_rectangle(
                        x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill=fill
                    )

    def update_world(self):
        for y in range(self.height):
            for x in range(self.width):
                organism = self.organisms[y][x]

    def start(self):  # start
        self.draw_world()
        self.root.after(1000, self.step)
        self.root.mainloop()

    def step(self):  # następna tura
        self.update_world()
        self.root.after(1000, self.step)
