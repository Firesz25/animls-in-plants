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
        self.turn = 0  # Dodaj zmienną do śledzenia tury

        # Dodaj legendę
        self.draw_legend()

        # Dodaj przycisk do rozpoczęcia następnej tury
        next_turn_button = tk.Button(self.root, text="Następna tura", command=self.next_turn)
        next_turn_button.pack()

    def draw_legend(self):
        legend_frame = tk.Frame(self.root)
        legend_frame.pack(side=tk.LEFT)

        legend_label = tk.Label(legend_frame, text="Legenda:")
        legend_label.pack()

        legend_entries = [
            ("Wilk", "red"),
            ("Owca", "pink"),
            ("Lis", "orange"),
            ("Wąż", "yellow"),
            ("Koń", "brown"),
            ("Chomik", "black"),
            ("Roślina", "green"),
        ]

        for name, color in legend_entries:
            legend_item = tk.Frame(legend_frame)
            legend_item.pack(anchor=tk.W)
            legend_color = tk.Label(legend_item, text="   ", bg=color, width=2)
            legend_color.pack(side=tk.LEFT)
            legend_name = tk.Label(legend_item, text=name)
            legend_name.pack(side=tk.LEFT)

    def addentity(self, organism, x, y):
        organism.x = x
        organism.y = y
        self.organisms[y][x] = organism

    def removeentity(self, x, y):
        self.organisms[y][x] = None

    def draw_world(self):
        self.canvas.delete("all")
        for y in range(self.height):
            for x in range(self.width):
                organism = self.organisms[y][x]
                if organism:
                    fill = organism.color
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

    def start(self):
        self.draw_world()
        self.root.mainloop()

    def next_turn(self):
        self.turn += 1
        self.step()

    def step(self):
        organisms_list = []
        for y in range(self.height):
            for x in range(self.width):
                organism = self.organisms[y][x]
                if organism:
                    organisms_list.append(organism)
        organisms_list.sort(key=lambda org: (-org.initiation, -org.age))

        for organism in organisms_list:
            organism.move()
            organism.action()

        self.update_world()
        self.draw_world()

if __name__ == "__main__":
    world = World(20, 20)
    world.start()
