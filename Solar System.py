from tkinter import *  
from os import path
from customtkinter import *
from PIL import Image  



# set theme
set_appearance_mode("light")
set_default_color_theme("blue")

#root = Tk()
root = CTk()
root.title('STELLAR EXPLORERS')
root.geometry('600x400')


font_style = ("arial", 35)


def back_to_main_menu():
    select_view_frame.pack_forget()
    main_frame.pack(expand=True, fill=BOTH)


def select_view():
    main_frame.pack_forget()

    global select_view_frame
    select_view_frame = CTkFrame(root)
    select_view_frame.pack(expand=True, fill=BOTH)

    back_btn = CTkButton(select_view_frame, text="Back", text_color="Black", command=back_to_main_menu)
    back_btn.place(relx=0.15, rely=0.9, anchor="center")

def options_view():
    pass

main_frame = CTkFrame(root)
main_frame.pack(expand=True, fil=BOTH)
title_label = CTkLabel(main_frame, text="Stellar Explorers", text_color= "Black", font=font_style)
title_label.place(relx=0.5, rely=0.2, anchor="center")
start_btn = CTkButton(main_frame, text = "Start", command=select_view)
start_btn.pack(pady=150)
options_btn = CTkButton(main_frame, text = "Options", command=options_view)
options_btn.pack(pady=170)


root.mainloop()