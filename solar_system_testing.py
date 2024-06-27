import tkinter as tk
import customtkinter as ctk
from os import path
from customtkinter import *
from PIL import Image  
from pathlib import Path
from os import path  

main_path = path.dirname(path.abspath(__file__))
assets_path = path.join(main_path, "assets") 

#TEXT for each planet---------------------------------------- 
sun_info = str("The Sun is the star at the center of the Solar System. It is a nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field via a dynamo process. It is by far the most important source of energy for life on Earth. Its diameter is about 1.39 million kilometers, and it accounts for about 99.86% of the total mass of the Solar System. The Sun's gravity holds the Solar System together, keeping everything from the biggest planets to the smallest particles of debris in its orbit. Solar energy is created deep within the core of the Sun, where the temperature is about 15 million degrees Celsius. This energy then radiates outward from the core and is emitted as sunlight and other forms of radiation.")

#Images-------------------------------------------------------
orbit_path = path.join(assets_path, "orbit.jpg") #image for orbit view
orbit_image = Image.open(orbit_path) 

menu_path = path.join(assets_path, "title.jpg") #Main Menu image
menu_image = Image.open(menu_path)

sun_path = path.join(assets_path, "sun.jpg") 
sun_image = Image.open(sun_path) 

mercury_path = path.join(assets_path, "mercury.jpg") 
mercury_image = Image.open(mercury_path) 

venus_path = path.join(assets_path, "venus.jpg") 
venus_image = Image.open(venus_path) 

earth_path = path.join(assets_path, "earth.jpg") 
earth_image = Image.open(earth_path) 

mars_path = path.join(assets_path, "mars.png") 
mars_image = Image.open(mars_path) 

astbelt_path = path.join(assets_path, "asteroidbelt.jpg") 
astbelt_image = Image.open(astbelt_path)

jupiter_path = path.join(assets_path, "jupiter.png") 
jupiter_image = Image.open(jupiter_path)   

saturn_path = path.join(assets_path, "saturn.jpg") 
saturn_image = Image.open(saturn_path)    

uranus_path = path.join(assets_path, "uranus.jpg") 
uranus_image = Image.open(uranus_path)    

neptune_path = path.join(assets_path, "neptune-planet-space-5568916.webp") 
neptune_image = Image.open(neptune_path)

#-------------------------------------------------------------------




# Variables for theme, zoom, and font style
current_theme = "dark"
font_size = 20
font_family = "Helvetica"

font_style = ("Cambria", 35)

def set_theme(theme):
    global current_theme
    current_theme = theme
    set_appearance_mode(theme)
    update_fonts()

def set_zoom(zoom):
    global font_size
    font_size = int(zoom)
    update_fonts()

def set_font_style(font):
    global font_family
    font_family = font
    update_fonts()

def update_fonts():
    global title_font, text_font
    title_font = (font_family, font_size + 10)
    text_font = (font_family, font_size)

    # Update all widgets in the root window
    update_widget_font(root)

def update_widget_font(widget):
    if isinstance(widget, (CTkScrollableFrame, CTkFrame)):
        for child in widget.winfo_children():
            update_widget_font(child)
    elif isinstance(widget, CTkLabel):
        widget.configure(font=text_font)

# Main menu
def main_menu():  
    global main_frame
    main_frame = CTkFrame(root)
    main_frame.pack(expand=True, fill=BOTH) 


    menu_background = CTkLabel(main_frame, text="", image=CTkImage(menu_image, size=(1000, 700)))
    menu_background.place(relx=0.5, rely=0.5, anchor="c")

    title_label = CTkLabel(main_frame, text="Stellar Explorers", font=font_style, bg_color="transparent")
    title_label.place(relx=0.5, rely=0.13, anchor="center") 

    start_btn = CTkButton(main_frame, text = "Start", command=select_view, width=200, height=50) 
    start_btn.pack(pady=200) 



#--------------------------------------------------------------



# set theme 
set_appearance_mode("dark")
set_default_color_theme("blue") 


#Back Buttons ----------------------------------------------------------------------------------#

