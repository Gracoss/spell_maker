import tkinter as tk
from tkinter import simpledialog
import re

def save_grid(grid_states, grid_params, create_combat_area):
    # Function to handle the GUI for inputting spell properties
    def get_spell_properties():
        spell_name = simpledialog.askstring("Spell Name", "Enter spell name:")
        spell_name = re.sub(r'[^\w\-_\. ]', '_', spell_name)  # Remove invalid characters
        spell_words = simpledialog.askstring("Spell Words", "Enter spell words:")
        spell_id = int(simpledialog.askstring("Spell ID", "Enter spell ID:"))

        # Create a Tkinter window for the GUI
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Create a Toplevel window for the dialog
        dialog = tk.Toplevel(root)
        dialog.title("Select Vocations")

        # Create a label
        label = tk.Label(dialog, text="Select up to 8 vocations:")
        label.pack()

        # Create a Listbox to display available vocations
        vocation_options = ["Druid", "Elder Druid", "Knight", "Elite Knight", "Sorcerer", "Master Sorcerer", "Paladin", "Royal Paladin"]
        selected_vocations = tk.Listbox(dialog, selectmode=tk.MULTIPLE, height=len(vocation_options))
        for vocation in vocation_options:
            selected_vocations.insert(tk.END, vocation)
        selected_vocations.pack()

        # Create a button to confirm selection
        def on_ok():
            nonlocal selected_vocations
            selected_indices = selected_vocations.curselection()
            selected_vocations = [vocation_options[int(i)] for i in selected_indices]
            dialog.destroy()

        confirm_button = tk.Button(dialog, text="OK", command=on_ok)
        confirm_button.pack()

        # Wait for the dialog to be closed
        dialog.wait_window()

        #  Convert the selected vocations to lowercase
        selected_vocations = [vocation.lower() for vocation in selected_vocations]

        # Return all the gathered spell properties
        return spell_name, spell_words, spell_id, selected_vocations

    # Call the function to get spell properties through GUI
    spell_name, spell_words, spell_id, spell_vocations = get_spell_properties()
    filename = f"{spell_name}.lua"

    with open(filename, "w") as file:
        # Write the variables
        file.write("-- SpellCreator generated.\n")
        file.write(f"local baseDamage = xxxx --Base Damage of the Spell\n")
        file.write(f"local levelMult = xxxx --Multiplier for the level\n")
        file.write(f"local magiclvlMult = xxxx --Multiplier for Magic Level\n")
        file.write(f"local offset = xxxx --This adds randomness to the formula. NO RNG = 1\n\n")

        for slider_value, grid in grid_states.items():
            grid_name = f"combat{slider_value + 1}_Brush"
            effect = grid_params[slider_value]["effect"]
            type_ = grid_params[slider_value]["type"]
            area_representation = create_combat_area(grid)
            file.write(f"local {grid_name} = Combat()\n")
            file.write(f"{grid_name}:setParameter(COMBAT_PARAM_EFFECT, {effect})\n")
            file.write(f"{grid_name}:setParameter(COMBAT_PARAM_TYPE, {type_})\n")
            file.write(f"{grid_name}:setArea({area_representation})\n\n")

            # Additional code for getDmg_Brush
            file.write(f"function getDmg_{grid_name}(cid, level, maglevel)\n")
            file.write(f"\treturn baseDamage + math.pow(level, levelMult) + math.pow(maglevel, magiclvlMult) + math.random(level + offset)\n")
            file.write(f"end\n")
            file.write(f"{grid_name}:setCallback(CALLBACK_PARAM_LEVELMAGICVALUE, \"getDmg_{grid_name}\")\n\n")

        # Additional core functions
        file.write("-- =============== CORE FUNCTIONS ===============\n")
        file.write("local function RunPart(c,cid,var,dirList,dirEmitPos) -- Part\n")
        file.write("\tif (Creature(cid):isCreature(cid)) then\n")
        file.write("\t\tc:execute(cid, var)\n")
        file.write("\t\tif (dirList ~= nil) then -- Emit distance effects\n")
        file.write("\t\t\tlocal i = 2;\n")
        file.write("\t\t\twhile (i < #dirList) do\n")
        file.write("\t\t\t\tdirEmitPos:sendDistanceEffect({x=dirEmitPos.x-dirList[i],y=dirEmitPos.y-dirList[i+1],z=dirEmitPos.z},dirList[1])\n")
        file.write("\t\t\t\ti = i + 2\n")
        file.write("\t\t\tend\n")    
        file.write("\t\tend\n")    
        file.write("end\n\n")    

        file.write("local spell = Spell(\"instant\")\n\n")
        file.write("function spell.onCastSpell(creature, var)\n")
        file.write("\tlocal startPos = creature:getPosition(cid)\n")
        file.write("\tlocal creatureId = creature:getId()\n")
        # Determine the number of combat brushes created
        num_combat_brushes = len(grid_states)

        for slider_value in range(num_combat_brushes, 0, -1):
            grid_name = f"combat{slider_value}_Brush"
            if slider_value == num_combat_brushes:
                file.write(f"\tRunPart({grid_name}, creatureId, var, startPos)\n")
            else:
                file.write(f"\taddEvent(RunPart, 100 * {slider_value}, {grid_name}, creatureId, var, startPos)\n")

        file.write("\treturn true\n")
        file.write("end\n")

        # Write spell properties
        file.write("\n-- Spell properties\n")
        file.write(f'spell:group("attack", "focus")\n')
        file.write(f'spell:id({spell_id})\n')
        file.write(f'spell:name("{spell_name}")\n')
        file.write(f'spell:words("{spell_words}")\n')
        file.write(f'spell:level(1000)\n')
        file.write(f'spell:mana(100)\n')
        file.write(f'spell:isPremium(true)\n')
        file.write(f'spell:isSelfTarget(false)\n')
        file.write(f'spell:cooldown(1)\n')
        file.write(f'spell:groupCooldown(1)\n')
        file.write(f'spell:needLearn(false)\n')
        vocation_str = ', '.join(f'"{v.strip()};true"' for v in spell_vocations)
        file.write(f'spell:vocation({vocation_str})\n')
        file.write(f'spell:register()\n')

    print(f"All grids saved to {filename}")

root = tk