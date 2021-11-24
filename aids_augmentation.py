# This set of code will allow AIDS to be run in various applications. Copy and paste the code needed to for App.
import AIDS

### tkinter set

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

tkinter_generate_button_all = tk.Button(text = "Generate Any", command = AIDS.generate(AIDS.all()))
tkinter_generate_button_action = tk.Button(text = "Generate Action", command = AIDS.generate(AIDS.kl.action_list))
tkinter_generate_button_creature = tk.Button(text = "Generate Creature", command = AIDS.generate(AIDS.kl.creature_list))
tkinter_generate_button_defeat = tk.Button(text = "Generate Defeat", command = AIDS.generate(AIDS.kl.defeat_list))
tkinter_generate_button_dungeon = tk.Button(text = "Generate Dungeon", command = AIDS.generate(AIDS.kl.dungeon_list))
tkinter_generate_button_goals = tk.Button(text = "Generate Goals", command = AIDS.generate(AIDS.kl.goals_list))
tkinter_generate_button_memetic = tk.Button(text = "Generate Memetic", command = AIDS.generate(AIDS.kl.memetic_list))
tkinter_generate_button_mind_control = tk.Button(text = "Generate Mind Control", command = AIDS.generate(AIDS.kl.mind_control_list))
tkinter_generate_button_transformation = tk.Button(text = "Generate Transformation", command = AIDS.generate(AIDS.kl.transformation_list))
tkinter_generate_button_traps = tk.Button(text = "Generate Traps", command = AIDS.generate(AIDS.kl.traps_list))
tkinter_generate_button_wilds = tk.Button(text = "Generate Wilds", command = AIDS.generate(AIDS.kl.wilds_list))