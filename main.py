import dearpygui.dearpygui as dpg
import Equation

dpg.create_context()
W, H = 600, 200

""" (|----------------------------------------------------|)"""
choice = []
len_str = []

with open("Equation.py", "r", encoding="utf-8") as file:
    content = file.readlines()

for Check_name_func in content:  # Создаеть список со всеми функциями в файле "Equation.py"
    if "def" in Check_name_func:
        x = ""
        for m in Check_name_func.split("(")[0].split(" ")[1].replace("_", " "):
            x += m
        choice.append(x)
    else: 
        continue 

for i in choice: # Создаеть список где хранятся количество букв в каждом предложении в другом списке
    len_str.append(len(i))
Longer_str = max(len_str) # Находится самое большое число то есть самое большое слово и сколько в нём букв | если длиннейшее слово это "hello" то в списке будеть 5

del len_str # Не нужон 
""" (|----------------------------------------------------|)"""


with dpg.window(label="Menu", tag="Menu"): 
    dpg.add_combo(choice, default_value="Choice", pos=[(W / 2) - (Longer_str * 4), 10], width=Longer_str * 8)
     
    
dpg.create_viewport(title='Menu', width=W, height=H)
dpg.set_viewport_min_width(80)
dpg.set_viewport_min_height(80)
dpg.set_viewport_always_top(True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Menu", True)
dpg.start_dearpygui()
dpg.destroy_context()