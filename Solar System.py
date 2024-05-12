from tkinter import *  
from os import path
from customtkinter import *
from PIL import Image  



# set theme 
set_appearance_mode("dark")
set_default_color_theme("blue")

#root = Tk() 
root = CTk() 
root.title('STELLAR EXPLORERS')  
app_width = 1000
app_height = 700 

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


font_style = ("Helvetica", 35)


def back_to_main_menu():
    select_view_frame.pack_forget()
    main_frame.pack(expand=True, fill=BOTH)


def select_view():
    main_frame.pack_forget()

    global select_view_frame
    select_view_frame = CTkFrame(root)
    select_view_frame.pack(expand=True, fill=BOTH)

    back_btn = CTkButton(select_view_frame, text="Back", text_color="Black", width=50, command=back_to_main_menu)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")

def options_view():
    main_frame.pack_forget()

    global options_view_frame
    options_view_frame = CTkFrame(root)
    options_view_frame.pack(expand=True, fill=BOTH)

    back_btn = CTkButton(options_view_frame, text="Back", text_color="Black", width=50, command=back_to_main_menu)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")

def quiz_view(): 
    main_frame.pack_forget() 

    global quiz_view_frame 
    quiz_view_frame = CTkFrame(root)
    quiz_view_frame.pack(expand=True, fill=BOTH) 

    back_btn = CTkButton(quiz_view_frame, text="Back", text_color="Black", width=50, command=back_to_main_menu)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")

main_frame = CTkFrame(root)
main_frame.pack(expand=True, fil=BOTH)
title_label = CTkLabel(main_frame, text="Stellar Explorers", text_color= "Black", font=font_style)
title_label.place(relx=0.5, rely=0.2, anchor="center")
start_btn = CTkButton(main_frame, text = "Start", command=select_view) 
start_btn.pack(pady=150)
options_btn = CTkButton(main_frame, text = "Options", command=options_view)
options_btn.place(relx=0.5, rely=0.5, anchor="center") 
quiz_btn = CTkButton(main_frame, text= "Quiz", command=quiz_view)
quiz_btn.place(relx=0.5, rely=0.59, anchor="center")


root.mainloop()