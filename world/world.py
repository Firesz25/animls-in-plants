import tkinter as tk
import entities.entities as ent


class World:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width * 20, height=height * 20)
        self.canvas.pack()
        self.organisms = [[None for _ in range(width)] for _ in range(height)]

    def addentity(self, organism, x, y):  # dodaj organizm
        self.organisms[x][y] = organism

    def removeentity(self, x, y):  # usuń organizm
        self.organisms[x][y] = None

    def draw_world(self):
        self.canvas.delete("all")
        for y in range(self.height):
            for x in range(self.width):
                organism = self.organisms[y][x]
                if organism:
                    self.canvas.create_rectangle(
                        x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green"
                    )

    def start(self):  # start
        self.root.after(1000, self.step)
        self.root.mainloop()

    def step(self):  # następna tura
        self.draw_world()
        self.root.after(1000, self.step)