def back_to_main_menu(): #Select view back button
    select_view_frame.pack_forget() 
    main_frame.pack(expand=True, fill=BOTH) 

def back_to_sequential_view(): #sun back button
    sun_view_frame.pack_forget()
    select_view_frame.pack(expand=True, fill=BOTH) 

def back_to_sequential_view_2(): #Orbit View Back button
    orbit_view_frame.pack_forget()
    select_view_frame.pack(expand=True, fill=BOTH)  



#Functions for buttons in orbit view------------------------------------------------------------
def open_sun(): 
    orbit_view_frame.pack_forget()
    sun() 

def open_mercury(): 
    orbit_view_frame.pack_forget()
    mercury()  


#-------------------------------------------------------------------------------------------------#

#FUNCTION FOR PLANET BACK TO ORBIT FRAME------------------ 
def sun_to_orbit(): 
    sun_view_frame.pack_forget() 
    orbit_view() 


#-------------------------------- 

#PLANets--------------------------------------------------------------
def sun():  
    global sun_view_frame 
    sun_view_frame = CTkFrame(root) 
    sun_view_frame.pack(expand=True, fill=BOTH) 

    sun_background = CTkLabel(sun_view_frame, text="", image=CTkImage(sun_image, size=(900, 650)))
    sun_background.place(relx=0.5, rely=0.5, anchor="c") 

    sun_title_label = CTkLabel(sun_view_frame, text="SUN", font=title_font)
    sun_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    sun_text = CTkScrollableFrame(sun_view_frame, width=400, height=250) 
    sun_text.place(relx=0.55, rely=0.545) 

    sun_text_label = CTkLabel(sun_text, text= sun_info, wraplength=380)
    sun_text_label.pack(padx=10, pady=10)

    next_btn = CTkButton(sun_view_frame, text="Next", width=50, command=next_to_mercury) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  
    back_btn = CTkButton(sun_view_frame, text="Back", width=50, command=back_to_sequential_view)
    back_btn.place(relx=0.09, rely=0.1, anchor="center") 
    orbit_btn = CTkButton(sun_view_frame, text="To Orbit View", width=100, command=sun_to_orbit)
    orbit_btn.place(relx=0.875, rely=0.52, anchor="center")  


def mercury(): 
    pass 

#Next Buttons-------------------------------------------------------------------------------------#

def next_to_mercury():
    sun_view_frame.pack_forget()  
    mercury()


#Start Button onwards---------------------------------------------------------------------------------#

def select_view():
    main_frame.pack_forget()
    global select_view_frame
    select_view_frame = CTkFrame(root)
    select_view_frame.pack(expand=True, fill=BOTH)

    select_view_label = CTkLabel(select_view_frame, text="What would You like to view?", font=font_style)
    select_view_label.place(relx=0.5, rely=0.13, anchor="center")

    sequential_order_btn = CTkButton(select_view_frame, text="Sequentially View (The Sun)", width=100, height=80, command=sequential_view) 
    sequential_order_btn.place(relx=0.25, rely=0.275) 
    orbit_view_btn = CTkButton(select_view_frame, text="Orbit View (Pick Any)", width=150, height=80, command=orbit_view) 
    orbit_view_btn.place(relx=0.6, rely=0.275) 
    back_btn = CTkButton(select_view_frame, text="Back", width=50, command=back_to_main_menu)
    back_btn.place(relx=0.09, rely=0.1, anchor="center") 

def sequential_view(): 
    select_view_frame.pack_forget() 
    sun()
    
