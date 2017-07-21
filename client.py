#copied Socket Client segement 
import socket
#s = socket.socket()
#host = socket.gethostname()
#port = 9999
#address = (host, port)
#msg = 'test 123'
#s.connect(address)
#s.send(msg)

from GUI import Window, Button, Font, ListButton, application, TextField
from GUI.StdFonts import system_font
from GUI.StdColors import red, black
from testing import say

free_cities = ["Detorit" , "Montreal", "Vancouver", "Victoria", "Calgary", "Edmonton", "Quebec City", "Ottawa", "Toronto", "Winipeg", "Churchill", "Saskatoon", "Regina", "Yellowknife", "Whitehorse", "Dawson City", "Fort Simson", "Iqaluit", "Resolute", "Fredrickton", "Saint John", "Halifax", "Dartmouth", "St. Johns", "Grand Falls-Windsor", "Charlottetown", "Summerside"]

taken_cities = []

current_city = "Earth"

def founded_city(): #possibly consider making a function for disabling buttons to reduce code copyingg
    global free_room_counter
    global free_cities
    global taken_cities
    global current_city
    current_city = free_cities[create_list_button.value]
    print "Founded the city of", current_city
    taken_cities.append(current_city)
    del free_cities[create_list_button.value]
    remove_window()
    refresh_buttons()
    #DEBUG print taken_cities
    #DEBUG print free_cities
    create_list_button.enabled = 0
    join_list_button.enabled = 0
    join_button.enabled = 0
    create_button.enabled = 0

def joined_city():
    global free_room_counter
    global free_cities
    global taken_cities
    global current_city
    current_city = taken_cities[join_list_button.value]
    print "Moved to the city of", current_city
    remove_window()
    refresh_buttons()
    join_list_button.enabled = 0
    create_list_button.enabled = 0
    join_button.enabled = 0
    create_button.enabled = 0
    #DEBUG print taken_cities
    #DEBUG print free_cities

def empty_city_list():
    create_list_button.enabled = 1

def occupied_city_list(): # enables the list 
    join_list_button.enabled = 1

def leave_city():
    join_button.enabled = 1
    create_button.enabled = 1

def send_message():
    pass

join_button = Button(position = (30, 30), 
        title = "Join City", 
        action = occupied_city_list, 
        style = 'cancel')

join_list_button = ListButton(position = (30, join_button.bottom + 30), 
    titles = ["Move to %s" % i for i in taken_cities], #need to add so only occupied free_cities are avaliable to be moved to
    action = joined_city)

    # create_button for creating a city

create_button = Button(position = (300, 30),
    title = "Create City", 
    action = empty_city_list, 
    style = 'cancel')

    #button 4 for list of not yet created free_cities

create_list_button = ListButton(position = (300, create_button.bottom + 30), 
    titles = ["Found %s" % i for i in free_cities], #need to add so only occupied free_cities are avaliable to be moved to
    action = founded_city)

leave_button = Button(position = (600, 30), 
    title = "Leave City", 
    action = leave_city, 
    style = 'cancel') 

send_button = Button(position = (550,600),
    title = "Send Message",
    action = send_message,
    style = 'default')

join_list_button.enabled = 0
create_list_button.enabled = 0

def refresh_buttons():
    global join_button
    global join_list_button
    global create_button
    global create_list_button
    global leave_button
    global free_cities
    global taken_cities

    join_button = Button(position = (30, 30), 
        title = "Join City", 
        action = occupied_city_list, 
        style = 'cancel')

    join_list_button = ListButton(position = (30, join_button.bottom + 30), 
        titles = ["Move to %s" % i for i in taken_cities], #need to add so only occupied free_cities are avaliable to be moved to
        action = joined_city)

    # create_button for creating a city

    create_button = Button(position = (300, 30),
        title = "Create City", 
        action = empty_city_list, 
        style = 'cancel')

    #button 4 for list of not yet created free_cities

    create_list_button = ListButton(position = (300, create_button.bottom + 30), 
        titles = ["Found %s" % i for i in free_cities], #need to add so only occupied free_cities are avaliable to be moved to
        action = founded_city)

    leave_button = Button(position = (600, 30), 
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

class TestTextField(TextField):

    def __init__(self, number, *args, **kwds):
        TextField.__init__(self, *args, **kwds)
        self.number = number
    
    def do_text_changed_action(self):
        print "Field %s text changed" % self.number
    
    def targeted(self):
        print "Field %s targeted" % self.number

    def untargeted(self):
        print "Field %s untargeted" % self.number

def create_window():
    window.add(join_button)
    window.add(join_list_button)
    window.add(create_button)
    window.add(create_list_button)
    window.add(leave_button)
    window.add(window.input_field)
    window.add(window.output_field)
    window.add(window.room_field)
    window.add(send_button)
    window.show()

def remove_window():
    window.remove(join_button)
    window.remove(join_list_button)
    window.remove(create_button)
    window.remove(create_list_button)
    window.remove(leave_button)


window = TestWindow(title = "Chatcity!", 
    bounds = (50, 70, 900, 800),
    auto_position = False)

window.input_field = TestTextField(1, #input
    position = (30, 600),
    width = 600)

window.output_field = TestTextField(2, #output
    position = (30, 200),
    width = 700,
    height = 400,
    editable = False,
    value = "Read Only") # have value change with input from other people 

window.room_field = TestTextField(3,
    position = (30, 170),
    width = 100,
    editable = False,
    value = "curent_city")

create_window()


application().run()
