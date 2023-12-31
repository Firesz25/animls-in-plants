import tkinter as tk


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
        self.turn = 0


        self.draw_legend()


        self.next_turn_button = tk.Button(self.root, text="Następna tura", command=self.next_turn)
        self.next_turn_button.pack()

        self.add_footer()

    def add_footer(self):
        footer_label = tk.Label(self.root, text="Tomasz Ciurkowski, Aleksander Czerny, Bartosz Urbański", font=("Helvetica", 12))
        footer_label.pack(side=tk.BOTTOM)

    def draw_legend(self):
        legend_frame = tk.Frame(self.root)
        legend_frame.pack(side=tk.LEFT)

        legend_label = tk.Label(legend_frame, text="Legenda:")
        legend_label.pack()

        legend_entries = [
            ("Wilk", "red"),
            ("Owca", "pink"),
            ("Lis - Dobry węch: lis nigdy nie ruszy się na pole zajmowane przez organizm silniejszy niż on", "orange"),
            ("Wąż - Ginie przy kolizji z silniejszym przeciwnikiem, ale zatruwa i zabija swojego pogromcę", "yellow"),
            ("Koń - Zasięg ruchu wynosi 2 pola. 50% szans na ucieczkę przed walką. Wówczas przesuwa się na niezajęte sąsiednie pole.", "brown"),
            ("Chomik", "black"),
            ("roślina - ma 30% szans na rozprzestrzenienie się", "green"),
            ("Wilcza jagoda - natychmiast zabija zwierzę które je zjadło", "#326236"),
            ("Guarana - dodaje 3 pkt siły", "#32CD32"),
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
            current_organism = self.organisms[y][x]
            target_organism = self.organisms[new_y][new_x]

            if current_organism is not None:  # Dodaj sprawdzenie, czy organizm istnieje
                current_organism.x = new_x
                current_organism.y = new_y

            self.organisms[new_y][new_x] = current_organism
            self.organisms[y][x] = None

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
