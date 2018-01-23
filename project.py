#Import Lists from separate documents and math
from stars import *
from location import *
from date_time import *
import math as m

#Formatting function
def divider(message):
    print('-'*20)
    print(message)
    print('-'*20)

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

def list_options(location_of_items_to_be_listed, label):
    optionlist = 1
    divider(label)
    for thing in location_of_items_to_be_listed:
        print(optionlist, thing)
        optionlist += 1

Tel_1 = Telescope()

#Bulk of program defined as a function in order to run a continuous loop without the user having to start over.
def program():
        #Catalog of Objects that Telescope can search (coordinates from other imported files)
        catalog = {
            "Stars":{
                "Sirius":sirius,
                "Vega":vega,
                "Polaris":polaris
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
                if cat_choice-1 >= items_in_selection:
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

        list_options(catalog[current], f"Entering the {current} catalog")

        #Prevents bad user input while selecting an object from catalog
        while True:
            try:
                obj_choice = int(input("Select an object by selecting the number: "))
                if obj_choice-1 >= number_of_items:
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
            else: continue

        #Calculating ALT of Star
        sin_ALT = m.sin(RA)*m.sin(lat)+m.cos(DEC)*m.cos(lat)*m.cos(HA)
        ALT = m.asin(sin_ALT)

        #Calculating AZ of Star
        cos_A = (m.sin(DEC) - m.sin(ALT)*m.sin(lat))/(m.cos(ALT)*m.cos(lat))
        A = m.acos(cos_A)
        if ALT < 0:
            AZ = A
        else:
            AZ = ALT - A

        da_wae = [AZ, ALT]

        #Gives Telescope the altitude and azimuth in degrees of the object, adjusted for location
        Tel_1.goto(da_wae)

        print(f"Your telescope is pointing at {obj}.\n{Tel_1.report()}")


#Continuous Loop to allow user to run program again without exiting.
while True:
    program()
    cont = (input("Type 'e' to exit. Press any other key to continue: ")).lower()
    if cont == 'e':
        print("Have a good day!")
        break
    else: continue