def orbit_view():
    select_view_frame.pack_forget()  

    global orbit_view_frame 
    orbit_view_frame = CTkFrame(root) 
    orbit_view_frame.pack(expand=True, fill=BOTH)  

    orbit_label = CTkLabel(orbit_view_frame, text="", image=CTkImage(orbit_image, size=(1000, 700)))
    orbit_label.place(relx=0.5, rely=0.5, anchor="c")
    orbit_view_label = CTkLabel(orbit_view_frame, text="Where would you like to go?", font=title_font)
    orbit_view_label.place(relx=0.5, rely=0.13, anchor="center") 

    sun_btn = CTkButton(orbit_view_frame, text="Sun", width=50, command=open_sun) 
    sun_btn.place(relx=0.475, rely=0.35) 
    mercury_btn = CTkButton(orbit_view_frame, text="Mercury", width=50, command=open_mercury) 
    mercury_btn.place(relx=0.39, rely=0.5) 

    back_btn = CTkButton(orbit_view_frame, text="Back", text_color="White", width=50, command=back_to_sequential_view_2)
    back_btn.place(relx=0.09, rely=0.1, anchor="center") 

#-----------------------------------------------------------------------------------------------------------------------------------#

#Options Button onwards-------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------------------------------------#

#Main Menu------------------------------------

   


#root = Tk() 
root = CTk() 
root.title('STELLAR EXPLORERS - Jonathan Silva')  
app_width = 1000
app_height = 700 

title_font = ("Cambria", 35)
theme_font = ("Cambria", 28)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

set_appearance_mode(current_theme)
update_fonts()
main_menu()  


#Menu bar functions--------------- 


#Themes-------
def light_theme():
    current_mode = ctk.get_appearance_mode()
    new_mode = "Light" if current_mode == "Dark" else "Dark"
    ctk.set_appearance_mode(new_mode)

def dark_theme(): 
    current_mode = ctk.get_appearance_mode()
    new_mode = "Dark" if current_mode == "Light" else "Dark"
    ctk.set_appearance_mode(new_mode)

def system_theme():
    current_mode = ctk.get_appearance_mode()
    new_mode = "System" if current_mode == "Dark" else "Dark"
    ctk.set_appearance_mode(new_mode)

#Zoom_---------- 
def zoom_in(): 
    sun_info = str("The Sun is the star at the center of the Solar System. It is a nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field via a dynamo process. It is by far the most important source of energy for life on Earth. Its diameter is about 1.39 million kilometers, and it accounts for about 99.86% of the total mass of the Solar System. The Sun's gravity holds the Solar System together, keeping everything from the biggest planets to the smallest particles of debris in its orbit. Solar energy is created deep within the core of the Sun, where the temperature is about 15 million degrees Celsius. This energy then radiates outward from the core and is emitted as sunlight and other forms of radiation.") +1


def zoom_out(): 
    pass 

#Font------------ 
def change_font_style(): 
    pass
  
#Menu Bar------------------------------------
menu_bar = tk.Menu(main_frame)  


theme_menu = tk.Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Light", command=light_theme)
theme_menu.add_command(label="Dark", command=dark_theme)
theme_menu.add_command(label="System", command=system_theme)
theme_menu.add_separator()
theme_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="Themes", menu=theme_menu)

#Zoom=--------------------------
zoom_menu = tk.Menu(menu_bar, tearoff=0)
zoom_menu.add_command(label="Zoom In", command=zoom_in)
zoom_menu.add_command(label="Zoom Out", command=zoom_out)
menu_bar.add_cascade(label="Zoom", menu=zoom_menu)
 
#--------------------------------------------


# Create the 'Font' menu---------------------------------------- 
fonts = ["Arial", "Cambria", "Cousine", "Spectral", "Helvetica", "Calibri"]
font_menu = tk.Menu(menu_bar, tearoff=0)

# Define available fonts
fonts = ["Arial", "Cambria", "Cousine", "Spectral", "Helvetica", "Calibri"]

# Add font options to the 'Font' menu
for font in fonts:
    font_menu.add_command(label=font, command=lambda f=font: change_font_style())

# Add the 'Font' menu to the menu bar
menu_bar.add_cascade(label="Font", menu=font_menu)

#Initialise current font size and font name 
current_font_size=25
current_font="Helvetica"

# Attach the menu bar to the window
root.config(menu=menu_bar) 

#=------------------------------------- 


#-----------------------------------------------------------------------------

root.mainloop()  


#fix menu bar disspearring after neptune -> main menu 
#do accessibility settings 
#add a hide button that hides the scrollable frame