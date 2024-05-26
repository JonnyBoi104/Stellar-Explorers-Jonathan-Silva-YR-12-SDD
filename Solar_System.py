import tkinter as tk
import customtkinter as ctk
from os import path
from customtkinter import *
from PIL import Image  
from pathlib import Path
from os import path  

main_path = path.dirname(path.abspath(__file__))
assets_path = path.join(main_path, "assets")

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
    root.config(menu="") 

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

def finish(): #From neptune to main menu back button
    neptune_view_frame.pack_forget()   
    main_menu()

#Functions for buttons in orbit view------------------------------------------------------------
def open_sun(): 
    orbit_view_frame.pack_forget()
    sun() 

def open_mercury(): 
    orbit_view_frame.pack_forget()
    mercury()  

def open_venus(): 
    orbit_view_frame.pack_forget()
    venus() 

def open_earth(): 
    orbit_view_frame.pack_forget()
    earth()  

def open_mars(): 
    orbit_view_frame.pack_forget()
    mars()  

def open_astbelt(): 
    orbit_view_frame.pack_forget()
    astbelt()  

def open_jupiter(): 
    orbit_view_frame.pack_forget()
    jupiter()  

def open_saturn(): 
    orbit_view_frame.pack_forget()
    saturn()  

def open_uranus(): 
    orbit_view_frame.pack_forget()
    uranus()  

def open_neptune(): 
    orbit_view_frame.pack_forget()
    neptune() 


#-------------------------------------------------------------------------------------------------#

#FUNCTION FOR PLANET BACK TO ORBIT FRAME------------------ 
def sun_to_orbit(): 
    sun_view_frame.pack_forget() 
    orbit_view() 

def mercury_to_orbit(): 
    mercury_view_frame.pack_forget() 
    orbit_view()

def venus_to_orbit(): 
    venus_view_frame.pack_forget() 
    orbit_view() 

def earth_to_orbit(): 
    earth_view_frame.pack_forget() 
    orbit_view()

def mars_to_orbit(): 
    mars_view_frame.pack_forget() 
    orbit_view()

def astbelt_to_orbit(): 
    astbelt_view_frame.pack_forget() 
    orbit_view() 

def jupiter_to_orbit(): 
    jupiter_view_frame.pack_forget() 
    orbit_view() 

def saturn_to_orbit(): 
    saturn_view_frame.pack_forget() 
    orbit_view()

def uranus_to_orbit(): 
    uranus_view_frame.pack_forget() 
    orbit_view() 

