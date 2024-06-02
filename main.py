import dearpygui.dearpygui as dpg
import Equation
from Qua import *

dpg.create_context()
W, H = 600, 400

""" (|----------------------------------------------------|)"""
choice = {}
len_str = []

with open("Equation.py", "r", encoding="utf-8") as file:
    content = file.readlines()

for Check_name_func in content:
    if "def" in Check_name_func:
        x = ""
        z = 0

        Def_Name, Value = Check_name_func.split("(")
        Value = Value.split("):")[0].split(": float, ")
        Value[-1] = Value[-1].split(": float")[0]

        for m in Def_Name.split(" ")[1].replace("_", " "):
            try:
                z = int(m)
            except ValueError:
                x += m
        choice[x[:-1]] = [z, Value]
    else: 
        continue 

for i in choice: 
    len_str.append(len(i))
Longer_str = max(len_str)

del len_str # Не нужон 
""" (|----------------------------------------------------|)"""

Text = []
def pes():
    Val = []
    Le = choice[dpg.get_value(Tr)][1]
    print(Le, dpg.get_value(Tr))
    for Delete in Text:
         if dpg.does_item_exist(Delete):
           dpg.delete_item(Delete)

    for check in range(len(Le)):
        Val.append(dpg.get_value(Le[check]))
        try:
            Val[check] = int(Val[check])
        except ValueError:
            Val[check] = None
    
    Res = Equation.Mass_Gravity_Weight_3(Val[0], Val[1], Val[2])
    Text.append(Res)
    if type(Res) == str:
        dpg.add_text(f"{Res}", tag=f"{Res}", pos=[(W - len(Res)) / 4,  H / 2], parent="Menu")
    else:
        dpg.add_text(f" {Equation.Mass_Gravity_Weight_3(Val[0], Val[1], Val[2])[0]} - {Equation.Mass_Gravity_Weight_3(Val[0], Val[1], Val[2])[1]}", 
                     tag=f"{Res}", 
                     pos=[(W - len(Equation.Mass_Gravity_Weight_3(Val[0], Val[1], Val[2])[0])) / 4,  H / 2], 
                     parent="Menu")

    

all_types = []
def count(sender):
    global Tr
    Tr = sender
    for Delete in all_types:
         if dpg.does_item_exist(Delete):
           dpg.delete_item(Delete)

    for i in range(choice[dpg.get_value(sender)][0]):
        dpg.add_input_text(label=f"{choice[dpg.get_value(Tr)][1][i]}", tag=f"{choice[dpg.get_value(Tr)][1][i]}", 
                           parent="Menu", default_value="Nothig", decimal=True,
                           pos=[(W / 2) - (Longer_str * 5), 40 + (i * 35)], 
                           width=Longer_str * 8)
        all_types.append(str(choice[dpg.get_value(Tr)][1][i]))

    dpg.add_button(label="Result", tag="Res", parent="Menu", 
                   pos=[W / 2 - (len("Result") * 5), (40 + (i * 35)) + 50], width=len("Result") * 10, 
                   callback=pes)
    all_types.append("Res")

with dpg.window(label="Menu", tag="Menu"): 
    dpg.add_combo(list(choice), default_value="Choice", pos=[(W / 2) - (Longer_str * 5), 10], width=Longer_str * 10, callback=count)
     
    
dpg.create_viewport(title='Menu', width=W, height=H)
dpg.set_viewport_min_width(80)
dpg.set_viewport_min_height(80)
dpg.set_viewport_always_top(True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Menu", True)
dpg.start_dearpygui()
dpg.destroy_context()