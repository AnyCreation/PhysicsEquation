import dearpygui.dearpygui as dpg
import Equation as E

dpg.create_context()
W, H = 600, 400

def Font():
    with dpg.font_registry():
            return dpg.add_font("Merich.otf", 15)


EQU = {
"Mass Gravity Weight": lambda One, Two, Three: E.Mass_Gravity_Weight_3(One, Two, Three),

"Gravitational Potential Energy": lambda One, Two, Three: E.Gravitational_Potential_Energy_3(One, Two, Three),

"Gravitational Potential Energy WITH MASS": lambda One, Two, Three, Four: E.Gravitational_Potential_Energy_WITH_MASS_4(One, Two, Three, Four),

"Distance Velocity Time": lambda One, Two, Three: E.Distance_Velocity_Time_3(One, Two, Three),

"Constant Speed": lambda One, Two, Three: E.Constant_Speed_3(One, Two, Three),
}



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
    for Delete in Text:
         if dpg.does_item_exist(Delete):
           dpg.delete_item(Delete)

    for check in range(len(Le)):
        Val.append(dpg.get_value(Le[check]))
        try:
            Val[check] = float(Val[check])
        except ValueError:
            Val[check] = None

    if len(Val) == 3:
        Res = EQU[dpg.get_value(Tr)](Val[0], Val[1], Val[2])
    elif len(Val) == 4:
        Res = EQU[dpg.get_value(Tr)](Val[0], Val[1], Val[2], Val[3])

    Text.append(Res)
    print(Res)
    if type(Res) == str:
        dpg.add_text(f"{Res}", tag=f"{Res}", before=RES, pos=[dpg.get_item_pos(RES)[0] - len(Res), dpg.get_item_pos(RES)[1] - 30],)
    else:
        dpg.set_value(RES, f"{Res[0]} : {Res[1]}")

    

all_types = []
def count(sender):
    global Tr
    Tr = sender
    for Delete in all_types:
         if dpg.does_item_exist(Delete):
           dpg.delete_item(Delete)

    for i in range(choice[dpg.get_value(Tr)][0]):

        dpg.add_input_text(label=f"{choice[dpg.get_value(Tr)][1][i]}", 
                           tag=f"{choice[dpg.get_value(Tr)][1][i]}", 
                           decimal=True, pos=[(W / 2) - (Longer_str * 5), 40 + (i * 35)],  # Pos
                           width=Longer_str * 8,parent="Menu")
        
        all_types.append(str(choice[dpg.get_value(Tr)][1][i]))

with dpg.window(label="Menu", tag="Menu"): 
    dpg.add_combo(list(choice), default_value="Choice", pos=[(W / 2) - (Longer_str * 5), 10], width=Longer_str * 10, callback=count)

    dpg.add_text("*leave blank the field that is unknown", tag="UN", wrap=len("leave") * 16)
    dpg.add_text("----")

    RES = dpg.add_text("Unknow : Quantity", pos=[W / 4 + len("Unknow") * 14, H / 1.5])
    dpg.bind_item_font(RES, Font())
    
    dpg.add_button(label="Result", tag="Res", parent="Menu", 
                   pos=[W / 2 - (len("Result") * 5), (H / 1.5) + 50], width=len("Result") * 10,
                   callback=pes)
     
    
dpg.create_viewport(title='Menu', width=W, height=H)
dpg.set_viewport_min_width(80)
dpg.set_viewport_min_height(80)
dpg.set_viewport_always_top(True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Menu", True)
dpg.start_dearpygui()
dpg.destroy_context()