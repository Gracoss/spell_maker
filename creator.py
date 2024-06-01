import tkinter as tk
from tkinter import ttk
from script import save_grid

class GridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("15x15 Grid Selector")
        
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()

        self.grid_size = 15
        self.grid_data = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.center_cell = (self.grid_size // 2, self.grid_size // 2)
        self.grid_data[self.center_cell[0]][self.center_cell[1]] = 2
        self.grid_states = {}  # Dictionary to save grid states based on slider value
        self.grid_params = {}  # Dictionary to save parameters for each grid state
        self.current_slider_value = 0

        self.buttons = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.create_grid()

        self.slider_label = tk.Label(root, text="Slider value: 0")
        self.slider_label.pack()

        self.effect_label = tk.Label(root, text="Select Effect:")
        self.effect_label.pack()
        self.effect_options = ["CONST_ME_DRAWBLOOD", "CONST_ME_LOSEENERGY", "CONST_ME_POFF", "CONST_ME_BLOCKHIT", "CONST_ME_EXPLOSIONAREA", "CONST_ME_EXPLOSIONHIT", "CONST_ME_FIREAREA", "CONST_ME_YELLOW_RINGS", "CONST_ME_GREEN_RINGS", "CONST_ME_HITAREA", "CONST_ME_TELEPORT", "CONST_ME_ENERGYHIT", "CONST_ME_MAGIC_BLUE", "CONST_ME_MAGIC_RED", "CONST_ME_MAGIC_GREEN", "CONST_ME_HITBYFIRE", "CONST_ME_HITBYPOISON", "CONST_ME_MORTAREA", "CONST_ME_SOUND_GREEN", "CONST_ME_SOUND_RED", "CONST_ME_POISONAREA", "CONST_ME_SOUND_YELLOW", "CONST_ME_SOUND_PURPLE", "CONST_ME_SOUND_BLUE", "CONST_ME_SOUND_WHITE", "CONST_ME_BUBBLES", "CONST_ME_CRAPS", "CONST_ME_GIFT_WRAPS", "CONST_ME_FIREWORK_YELLOW", "CONST_ME_FIREWORK_RED", "CONST_ME_FIREWORK_BLUE", "CONST_ME_STUN", "CONST_ME_SLEEP", "CONST_ME_WATERCREATURE", "CONST_ME_GROUNDSHAKER", "CONST_ME_HEARTS", "CONST_ME_FIREATTACK", "CONST_ME_ENERGYAREA", "CONST_ME_SMALLCLOUDS", "CONST_ME_HOLYDAMAGE", "CONST_ME_BIGCLOUDS", "CONST_ME_ICEAREA", "CONST_ME_ICETORNADO", "CONST_ME_ICEATTACK", "CONST_ME_STONES", "CONST_ME_SMALLPLANTS", "CONST_ME_CARNIPHILA", "CONST_ME_PURPLEENERGY", "CONST_ME_YELLOWENERGY", "CONST_ME_HOLYAREA", "CONST_ME_BIGPLANTS", "CONST_ME_CAKE", "CONST_ME_GIANTICE", "CONST_ME_WATERSPLASH", "CONST_ME_PLANTATTACK", "CONST_ME_TUTORIALARROW", "CONST_ME_TUTORIALSQUARE", "CONST_ME_MIRRORHORIZONTAL", "CONST_ME_MIRRORVERTICAL", "CONST_ME_SKULLHORIZONTAL", "CONST_ME_SKULLVERTICAL", "CONST_ME_ASSASSIN", "CONST_ME_STEPSHORIZONTAL", "CONST_ME_BLOODYSTEPS", "CONST_ME_STEPSVERTICAL", "CONST_ME_YALAHARIGHOST", "CONST_ME_BATS", "CONST_ME_SMOKE", "CONST_ME_INSECTS", "CONST_ME_DRAGONHEAD", "CONST_ME_ORCSHAMAN", "CONST_ME_ORCSHAMAN_FIRE", "CONST_ME_THUNDER", "CONST_ME_FERUMBRAS", "CONST_ME_CONFETTI_HORIZONTAL", "CONST_ME_CONFETTI_VERTICAL"]
        self.effect_var = tk.StringVar(value=self.effect_options[0])
        self.effect_dropdown = ttk.Combobox(root, textvariable=self.effect_var, values=self.effect_options)
        self.effect_dropdown.pack()

        self.type_label = tk.Label(root, text="Select Type:")
        self.type_label.pack()
        self.type_options = ["COMBAT_PHYSICALDAMAGE", "COMBAT_ENERGYDAMAGE", "COMBAT_EARTHDAMAGE", "COMBAT_FIREDAMAGE", "COMBAT_LIFEDRAIN", "COMBAT_HEALING", "COMBAT_DROWNDAMAGE", "COMBAT_ICEDAMAGE", "COMBAT_HOLYDAMAGE", "COMBAT_DEATHDAMAGE", "COMBAT_MANADRAIN", "COMBAT_AGONYDAMAGE", "COMBAT_NEUTRALDAMAGE"]
        self.type_var = tk.StringVar(value=self.type_options[0])
        self.type_dropdown = ttk.Combobox(root, textvariable=self.type_var, values=self.type_options)
        self.type_dropdown.pack()

        self.prev_button = tk.Button(root, text="<", command=lambda: self.move_slider(-1))
        self.prev_button.pack(side="left", padx=(20, 10))

        self.next_button = tk.Button(root, text=">", command=lambda: self.move_slider(1))
        self.next_button.pack(side="right", padx=(10, 20))

        self.save_button = tk.Button(root, text="Save Grid", command=self.save_grid)
        self.save_button.pack()

    def create_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) == self.center_cell:
                    color = "red"
                else:
                    color = "SystemButtonFace"
                button = tk.Button(self.grid_frame, width=3, height=1, bg=color, command=lambda i=i, j=j: self.toggle_cell(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def toggle_cell(self, i, j):
        if (i, j) != self.center_cell:
            if self.grid_data[i][j] == 0:
                self.grid_data[i][j] = 1
                self.buttons[i][j].config(bg="blue")
            else:
                self.grid_data[i][j] = 0
                self.buttons[i][j].config(bg="SystemButtonFace")

    def move_slider(self, direction):
        new_value = self.current_slider_value + direction
        if 0 <= new_value <= 100:
            self.slider_update(new_value)

    def slider_update(self, slider_value):
        self.slider_label.config(text=f"Slider value: {slider_value}")
    
    # Save the current grid state and parameters
        self.grid_states[self.current_slider_value] = [row[:] for row in self.grid_data]
        self.grid_params[self.current_slider_value] = {
            "effect": self.effect_var.get(),
            "type": self.type_var.get()
        }

    # Clear the grid
        self.clear_grid()

    # Load the new grid state and parameters if they exist, else create a new empty grid
        if slider_value in self.grid_states:
            self.grid_data = [row[:] for row in self.grid_states[slider_value]]
            self.effect_var.set(self.grid_params[slider_value]["effect"])
            self.type_var.set(self.grid_params[slider_value]["type"])
        else:
            self.grid_data = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
            self.effect_var.set(self.effect_options[0])
            self.type_var.set(self.type_options[0])

    # Ensure the center cell is always 2
        self.grid_data[self.center_cell[0]][self.center_cell[1]] = 2

        self.update_grid_display()
        self.current_slider_value = slider_value

    def clear_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) == self.center_cell:
                    color = "red"
                else:
                    color = "SystemButtonFace"
                self.buttons[i][j].config(bg=color)

    def update_grid_display(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid_data[i][j] == 1:
                    self.buttons[i][j].config(bg="blue")

    def save_grid(self):
        save_grid(self.grid_states, self.grid_params, self.create_combat_area)

    def create_combat_area(self, grid):
        # Ensure the center cell is always active and set to 2
        grid[self.center_cell[0]][self.center_cell[1]] = 2
        
        # Find the bounding box that includes the center cell
        min_row, max_row, min_col, max_col = self.find_bounding_box(grid)
        
        # Create the area representation
        area_representation = "createCombatArea({\n"
        for i in range(min_row, max_row + 1):
            row_representation = "{" + ", ".join(str(grid[i][j]) for j in range(min_col, max_col + 1)) + "}"
            area_representation += row_representation + ",\n"
        area_representation = area_representation.rstrip(",\n") + "\n})"
        
        return area_representation

    def find_bounding_box(self, grid):
        min_row, max_row = self.grid_size - 1, 0
        min_col, max_col = self.grid_size - 1, 0

        found_active_cell = False
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    found_active_cell = True
                    if i < min_row: min_row = i
                    if i > max_row: max_row = i
                    if j < min_col: min_col = j
                    if j > max_col: max_col = j
        
        if not found_active_cell:
            # Return the center cell if no active cells are found
            return self.center_cell[0], self.center_cell[0], self.center_cell[1], self.center_cell[1]

        return min_row, max_row, min_col, max_col
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)
    root.mainloop()