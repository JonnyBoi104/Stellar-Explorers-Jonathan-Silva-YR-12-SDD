import tkinter as tk
from os import path
from customtkinter import *
from PIL import Image  
from pathlib import Path
from os import path  

main_path = path.dirname(path.abspath(__file__))
assets_path = path.join(main_path, "assets")

#Images-------------------------------------------------------
orbit_path = path.join(assets_path, "orbit.jpg")
orbit_image = Image.open(orbit_path)

sun_path = path.join(assets_path, "443.jpg") 
sun_image = Image.open(sun_path) 

def main_menu():  
    global main_frame
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

#--------------------------------------------------------------

# set theme 
set_appearance_mode("dark")
set_default_color_theme("blue")