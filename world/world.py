import tkinter as tk
import entities.entities as ent


class World:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.root = tk.Tk(className="Animals In Plants")
        self.root.title("Animals In Plants")
        self.canvas = tk.Canvas(self.root, width=width * 20, height=height * 20)
        self.canvas.pack()
        self.organisms = [[None] * width for _ in range(height)]
        self.world = self 

    def addentity(self, organism, x, y):  # dodaj organizm
        organism.x = x
        organism.y = y
        self.organisms[y][x] = organism

    def removeentity(self, x, y):  # usuń organizm
        self.organisms[x][y] = None

    def draw_world(self):
        self.canvas.delete("all")
        for y in range(self.height):
            for x in range(self.width):
                organism = self.organisms[y][x]
                if organism:
                    fill = organism.color  # Ustaw kolor na podstawie pola koloru organizmu
                    self.canvas.create_rectangle(
                        x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill=fill
                    )


    def move_organism(self, x, y, new_x, new_y):
        if new_x >= 0 and new_x < self.width and new_y >= 0 and new_y < self.height:
            if not self.organisms[new_y][new_x]:
                self.organisms[new_y][new_x] = self.organisms[y][x]
                self.organisms[y][x] = None
                self.organisms[new_y][new_x].x = new_x
                self.organisms[new_y][new_x].y = new_y


    def update_world(self):
        for y in range(self.height):
            for x in range(self.width):
                organism = self.organisms[y][x]
                if organism:
                    organism.age += 1

    def start(self):  # start
        self.draw_world()
        self.root.after(1000, self.step)
        self.root.mainloop()

    def step(self):
    # Sortowanie organizmów według inicjatywy (najwyższa inicjatywa pierwsza)
        organisms_list = []
        for y in range(self.height):
            for x in range(self.width):
                organism = self.organisms[y][x]
                if organism:
                    organisms_list.append(organism)
        organisms_list.sort(key=lambda org: (-org.initiation, -org.age))

        # Wykonaj akcje organizmów w kolejności
        for organism in organisms_list:
            organism.move() # Przekazujemy obiekt 'world' jako argument
            organism.action()

        self.update_world()
        self.draw_world()
        self.root.after(1000, self.step)
