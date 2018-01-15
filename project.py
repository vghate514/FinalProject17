#Import Lists from separate documents
from planets import *
from stars import *

#Formatting function
def divider(message):
    print('-'*20)
    print(message)
    print('-'*20)

#Sets up motion of Telescope
class Telescope():
    def __init__(self):
    #Motion in two axes (measured in degrees)
        #Direction
        self.x = 0
        #Elevation
        self.y = 0
    """Because the user only chooses from a pre-determined list of objects,
    there is no need to limit the range of the telescope's motion"""
    def go_to(self,object):
        self.x = object[0]
        self.y = object[1]

    def report(self):
        print(self.x)
        print(self.y)

def list_options(what, label, listname):
    optionlist = 1
    divider(label)
    if listname == None:
        for thing in what:
            print(optionlist, thing)
            optionlist += 1
    else:
        for thing in what:
            print(optionlist, thing)
            listname.append(thing)
            optionlist += 1

Tel_1 = Telescope()
test = [200,26]

#Catalog of Objects that Telescope can search (coordinates from other imported files)
catalog = {
    "Stars":{
        "Sirius":sirius,
        "Vega":vega,
        "Polaris":polaris
        },
    "Planets":{
        "Jupiter":jupiter,
        "Mars":mars,
        "Venus":venus
        }
    }

#Populate list with catalog keys so that there is no out-of-orderness due to dictionaies
selection = []
for key in catalog.keys():
    selection.append(key)

list_options(selection, "Catalogs", None)

cat_choice = int(input("Select a category by selecting the number: "))
current = selection[cat_choice-1]

list_of_objects = []

list_options(catalog[current], f"Entering the {current} catalog", list_of_objects)

print(list_of_objects)
obj_choice = int(input("Select an object by selecting the number: "))
obj = list_of_objects[(obj_choice - 1)]

coor = catalog[current].get(obj)

print(coor)

""""Tel_1.go_to(test)
Tel_1.report
print(catalog["Stars"].get("Sirius")[0])
"""
