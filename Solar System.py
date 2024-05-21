import tkinter as tk
from os import path
from customtkinter import *
from PIL import Image  


# set theme 
set_appearance_mode("dark")
set_default_color_theme("blue")

#root = Tk() 
root = CTk() 
root.title('STELLAR EXPLORERS - Jonathan Silva')  
app_width = 1000
app_height = 700 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


title_font = ("Cambria", 35)
theme_font = ("Cambria", 28)

#Back Buttons ----------------------------------------------------------------------------------#

def back_to_main_menu(): #Select view back button
    select_view_frame.pack_forget() 
    main_frame.pack(expand=True, fill=BOTH) 

def back_to_main_menu_2(): #options back button
    options_view_frame.pack_forget() 
    main_frame.pack(expand=True, fill=BOTH) 

def back_to_main_menu_3(): #quiz ready back button
    quiz_view_frame.pack_forget() 
    main_frame.pack(expand=True, fill=BOTH) 

def back_to_sequential_view(): #sun back button
    sun_view_frame.pack_forget()
    select_view_frame.pack(expand=True, fill=BOTH) 

def back_to_sequential_view_2(): #Orbit View Back button
    orbit_view_frame.pack_forget()
    select_view_frame.pack(expand=True, fill=BOTH)  

def back_to_sun(): 
    mercury_view_frame.pack_forget() 
    sun() 

def back_to_mercury(): 
    venus_view_frame.pack_forget()
    mercury() 

def back_to_venus(): 
    earth_view_frame.pack_forget() 
    venus() 

def back_to_earth(): 
    mars_view_frame.pack_forget() 
    earth()

def back_to_mars(): 
    astbelt_view_frame.pack_forget() 
    mars() 

def back_to_astbelt(): 
    jupiter_view_frame.pack_forget() 
    astbelt() 

def back_to_jupiter(): 
    saturn_view_frame.pack_forget() 
    jupiter() 

def back_to_saturn(): 
    uranus_view_frame.pack_forget() 
    saturn() 

def back_to_uranus(): 
    neptune_view_frame.pack_forget() 
    uranus()

def back_to_main_menu_4(): #From neptune to main menu back button
    neptune_view_frame.pack_forget() 
    main_menu()

#-------------------------------------------------------------------------------------------------#

#PLANets 
def sun(): 
    global sun_view_frame 
    sun_view_frame = CTkFrame(root)
    sun_view_frame.pack(expand=True, fill=BOTH) 

    sun_title_label = CTkLabel(sun_view_frame, text="SUN", text_color= "Black", font=title_font)
    sun_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    sun_text = CTkScrollableFrame(sun_view_frame, width=400, height=550) 
    sun_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(sun_view_frame, text="Back", width=50, command=back_to_sequential_view)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(sun_view_frame, text="Next", width=50, command=next_to_mercury) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center") 

def mercury(): 
    global mercury_view_frame 
    mercury_view_frame = CTkFrame(root) 
    mercury_view_frame.pack(expand=True, fill=BOTH) 

    mercury_title_label = CTkLabel(mercury_view_frame, text="MERCURY", text_color= "Black", font=title_font)
    mercury_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    mercury_text = CTkScrollableFrame(mercury_view_frame, width=400, height=550) 
    mercury_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(mercury_view_frame, text="Back", width=50, command=back_to_sun)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(mercury_view_frame, text="Next", width=50, command=next_to_venus) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center") 

def venus():  
    global venus_view_frame 
    venus_view_frame = CTkFrame(root) 
    venus_view_frame.pack(expand=True, fill=BOTH) 

    venus_title_label = CTkLabel(venus_view_frame, text="VENUS", text_color= "Black", font=title_font)
    venus_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    venus_text = CTkScrollableFrame(venus_view_frame, width=400, height=550) 
    venus_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(venus_view_frame, text="Back", width=50, command=back_to_mercury)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(venus_view_frame, text="Next", width=50, command=next_to_earth) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  


def earth(): 
    global earth_view_frame 
    earth_view_frame = CTkFrame(root) 
    earth_view_frame.pack(expand=True, fill=BOTH) 

    earth_title_label = CTkLabel(earth_view_frame, text="EARTH", text_color= "Black", font=title_font)
    earth_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    earth_text = CTkScrollableFrame(earth_view_frame, width=400, height=550) 
    earth_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(earth_view_frame, text="Back", width=50, command=back_to_venus)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(earth_view_frame, text="Next", width=50, command=next_to_mars) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  

def mars():
    global mars_view_frame 
    mars_view_frame = CTkFrame(root) 
    mars_view_frame.pack(expand=True, fill=BOTH) 

    mars_title_label = CTkLabel(mars_view_frame, text="MARS", text_color= "Black", font=title_font)
    mars_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    mars_text = CTkScrollableFrame(mars_view_frame, width=400, height=550) 
    mars_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(mars_view_frame, text="Back", width=50, command=back_to_earth)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(mars_view_frame, text="Next", width=50, command=next_to_astbelt) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  

