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

def back_to_sun_view(): 
    mercury_view_frame.pack_forget() 
    sun_view_frame.pack(expand=True, fill=BOTH)


#-------------------------------------------------------------------------------------------------#

#Next Buttons-------------------------------------------------------------------------------------#

def next_to_mercury():
    sun_view_frame.pack_forget()  

    global mercury_view_frame 
    mercury_view_frame = CTkFrame(root) 
    mercury_view_frame.pack(expand=True, fill=BOTH) 

    mercury_title_label = CTkLabel(mercury_view_frame, text="MERCURY", text_color= "Black", font=title_font)
    mercury_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    mercury_text = CTkScrollableFrame(mercury_view_frame, width=400, height=550) 
    mercury_text.place(relx=0.55, rely=0.165) 

    back_btn = CTkButton(mercury_view_frame, text="Back", width=50, command=back_to_sun_view)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(sun_view_frame, text="Next", width=50, command=next_to_venus) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center") 

def next_to_venus(): 
    pass


#Start Button onwards---------------------------------------------------------------------------------#

def select_view():
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