# Spell Creator for Tibia 13.xx

This Python script creates a graphical user interface (GUI) using Tkinter for selecting and saving grid configurations. The grids represent combat areas for a game, and the user can toggle cells on/off to define the area. The script also allows saving multiple grid configurations with associated parameters.

## Requirements
- Python
- Tkinter (usually comes pre-installed with Python)

## Usage

1. Run the script `creator.py`.
2. The GUI window will open displaying a 15x15 grid.
3. Toggle cells on/off by clicking on them to define the combat area.
4. Use the slider to navigate between different grid configurations.
5. Select desired effect and type from the dropdown menus.
6. Click the "<" or ">" buttons to move the slider.
7. Click the "Save Grid" button to save the current grid configuration.
8. The saved configurations will be written to `"spell_name".lua`.

## `.lua` Format

- **Spell Properties:** The user is prompted to enter the spell name, words, and ID via a dialog window.
- **Grid Configurations:** Each grid configuration consists of a combat area defined by the toggled cells, along with associated effect and type parameters.
- **Additional Functions:** Core functions required for spell casting and combat execution are included.
- **Spell Properties Definition:** The spell properties entered by the user are defined in Lua format.

## `save_grid()` Function

The `save_grid()` function is responsible for writing the grid configurations and associated parameters to a file. It includes a GUI for inputting spell properties such as name, words, and ID, and then writes the configurations to `"spell_name".lua`.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or create a pull request.