def astbelt(): 
    global astbelt_view_frame 
    astbelt_view_frame = CTkFrame(root) 
    astbelt_view_frame.pack(expand=True, fill=BOTH) 

    astbelt_title_label = CTkLabel(astbelt_view_frame, text="ASTEROID BELT", text_color= "Black", font=title_font)
    astbelt_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    astbelt_text = CTkScrollableFrame(astbelt_view_frame, width=400, height=550) 
    astbelt_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(astbelt_view_frame, text="Back", width=50, command=back_to_mars)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(astbelt_view_frame, text="Next", width=50, command=next_to_jupiter) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  

def jupiter(): 
    global jupiter_view_frame 
    jupiter_view_frame = CTkFrame(root) 
    jupiter_view_frame.pack(expand=True, fill=BOTH) 

    jupiter_title_label = CTkLabel(jupiter_view_frame, text="JUPITER", text_color= "Black", font=title_font)
    jupiter_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    jupiter_text = CTkScrollableFrame(jupiter_view_frame, width=400, height=550) 
    jupiter_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(jupiter_view_frame, text="Back", width=50, command=back_to_astbelt)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(jupiter_view_frame, text="Next", width=50, command=next_to_saturn) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center") 

def saturn(): 
    global saturn_view_frame 
    saturn_view_frame = CTkFrame(root) 
    saturn_view_frame.pack(expand=True, fill=BOTH) 

    saturn_title_label = CTkLabel(saturn_view_frame, text="SATURN", text_color= "Black", font=title_font)
    saturn_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    saturn_text = CTkScrollableFrame(saturn_view_frame, width=400, height=550) 
    saturn_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(saturn_view_frame, text="Back", width=50, command=back_to_jupiter)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(saturn_view_frame, text="Next", width=50, command=next_to_uranus) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center") 

def uranus(): 
    global uranus_view_frame 
    uranus_view_frame = CTkFrame(root) 
    uranus_view_frame.pack(expand=True, fill=BOTH) 

    uranus_title_label = CTkLabel(uranus_view_frame, text="URANUS", text_color= "Black", font=title_font)
    uranus_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    uranus_text = CTkScrollableFrame(uranus_view_frame, width=400, height=550) 
    uranus_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(uranus_view_frame, text="Back", width=50, command=back_to_saturn)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(uranus_view_frame, text="Next", width=50, command=next_to_neptune) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  

def neptune(): 
    global neptune_view_frame 
    neptune_view_frame = CTkFrame(root) 
    neptune_view_frame.pack(expand=True, fill=BOTH) 

    neptune_title_label = CTkLabel(neptune_view_frame, text="NEPTUNE", text_color= "Black", font=title_font)
    neptune_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    neptune_text = CTkScrollableFrame(neptune_view_frame, width=400, height=550) 
    neptune_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(neptune_view_frame, text="Back", width=50, command=back_to_uranus)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(neptune_view_frame, text="FINISH", width=50, command=back_to_main_menu_4) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  

#Next Buttons-------------------------------------------------------------------------------------#

def next_to_mercury():
    sun_view_frame.pack_forget()  
    mercury()

def next_to_venus():  
    mercury_view_frame.pack_forget()
    venus()

def next_to_earth(): 
    venus_view_frame.pack_forget()
    earth() 

def next_to_mars(): 
    earth_view_frame.pack_forget()
    mars() 

def next_to_astbelt(): 
    mars_view_frame.pack_forget()
    astbelt()

def next_to_jupiter(): 
    astbelt_view_frame.pack_forget()
    jupiter()

def next_to_saturn(): 
    jupiter_view_frame.pack_forget() 
    saturn() 

def next_to_uranus(): 
    saturn_view_frame.pack_forget() 
    uranus()

def next_to_neptune(): 
    uranus_view_frame.pack_forget()
    neptune()

#Start Button onwards---------------------------------------------------------------------------------#

def select_view():
    main_frame.pack_forget()
    main_frame.pack_forget()
    global select_view_frame
    select_view_frame = CTkFrame(root)
    select_view_frame.pack(expand=True, fill=BOTH)

    select_view_label = CTkLabel(select_view_frame, text="Would You like to view?", text_color= "Black", font=title_font)
    select_view_label.place(relx=0.5, rely=0.13, anchor="center")

    sequential_order_btn = CTkButton(select_view_frame, text="Sequential Order (The Sun)", width=100, height=80, command=sequential_view) 
    sequential_order_btn.place(relx=0.25, rely=0.275) 
    orbit_view_btn = CTkButton(select_view_frame, text="Orbit View (Pick Any)", width=150, height=80, command=orbit_view) 
    orbit_view_btn.place(relx=0.6, rely=0.275) 
    back_btn = CTkButton(select_view_frame, text="Back", text_color="Black", width=50, command=back_to_main_menu)
    back_btn.place(relx=0.09, rely=0.1, anchor="center") 

def sequential_view(): 
    select_view_frame.pack_forget() 
    sun()
    

