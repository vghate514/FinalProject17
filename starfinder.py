#Import Lists from separate documents and math
from stars import *
from location import *
from date_time import *
import math as m

#Formatting function, for aesthetic
def divider(message):
    print('-'*20)
    print(message)
    print('-'*20)

#Clear Screen function, tidy up console
def clear():
    import os
    os.system("clear")

#Sets up motion of Telescope
class Telescope():
    def __init__(self):
    #Motion in two axes (measured in degrees)
        #Direction (AZ)
        self.x = 0
        #Elevation (ALT)
        self.y = 0
    #Because the user only chooses from a pre-determined list of objects,
    #there is no need to limit the range of the telescope's motion
    def go_to(self,object):
        self.x = object[0]
        self.y = object[1]

    def report(self):
        print(f"AZ: {self.x}")
        print(f"ALT: {self.y}")

"""The function below is for user interface and backend organization. The function prints out a list of all the objects with corresponding number choices,
and adds the items to a list in order to create a constant and reliable method of calling objects using numbers."""
def list_options(location_of_items_to_be_listed, label):
    optionlist = 1
    divider(label)
    for thing in location_of_items_to_be_listed:
        print(optionlist, thing)
        optionlist += 1
    print("")

Tel_1 = Telescope()

#Bulk of program defined as a function in order to run a continuous loop without the user having to start over.
def program():
        #Catalog of Objects that Telescope can search (coordinates from other imported files)
        catalog = {
            "Stars":{
                "Sirius":sirius,
                "Vega":vega,
                "Shaula":shaula,
                "Saiph":saiph,
                "Rigel":rigel,
                "Regulus":regulus,
                "Rasalhague":rasalhague,
                "Rasalgethi":rasalgethi,
                "Procyon":procyon
            }
        }

        #Populate list with catalog keys so that there is no out-of-orderness due to dictionaies
        selection = []
        items_in_selection = 0
        for key in catalog.keys():
            selection.append(key)
            items_in_selection += 1

        list_options(selection, "Catalogs")

        #Avoids Breaking Program when given bad input.
        while True:
            cat_choice = (input("Select a category by selecting the number: "))
            try:
                cat_choice = int(cat_choice)
                if cat_choice-1 >= items_in_selection or cat_choice-1 < 0:
                    print("*Please select a valid number*")
                    continue
                else: break
            except: print("*Please enter a number*")
        #Enters catalog chosen (only one available, but allows for more to be added in future)
        current = selection[cat_choice-1]

        list_of_objects = []
        number_of_items = 0
        for obj in catalog[current]:
            list_of_objects.append(obj)
            number_of_items += 1

        print(" ")
        list_options(catalog[current], f"Entering the {current} catalog")

        #Prevents bad user input while selecting an object from catalog
        while True:
            try:
                obj_choice = int(input("Select an object by selecting the number: "))
                if obj_choice-1 >= number_of_items or obj_choice-1 < 0:
                    print("*Please select a valid number*")
                    continue
                else: break
            except: print("*Enter a number*")

        #Selects object from current catalog
        obj = list_of_objects[(obj_choice - 1)]

        #Pulls values mapped to object from external file
        coor_values = catalog[current].get(obj)

        #Star Celestial Coordinates
        RA = coor_values[0]
        DEC = coor_values[1]

        #Calculating Hour Angle of Star
        HA = lst_time - RA
        while HA not in range(361):
            if HA < 0:
                HA += 360
                continue
            elif HA > 360:
                HA -= 360
                continue
            else: break

        #Python can only handle radians so here we convert from degrees to radians
        HA = m.radians(HA)
        RA = m.radians(RA)
        DEC = m.radians(DEC)
        lat1 = m.radians(lat)

        #Calculating ALT of Star
        sin_ALT = m.sin(RA)*m.sin(lat1)+m.cos(DEC)*m.cos(lat1)*m.cos(HA)
        ALT = m.asin(sin_ALT)
        #Python can only handle radians so here we convert from degrees to radians
        alt = m.radians(ALT)
        #Calculating AZ of Star
        cos_A = ((m.sin(DEC) - m.sin(alt)*m.sin(lat1))/(m.cos(alt)*m.cos(lat1)))
        A = m.acos(cos_A)
        if ALT < 0:
            AZ = A
        else:
            AZ = ALT - A
        AZ = m.degrees(AZ)
        ALT = m.degrees(alt)
        da_wae = [AZ, ALT]

        #Gives Telescope the altitude and azimuth in degrees of the object, adjusted for location
        Tel_1.go_to(da_wae)

        print(f"\nYour telescope is pointing at {obj}.\n")
        Tel_1.report()
"""
"""
#Continuous Loop to allow user to run program again without physically re-opening the file.
while True:
    program()
    cont = (input("Type 'e' to exit. Press any other key to continue: ")).lower()
    print("")
    if cont == 'e':
        clear()
        print("Have a good day!")
        print("""⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠶⣿⣭⡧⡤⣤⣻⣛⣹⣿⣿⣿⣶⣄
⢀⢀⢀⢀⢀⢀⢀⢀⢀⣼⣊⣤⣶⣷⣶⣧⣤⣽⣿⣿⣿⣿⣿⣿⣷
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢀⢀⢀⢀⢀⢀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⢀⢀⢀⢀⢀⢀⠸⠿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣻⣿⣿⣿⣿⣿⡆
⢀⢀⢀⢀⢀⢀⢀⢸⣿⣿⡀⠘⣿⡿⢿⣿⣿⡟⣾⣿⣯⣽⣼⣿⣿⣿⣿⡀
⢀⢀⢀⢀⢀⢀⡠⠚⢛⣛⣃⢄⡁⢀⢀⢀⠈⠁⠛⠛⠛⠛⠚⠻⣿⣿⣿⣷
⢀⢀⣴⣶⣶⣶⣷⡄⠊⠉⢻⣟⠃⢀⢀⢀⢀⡠⠔⠒⢀⢀⢀⢀⢹⣿⣿⣿⣄⣀⣀⣀⣀⣀⣀
⢠⣾⣿⣿⣿⣿⣿⣿⣿⣶⣄⣙⠻⠿⠶⠒⠁⢀⢀⣀⣤⣰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄
⢿⠟⠛⠋⣿⣿⣿⣿⣿⣿⣿⣟⡿⠷⣶⣶⣶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢀⢀⢀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠙⠻⠿⣿⣿⡿
⢀⢀⢀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⢀⢀⢀⠈⠁
⢀⢀⢀⢀⢸⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢀⢀⢀⢀⢸⣿⣿⣿⣿⣄⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣹⣿⣿⣿⣿⣿⣿⣿⣿⠇
⢀⢀⢀⢀⢀⢻⣿⣿⣿⣿⣧⣀⢀⢀⠉⠛⠛⠋⠉⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠏
⢀⢀⢀⢀⢀⢀⢻⣿⣿⣿⣿⣿⣷⣤⣄⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋
⢀⢀⢀⢀⢀⢀⢀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢹⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⣿⡇⢀⠈⠙⠛⠛⠛⠛⠛⠛⠻⣿⣿⣿⠇
⢀⢀⢀⢀⢀⢀⢀⢀⢀⣸⣿⡇⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢨⣿⣿
⢀⢀⢀⢀⢀⢀⢀⢀⣾⣿⡿⠃⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⣿⡏
⢀⢀⢀⢀⢀⢀⢀⢀⠻⠿⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢠⣿⣿⡇
""")
        print("I hope you find da wae.")
        break
    else:
        clear()
        continue