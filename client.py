#copied Socket Client segement 
import socket
#s = socket.socket()
#host = socket.gethostname()
#port = 9999
#address = (host, port)
#msg = 'test 123'
#s.connect(address)
#s.send(msg)

from GUI import Window, Button, Font, ListButton, application
from GUI.StdFonts import system_font
from GUI.StdColors import red, black
from testing import say

free_room_counter = 1

free_cities = {1:"Detorit" , 2:"Montreal", 3:"Vancouver", 4:"Victoria", 5:"Calgary", 6:"Edmonton", 7:"Quebec City", 8:"Ottawa", 9:"Toronto", 10:"Winipeg", 11:"Churchill", 12:"Saskatoon", 13:"Regina", 14:"Yellowknife", 15:"Whitehorse", 16:"Dawson City", 17:"Fort Simson", 18:"Iqaluit", 19:"Resolute", 20:"Fredrickton", 21:"Saint John", 22:"Halifax", 23:"Dartmouth", 24:"St. Johns", 25:"Grand Falls-Windsor", 26:"Charlottetown", 27:"Summerside"}

taken_cities = {}

current_city = "Earth"

def founded_city(): #possibly consider making a function for disabling buttons to reduce code copyingg
    global free_room_counter
    current_city = free_cities[create_list_button.value + free_room_counter]
    print "Founded the city of", current_city
    taken_cities[len(taken_cities)+1] = current_city
    del free_cities[create_list_button.value + free_room_counter]
    free_room_counter = free_room_counter + 1
    remove_window()
    refresh_buttons()
    print taken_cities
    print free_cities
    create_list_button.enabled = 0
    join_list_button.enabled = 0
    join_button.enabled = 0
    create_button.enabled = 0

def joined_city():
    global free_room_counter
    current_city = taken_cities[join_list_button.value + 1]
    print "Moved to the city of", current_city
    remove_window()
    refresh_buttons()
    join_list_button.enabled = 0
    create_list_button.enabled = 0
    join_button.enabled = 0
    create_button.enabled = 0
    print taken_cities
    print free_cities

def empty_city_list():
    create_list_button.enabled = 1

def occupied_city_list(): # enables the list 
    join_list_button.enabled = 1

def leave_city():
    join_button.enabled = 1
    create_button.enabled = 1

join_button = Button(position = (30, 30), 
        title = "Join City", 
        action = occupied_city_list, 
        style = 'cancel')

join_list_button = ListButton(position = (30, join_button.bottom + 30), 
    titles = ["Move to %s" % taken_cities[i] for i in taken_cities], #need to add so only occupied free_cities are avaliable to be moved to
    action = joined_city)

    # create_button for creating a city

create_button = Button(position = (join_list_button.right + 30, 30),
    title = "Create City", 
    action = empty_city_list, 
    style = 'cancel')

    #button 4 for list of not yet created free_cities

create_list_button = ListButton(position = (join_list_button.right + 30, create_button.bottom + 30), 
    titles = ["Found %s" % free_cities[i] for i in free_cities], #need to add so only occupied free_cities are avaliable to be moved to
    action = founded_city)

leave_button = Button(position = (create_list_button.right + 30, 30), 
    title = "Leave City", 
    action = leave_city, 
    style = 'cancel') 

join_list_button.enabled = 0
create_list_button.enabled = 0

def refresh_buttons():
    global join_button
    global join_list_button
    global create_button
    global create_list_button
    global leave_button

    join_button = Button(position = (30, 30), 
        title = "Join City", 
        action = occupied_city_list, 
        style = 'cancel')

    join_list_button = ListButton(position = (30, join_button.bottom + 30), 
        titles = ["Move to %s" % taken_cities[i] for i in taken_cities], #need to add so only occupied free_cities are avaliable to be moved to
        action = joined_city)

    # create_button for creating a city

    create_button = Button(position = (join_list_button.right + 30, 30),
        title = "Create City", 
        action = empty_city_list, 
        style = 'cancel')

    #button 4 for list of not yet created free_cities

    create_list_button = ListButton(position = (join_list_button.right + 30, create_button.bottom + 30), 
        titles = ["Found %s" % free_cities[i] for i in free_cities], #need to add so only occupied free_cities are avaliable to be moved to
        action = founded_city)

    leave_button = Button(position = (create_list_button.right + 30, 30), 
        title = "Leave City", 
        action = leave_city, 
        style = 'cancel')   

    create_window() 

class TestWindow(Window):

    def mouse_down(self, event):
        say(self.name, "Mouse down:", event)
    
    def mouse_drag(self, event):
        say(self.name, "Mouse drag:", event)
    
    def mouse_up(self, event):
        say(self.name, "Mouse up:", event)
        print
    
    def key_down(self, event):
        say(self.name, "Key down:", event)

    def key_up(self, event):
        say(self.name, "Key up:", event)
        print

def create_window():
    window.add(join_button)
    window.add(join_list_button)
    window.add(create_button)
    window.add(create_list_button)
    window.add(leave_button)
    window.show()

def remove_window():
    window.remove(join_button)
    window.remove(join_list_button)
    window.remove(create_button)
    window.remove(create_list_button)
    window.remove(leave_button)


window = TestWindow(title = "Chatcity!", 
    bounds = (50, 70, 1800, 800),
    auto_position = False)

create_window()


application().run()
