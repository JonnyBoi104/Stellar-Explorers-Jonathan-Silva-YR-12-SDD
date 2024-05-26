import customtkinter as ctk
from tkinter import Menu

# Function to change the font style
def change_font_style(new_font):
    global current_font
    current_font = new_font
    label.configure(font=(current_font, 14))
    print(f"Font changed to: {current_font}")

# Initialize the CTk application
app = ctk.CTk()
app.title("CustomTkinter Font Style Change Example")
app.geometry("300x200")

# Create a menu bar
menu_bar = Menu(app)

# Create the 'Font' menu
font_menu = Menu(menu_bar, tearoff=0)

# Define available fonts
fonts = ["Arial", "Times New Roman", "Courier New"]

# Add font options to the 'Font' menu
for font in fonts:
    font_menu.add_command(label=font, command=lambda f=font: change_font_style(f))

# Add the 'Font' menu to the menu bar
menu_bar.add_cascade(label="Font", menu=font_menu)

# Configure the menu bar
app.config(menu=menu_bar)

# Add a label to the window for visual feedback
current_font = "Arial"  # Set a default font
label = ctk.CTkLabel(app, text="Use the menu to change the font style", font=(current_font, 14))
label.pack(pady=20)

# Start the application
app.mainloop()
