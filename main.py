import dearpygui.dearpygui as dpg

dpg.create_context()
W, H = 600, 200

def d(se):
    print(dpg.get_value(se))


choice = ["Mass, Gravity And Weight", "Gravitational Potential Energy", "Distance Velocity Time"]
len_str = []
for i in choice:
    len_str.append(len(i))
Longer_str = max(len_str)
print(Longer_str)

with dpg.window(label="Menu", tag="Menu"): 
    dpg.add_combo(choice, default_value="Choice", pos=[(W / 2 ) - (Longer_str * 5), 10], width=Longer_str * 10, callback=d)
    
dpg.create_viewport(title='Menu', width=W, height=H)
dpg.set_viewport_min_width(80)
dpg.set_viewport_min_height(80)
dpg.set_viewport_always_top(True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Menu", True)
dpg.start_dearpygui()
dpg.destroy_context()