def neptune_to_orbit(): 
    neptune_view_frame.pack_forget() 
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
    sun_text = CTkScrollableFrame(sun_view_frame, width=400, height=550) 
    sun_text.place(relx=0.55, rely=0.165) 

    sun_text_label = CTkLabel(sun_text, text="The Sun is the star at the center of the Solar System. It is a nearly perfect sphere of hot plasma, with internal convective motion that generates a magnetic field via a dynamo process. It is by far the most important source of energy for life on Earth. Its diameter is about 1.39 million kilometers, and it accounts for about 99.86% of the total mass of the Solar System. The Sun's gravity holds the Solar System together, keeping everything from the biggest planets to the smallest particles of debris in its orbit. Solar energy is created deep within the core of the Sun, where the temperature is about 15 million degrees Celsius. This energy then radiates outward from the core and is emitted as sunlight and other forms of radiation.", wraplength=380)
    sun_text_label.pack(padx=10, pady=10)

    next_btn = CTkButton(sun_view_frame, text="Next", width=50, command=next_to_mercury) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  
    back_btn = CTkButton(sun_view_frame, text="Back", width=50, command=back_to_sequential_view)
    back_btn.place(relx=0.09, rely=0.1, anchor="center") 
    orbit_btn = CTkButton(sun_view_frame, text="To Orbit", width=100, command=sun_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")  

def mercury():  
    global mercury_view_frame 
    mercury_view_frame = CTkFrame(root) 
    mercury_view_frame.pack(expand=True, fill=BOTH)  

    mercury_background = CTkLabel(mercury_view_frame, text="", image=CTkImage(mercury_image, size=(900, 650)))
    mercury_background.place(relx=0.5, rely=0.5, anchor="c") 

    mercury_title_label = CTkLabel(mercury_view_frame, text="MERCURY", font=title_font)
    mercury_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    mercury_text = CTkScrollableFrame(mercury_view_frame, width=400, height=550) 
    mercury_text.place(relx=0.55, rely=0.165) 

    mercury_text_label = CTkLabel(mercury_text, text="Mercury is the closest planet to the Sun and the smallest planet in the solar system. It has a rocky body like Earth but is only about 38% of Earth's diameter. Mercury orbits the Sun every 88 days and has a very thin atmosphere, meaning it cannot retain heat and has extreme temperature fluctuations. Its surface is heavily cratered and similar in appearance to the Moon. Despite its proximity to the Sun, Mercury is not the hottest planet in the solar system; that title belongs to Venus. The lack of a significant atmosphere also means Mercury cannot support life as we know it. The planet has a large iron core that generates a magnetic field, albeit one that is only about 1% as strong as Earth's.", wraplength=380)
    mercury_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(mercury_view_frame, text="Back", width=50, command=back_to_sun)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(mercury_view_frame, text="Next", width=50, command=next_to_venus) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  
    orbit_btn = CTkButton(mercury_view_frame, text="To Orbit", width=100, command=mercury_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")

def venus():  
    global venus_view_frame 
    venus_view_frame = CTkFrame(root) 
    venus_view_frame.pack(expand=True, fill=BOTH)  

    venus_background = CTkLabel(venus_view_frame, text="", image=CTkImage(venus_image, size=(900, 650)))
    venus_background.place(relx=0.5, rely=0.5, anchor="c") 

    venus_title_label = CTkLabel(venus_view_frame, text="VENUS", font=title_font)
    venus_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    venus_text = CTkScrollableFrame(venus_view_frame, width=400, height=550) 
    venus_text.place(relx=0.55, rely=0.165) 

    venus_text_label = CTkLabel(venus_text, text="Venus is the second planet from the Sun and is similar in size and structure to Earth, earning it the title of Earth's twin. However, Venus has a thick, toxic atmosphere that traps heat, making it the hottest planet in the solar system with surface temperatures reaching 465 degrees Celsius. The atmosphere is composed mainly of carbon dioxide, with clouds of sulfuric acid, making the surface pressure 92 times that of Earth's. Venus has no moons and rotates very slowly on its axis, taking about 243 Earth days to complete one rotation. The planet's surface features numerous volcanoes, mountains, and large highland regions, with evidence suggesting that it is geologically active.", wraplength=380)
    venus_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(venus_view_frame, text="Back", width=50, command=back_to_mercury)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(venus_view_frame, text="Next", width=50, command=next_to_earth) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")   
    orbit_btn = CTkButton(venus_view_frame, text="To Orbit", width=100, command=venus_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")

def earth():  
    global earth_view_frame 
    earth_view_frame = CTkFrame(root) 
    earth_view_frame.pack(expand=True, fill=BOTH)  

    earth_background = CTkLabel(earth_view_frame, text="", image=CTkImage(earth_image, size=(900, 650)))
    earth_background.place(relx=0.5, rely=0.5, anchor="c")

    earth_title_label = CTkLabel(earth_view_frame, text="EARTH", font=title_font)
    earth_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    earth_text = CTkScrollableFrame(earth_view_frame, width=400, height=550) 
    earth_text.place(relx=0.55, rely=0.165) 

    earth_text_label = CTkLabel(earth_text, text="Earth is the third planet from the Sun and the only astronomical object known to harbor life. About 71% of Earth's surface is water-covered, and the atmosphere protects and supports life. Earth has a moderate climate, supported by its distance from the Sun, the presence of an atmosphere, and its magnetic field which shields it from harmful solar radiation. Earth is unique for its active plate tectonics and water cycle, which are essential in regulating the climate and enabling the diverse ecosystems found across the planet. Earth's atmosphere is composed of 78% nitrogen, 21% oxygen, and trace amounts of other gases, making it suitable for life as we know it.", wraplength=380)
    earth_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(earth_view_frame, text="Back", width=50, command=back_to_venus)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(earth_view_frame, text="Next", width=50, command=next_to_mars) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center") 
    orbit_btn = CTkButton(earth_view_frame, text="To Orbit", width=100, command=earth_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center") 

def mars():  
    global mars_view_frame 
    mars_view_frame = CTkFrame(root) 
    mars_view_frame.pack(expand=True, fill=BOTH)  

    mars_background = CTkLabel(mars_view_frame, text="", image=CTkImage(mars_image, size=(900, 650)))
    mars_background.place(relx=0.5, rely=0.5, anchor="c")

    mars_title_label = CTkLabel(mars_view_frame, text="MARS", font=title_font)
    mars_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    mars_text = CTkScrollableFrame(mars_view_frame, width=400, height=550) 
    mars_text.place(relx=0.55, rely=0.165) 

    mars_text_label = CTkLabel(mars_text, text="Mars is the fourth planet from the Sun and the second smallest planet in the solar system. Known as the Red Planet due to its reddish appearance, which is caused by iron oxide on its surface. Mars has the largest volcano in the solar system, Olympus Mons, and the deepest canyon, Valles Marineris. The planet's thin atmosphere is composed mostly of carbon dioxide. Mars has seasons, polar ice caps, and signs of ancient floods, but present-day water is scarce. Recent missions have found evidence of liquid water in the form of briny streaks on its surface, increasing the possibility that life once existed there or could exist in the future.", wraplength=380)
    mars_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(mars_view_frame, text="Back", width=50, command=back_to_earth)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(mars_view_frame, text="Next", width=50, command=next_to_astbelt) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  
    orbit_btn = CTkButton(mars_view_frame, text="To Orbit", width=100, command=mars_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")

def astbelt():  
    global astbelt_view_frame 
    astbelt_view_frame = CTkFrame(root) 
    astbelt_view_frame.pack(expand=True, fill=BOTH)  

    astbelt_background = CTkLabel(astbelt_view_frame, text="", image=CTkImage(astbelt_image, size=(900, 650)))
    astbelt_background.place(relx=0.5, rely=0.5, anchor="c")

    astbelt_title_label = CTkLabel(astbelt_view_frame, text="ASTEROID BELT", font=title_font)
    astbelt_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    astbelt_text = CTkScrollableFrame(astbelt_view_frame, width=400, height=550) 
    astbelt_text.place(relx=0.55, rely=0.165) 

    astbelt_text_label = CTkLabel(astbelt_text, text="The Asteroid Belt is a region of the solar system located between the orbits of Mars and Jupiter. It contains a vast number of irregularly shaped bodies called asteroids or minor planets. The largest object in the asteroid belt is the dwarf planet Ceres, which comprises about a third of the belt's total mass. The asteroids are composed of rock and metal, and their sizes vary from tiny dust particles to objects that are hundreds of kilometers in diameter. The Asteroid Belt is thought to be remnants from the early solar system that never formed into a planet due to the gravitational influence of Jupiter. These bodies are of great interest to scientists as they provide clues about the conditions and processes that shaped our solar system.", wraplength=380)
    astbelt_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(astbelt_view_frame, text="Back", width=50, command=back_to_mars)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(astbelt_view_frame, text="Next", width=50, command=next_to_jupiter) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  
    orbit_btn = CTkButton(astbelt_view_frame, text="To Orbit", width=100, command=astbelt_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")

def jupiter():  
    global jupiter_view_frame 
    jupiter_view_frame = CTkFrame(root) 
    jupiter_view_frame.pack(expand=True, fill=BOTH) 

    jupiter_background = CTkLabel(jupiter_view_frame, text="", image=CTkImage(jupiter_image, size=(900, 650)))
    jupiter_background.place(relx=0.5, rely=0.5, anchor="c") 

    jupiter_title_label = CTkLabel(jupiter_view_frame, text="JUPITER", font=title_font)
    jupiter_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    jupiter_text = CTkScrollableFrame(jupiter_view_frame, width=400, height=550) 
    jupiter_text.place(relx=0.55, rely=0.165) 

    jupiter_text_label = CTkLabel(jupiter_text, text="Jupiter is the fifth planet from the Sun and the largest in the solar system. It is a gas giant with a mass one-thousandth that of the Sun but two and a half times that of all the other planets in the solar system combined. Jupiter is known for its prominent bands of clouds and its Great Red Spot, a giant storm that has persisted for at least 400 years. The planet has a strong magnetic field and at least 79 moons, including the four large Galilean moons: Io, Europa, Ganymede, and Callisto. These moons are of great interest due to their potential subsurface oceans and geological activity. Jupiter's atmosphere is primarily composed of hydrogen and helium, with traces of other gases.", wraplength=380)
    jupiter_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(jupiter_view_frame, text="Back", width=50, command=back_to_astbelt)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(jupiter_view_frame, text="Next", width=50, command=next_to_saturn) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")  
    orbit_btn = CTkButton(jupiter_view_frame, text="To Orbit", width=100, command=jupiter_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")

def saturn():  
    global saturn_view_frame 
    saturn_view_frame = CTkFrame(root) 
    saturn_view_frame.pack(expand=True, fill=BOTH)  

    saturn_background = CTkLabel(saturn_view_frame, text="", image=CTkImage(saturn_image, size=(900, 650)))
    saturn_background.place(relx=0.5, rely=0.5, anchor="c") 

    saturn_title_label = CTkLabel(saturn_view_frame, text="SATURN", font=title_font)
    saturn_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    saturn_text = CTkScrollableFrame(saturn_view_frame, width=400, height=550) 
    saturn_text.place(relx=0.55, rely=0.165) 

    saturn_text_label = CTkLabel(saturn_text, text="Saturn is the sixth planet from the Sun and the second largest in the solar system, renowned for its stunning ring system. The rings are composed of countless small particles of ice and rock, ranging in size from micrometers to meters, that orbit the planet. Saturn is a gas giant like Jupiter, with an atmosphere mostly made up of hydrogen and helium. It has at least 83 moons, with Titan being the largest. Titan is larger than the planet Mercury and has a thick atmosphere and liquid hydrocarbon lakes on its surface, making it one of the most Earth-like bodies in the solar system. Saturn's magnetic field is also substantial, though it is weaker than Jupiter's. The planet's unique and complex ring system has been studied extensively, offering insights into planetary ring dynamics and the conditions in the early solar system.", wraplength=380)
    saturn_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(saturn_view_frame, text="Back", width=50, command=back_to_jupiter)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(saturn_view_frame, text="Next", width=50, command=next_to_uranus) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")   
    orbit_btn = CTkButton(saturn_view_frame, text="To Orbit", width=100, command=saturn_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")

def uranus():  
    global uranus_view_frame 
    uranus_view_frame = CTkFrame(root) 
    uranus_view_frame.pack(expand=True, fill=BOTH)  

    uranus_background = CTkLabel(uranus_view_frame, text="", image=CTkImage(uranus_image, size=(900, 650)))
    uranus_background.place(relx=0.5, rely=0.5, anchor="c") 

    uranus_title_label = CTkLabel(uranus_view_frame, text="URANUS", font=title_font)
    uranus_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    uranus_text = CTkScrollableFrame(uranus_view_frame, width=400, height=550) 
    uranus_text.place(relx=0.55, rely=0.165) 

    uranus_text_label = CTkLabel(uranus_text, text="Uranus is the seventh planet from the Sun and is classified as an ice giant due to its composition. It has a unique blue-green color due to the presence of methane in its atmosphere. Uranus is tilted on its side, with an axial tilt of 98 degrees, making its rotation nearly parallel to the Sun. This unusual tilt causes extreme seasonal variations during its 84-year orbit. Uranus has 27 known moons and a faint ring system composed of dark, narrow rings. The planet's atmosphere is primarily hydrogen and helium, with trace amounts of water, ammonia, and methane. Uranus' cold and featureless appearance belies the complex and dynamic processes occurring in its atmosphere and interior.", wraplength=380)
    uranus_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(uranus_view_frame, text="Back", width=50, command=back_to_saturn)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(uranus_view_frame, text="Next", width=50, command=next_to_neptune) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center") 
    orbit_btn = CTkButton(uranus_view_frame, text="To Orbit", width=100, command=uranus_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")

def neptune():  
    global neptune_view_frame 
    neptune_view_frame = CTkFrame(root) 
    neptune_view_frame.pack(expand=True, fill=BOTH)  

    neptune_background = CTkLabel(neptune_view_frame, text="", image=CTkImage(neptune_image, size=(900, 650)))
    neptune_background.place(relx=0.5, rely=0.5, anchor="c") 

    neptune_title_label = CTkLabel(neptune_view_frame, text="NEPTUNE", font=title_font)
    neptune_title_label.place(relx=0.5, rely=0.1, anchor="center") 
    neptune_text = CTkScrollableFrame(neptune_view_frame, width=400, height=550) 
    neptune_text.place(relx=0.55, rely=0.165) 

    neptune_text_label = CTkLabel(neptune_text, text="Neptune is the eighth planet from the Sun and is similar in composition to Uranus. It is an ice giant with a deep blue color due to the presence of methane in its atmosphere. Neptune has the strongest winds in the solar system, with speeds reaching up to 2,100 kilometers per hour (1,300 miles per hour). It has 14 known moons, with Triton being the largest. Triton is geologically active, with geysers of liquid nitrogen, making it one of the most interesting moons in the solar system. Neptune's atmosphere is dynamic, with large storms and dark spots similar to Jupiter's Great Red Spot. The planet's internal heat contributes to its weather patterns and the turbulent conditions in its atmosphere.", wraplength=380)
    neptune_text_label.pack(padx=10, pady=10)

    back_btn = CTkButton(neptune_view_frame, text="Back", width=50, command=back_to_uranus)
    back_btn.place(relx=0.09, rely=0.1, anchor="center")  
    next_btn = CTkButton(neptune_view_frame, text="Next", width=50, command=finish) 
    next_btn.place(relx=0.91, rely=0.1, anchor="center")   
    orbit_btn = CTkButton(neptune_view_frame, text="To Orbit", width=100, command=neptune_to_orbit)
    orbit_btn.place(relx=0.5, rely=0.95, anchor="center")

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
    global select_view_frame
    select_view_frame = CTkFrame(root)
    select_view_frame.pack(expand=True, fill=BOTH)

    select_view_label = CTkLabel(select_view_frame, text="Would You like to view?", font=font_style)
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
    venus_btn = CTkButton(orbit_view_frame, text="Venus", width=50, command=open_venus) 
    venus_btn.place(relx=0.59, rely=0.49) 
    earth_btn = CTkButton(orbit_view_frame, text="Earth", width=50, command=open_earth) 
    earth_btn.place(relx=0.31, rely=0.415) 
    mars_btn = CTkButton(orbit_view_frame, text="Mars", width=50, command=open_mars) 
    mars_btn.place(relx=0.31, rely=0.579)
    astbelt_btn = CTkButton(orbit_view_frame, text="Asteroid Belt", width=50, command=open_astbelt) 
    astbelt_btn.place(relx=0.55, rely=0.675)  
    jupiter_btn = CTkButton(orbit_view_frame, text="Jupiter", width=50, command=open_jupiter) 
    jupiter_btn.place(relx=0.16, rely=0.62)  
    saturn_btn = CTkButton(orbit_view_frame, text="Saturn", width=50, command=open_saturn) 
    saturn_btn.place(relx=0.82, rely=0.54) 
    uranus_btn = CTkButton(orbit_view_frame, text="Uranus", width=50, command=open_uranus) 
    uranus_btn.place(relx=0.78, rely=0.78)
    neptune_btn = CTkButton(orbit_view_frame, text="Neptune", width=50, command=open_neptune) 
    neptune_btn.place(relx=0.085, rely=0.785)

    back_btn = CTkButton(orbit_view_frame, text="Back", text_color="White", width=50, command=back_to_sequential_view_2)
    back_btn.place(relx=0.09, rely=0.1, anchor="center") 

#-----------------------------------------------------------------------------------------------------------------------------------#

#Options Button onwards-------------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------------------------------------#

#Main Menu------------------------------------

def main_menu_2(): #Main menu from neptune  
    neptune_view_frame.pack_forget()
    main_frame = CTkFrame(root)
    main_frame.pack(expand=True, fill=BOTH)
    title_label = CTkLabel(main_frame, text="Stellar Explorers", text_color= "Gray", font=title_font)
    title_label.place(relx=0.5, rely=0.13, anchor="center") 

    menu_background = CTkLabel(main_frame, text="", image=CTkImage(menu_image, size=(1000, 700)))
    menu_background.place(relx=0.5, rely=0.5, anchor="c")

    start_btn = CTkButton(main_frame, text = "Start", command=select_view, width=200, height=35) 
    start_btn.pack(pady=200)    


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
    pass 

def zoom_out(): 
    pass 

#Font------------ 
def change_font_style():
    global main_frame, select_view_frame, orbit_view_frame, sun_view_frame, mercury_view_frame, venus_view_frame, earth_view_frame, mars_view_frame, jupiter_view_frame, saturn_view_frame, uranus_view_frame, neptune_image
    
    

def update_all_fonts(widget, font):
    widget_type = widget.winfo_class()
    if widget_type in ('CTkLabel', 'CTkButton', 'CTkEntry', 'CTkScrollableFrame'):
        widget.configure(font=(font, 14))
    for child in widget.winfo_children():
        update_all_fonts(child, font)

#Menu Bar------------------------------------
menu_bar = tk.Menu(main_frame)  
root.config(menu="")

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
    font_menu.add_command(label=font, command=lambda f=font: change_font_style(f))

# Add the 'Font' menu to the menu bar
menu_bar.add_cascade(label="Font", menu=font_menu)

#Initialise current font size and font name 
current_font_size=25
current_font="Helvetica"

# Attach the menu bar to the window
root.config(menu=menu_bar)

#-----------------------------------------------------------------------------

root.mainloop() 