def orbit_view():
    select_view_frame.pack_forget()  

    global orbit_view_frame 
    orbit_view_frame = CTkFrame(root) 
    orbit_view_frame.pack(expand=True, fill=BOTH)  

    orbit_view_label = CTkLabel(orbit_view_frame, text="Where would you like to go?", text_color= "Black", font=title_font)
    orbit_view_label.place(relx=0.5, rely=0.13, anchor="center") 

    back_btn = CTkButton(orbit_view_frame, text="Back", text_color="Black", width=50, command=back_to_sequential_view_2)
    back_btn.place(relx=0.09, rely=0.1, anchor="center") 

#-----------------------------------------------------------------------------------------------------------------------------------#


#Options Button onwards-------------------------------------------------------------------------------------------------------------#

def options_view(): 
    
    main_frame.pack_forget()

    global options_view_frame
    options_view_frame = CTkFrame(root)
    options_view_frame.pack(expand=True, fill=BOTH)

    back_btn = CTkButton(options_view_frame, text="Back", text_color="Black", width=50, command=back_to_main_menu_2)
    back_btn.place(relx=0.09, rely=0.1, anchor="center") 

#Themes
    theme_label = CTkLabel(options_view_frame, text="Themes", text_color="black", font=theme_font) 
    theme_label.place(relx=0.2, rely=0.225) 
    themes = ["Dark Blue", "Blue", "Green", "Light", "System", "Dark"]
    theme_combo = CTkComboBox(options_view_frame, values=themes, command=theme_select) 
    theme_combo.place(relx=0.18, rely=0.3)

#Zoom
    zoom_label = CTkLabel(options_view_frame, text="Zoom", text_color="black", font=theme_font) 
    zoom_label.place(relx=0.45, rely=0.225)  
    zoom = ["Zoom In", "Zoom Out"] 
    zoom_combo = CTkComboBox(options_view_frame, values=zoom, command=zoom_select)
    zoom_combo.place(relx=0.424, rely=0.3)

#Font
    font_label = CTkLabel(options_view_frame, text="Font", text_color="black", font=theme_font) 
    font_label.place(relx=0.7, rely=0.225)  
    font = ["Arial", "Cambira", "Spectral"] 
    font_combo = CTkComboBox(options_view_frame, values=font, command=zoom_select)
    font_combo.place(relx=0.665, rely=0.3)

def theme_select(choice): 
    pass

def zoom_select(choice): 
    pass

 



   #Zoom
#--------------------------------------------------------------------------------------------------------------------------------------#


def quiz_view(): 
    main_frame.pack_forget() 

    global quiz_view_frame 
    quiz_view_frame = CTkFrame(root)
    quiz_view_frame.pack(expand=True, fill=BOTH) 

    back_btn = CTkButton(quiz_view_frame, text="Back", text_color="Black", width=50, command=back_to_main_menu_3)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")

#Main Menu-  

main_frame = CTkFrame(root)
main_frame.pack(expand=True, fill=BOTH)
title_label = CTkLabel(main_frame, text="Stellar Explorers", text_color= "Black", font=title_font)
title_label.place(relx=0.5, rely=0.13, anchor="center")
start_btn = CTkButton(main_frame, text = "Start", command=select_view, width=200, height=35) 
start_btn.pack(pady=200)
options_btn = CTkButton(main_frame, text = "Options", command=options_view, width=200, height=35)
options_btn.place(relx=0.5, rely=0.45, anchor="center") 
quiz_btn = CTkButton(main_frame, text= "Quiz", command=quiz_view, width=200, height=35)
quiz_btn.place(relx=0.5, rely=0.59, anchor="center")


def main_menu(): 
    main_frame = CTkFrame(root)
    main_frame.pack(expand=True, fill=BOTH)
    title_label = CTkLabel(main_frame, text="Stellar Explorers", text_color= "Black", font=title_font)
    title_label.place(relx=0.5, rely=0.13, anchor="center")
    start_btn = CTkButton(main_frame, text = "Start", command=select_view, width=200, height=35) 
    start_btn.pack(pady=200)
    options_btn = CTkButton(main_frame, text = "Options", command=options_view, width=200, height=35)   
    options_btn.place(relx=0.5, rely=0.45, anchor="center") 
    quiz_btn = CTkButton(main_frame, text= "Quiz", command=quiz_view, width=200, height=35)
    quiz_btn.place(relx=0.5, rely=0.59, anchor="center")

def main_menu_2(): #Main menu from neptune 
    main_frame = CTkFrame(root)
    main_frame.pack(expand=True, fill=BOTH)
    title_label = CTkLabel(main_frame, text="Stellar Explorers", text_color= "Black", font=title_font)
    title_label.place(relx=0.5, rely=0.13, anchor="center")
    start_btn = CTkButton(main_frame, text = "Start", command=select_view, width=200, height=35) 
    start_btn.pack(pady=200)    
    options_btn = CTkButton(main_frame, text = "Options", command=options_view, width=200, height=35)
    options_btn.place(relx=0.5, rely=0.45, anchor="center") 
    quiz_btn = CTkButton(main_frame, text= "Quiz", command=quiz_view, width=200, height=35)
    quiz_btn.place(relx=0.5, rely=0.59, anchor="center")


root.mainloop()