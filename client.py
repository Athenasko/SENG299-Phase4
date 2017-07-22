#copied Socket Client segement 
#s = socket.socket()
#host = socket.gethostname()
#port = 9999
#address = (host, port)
#msg = 'test 123'
#s.connect(address)
#s.send(msg)

import socket
import os, sys
from GUI import Window, Button, Font, ListButton, application, TextField, View, Image
from GUI.Geometry import offset_rect, rect_sized
from GUI.StdFonts import system_font
from GUI.StdColors import red,black,yellow,blue 
from testing import say

free_cities = ["Detroit" , "Montreal", "Vancouver", "Victoria", "Calgary", "Edmonton", "Quebec City", "Ottawa", "Toronto", "Winnipeg", "Churchill", "Saskatoon", "Regina", "Yellowknife", "Whitehorse", "Dawson City", "Fort Simson", "Iqaluit", "Resolute", "Fredericton", "Saint John", "Halifax", "Dartmouth", "St. Johns", "Grand Falls-Windsor", "Charlottetown", "Summerside"]
taken_cities = []

current_city = "Earth"
current_alias = "Bob"

here = sys.path[0]
image_path = os.path.join(here, "earth_background.jpg")
calgary_path = os.path.join(here, "Calgary_background.jpg")
charlottetown_path = os.path.join(here, "charlottetown_background.jpg")
churchill_path = os.path.join(here, "churchill_background.jpg")
dartmouth_path = os.path.join(here, "dartmouth_background.jpg")
dawson_path = os.path.join(here, "Dawson_city_background.jpg")
detroit_path = os.path.join(here, "detroit_background.jpg")
edmonton_path = os.path.join(here, "Edmonton_background.jpg")
simson_path = os.path.join(here, "Fort_simson_background.jpg")
fredericton_path = os.path.join(here, "fredericton_background.jpg")
windsor_path = os.path.join(here, "Grand_falls_windsor_background.jpg")
halifax_path = os.path.join(here, "Halifax_background.jpg")
iqaluit_path = os.path.join(here, "iqaluit_background.jpg")
montreal_path = os.path.join(here, "Montreal_background.jpg")
ottawa_path = os.path.join(here, "Ottawa_background.jpg")
quebec_path = os.path.join(here, "quebec_background.jpg")
regina_path = os.path.join(here, "regina_background.jpg")
resolute_path = os.path.join(here, "Resolute_background.jpg")
saint_path = os.path.join(here, "saint_john_background.jpg")
saskatoon_path = os.path.join(here, "saskatoon_background.jpg")
john_path = os.path.join(here, "st_john's_background.jpg")
summerside_path = os.path.join(here, "summerside_background.jpg")
toronto_path = os.path.join(here, "Toronto_background.jpg")
vancouver_path = os.path.join(here, "vancouver_background.jpg")
victoria_path = os.path.join(here, "Victoria_background.jpg")
whitehorse_path = os.path.join(here, "whitehorse_background.jpg")
winnipeg_path = os.path.join(here, "winnipeg_background.jpg")
yellowknife_path = os.path.join(here, "yellowknife_background.jpg")
background_image = Image(file = image_path)


def founded_city(): #possibly consider making a function for disabling buttons to reduce code copyingg
    global free_room_counter
    global free_cities
    global taken_cities
    global current_city
    current_city = free_cities[create_list_button.value]
    print "Founded the city of", current_city
    switch_background()
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
    leave_button.enabled = 1

def joined_city():
    global free_room_counter
    global free_cities
    global taken_cities
    global current_city
    current_city = taken_cities[join_list_button.value]
    print "Moved to the city of", current_city
    switch_background()
    remove_window()
    refresh_buttons()
    join_list_button.enabled = 0
    create_list_button.enabled = 0
    join_button.enabled = 0
    create_button.enabled = 0
    leave_button.enabled = 1
    #DEBUG print taken_cities
    #DEBUG print free_cities

def empty_city_list():
    create_list_button.enabled = 1

def occupied_city_list(): # enables the list 
    join_list_button.enabled = 1

def leave_city():
    global current_city
    current_city = "Earth"
    switch_background()
    remove_window()
    refresh_buttons()
    join_button.enabled = 1
    create_button.enabled = 1
    join_list_button.enabled = 0
    create_list_button.enabled = 0
    leave_button.enabled = 0
   
def send_message(): #need to implement 
    global window
    print "Debug " 
    print window.input_field.text
    print window.input_field

def switch_background():
    global current_city
    global view
    global background_image
    print current_city
    if current_city == "Calgary":
       background_image = Image(file = calgary_path)
    elif current_city == "Charlottetown":
       background_image = Image(file = charlottetown_path)
    elif current_city == "Churchill":
       background_image = Image(file = churchill_path)
    elif current_city == "Dartmouth":
       background_image = Image(file = dartmouth_path)
    elif current_city == "Dawson City":
       background_image = Image(file = dawson_path)
    elif current_city == "Detroit":
       background_image = Image(file = detroit_path)
    elif current_city == "Edmonton":
       background_image = Image(file = edmonton_path)
    elif current_city == "Fort Simson":
       background_image = Image(file = simson_path)
    elif current_city == "Fredericton":
       background_image = Image(file = fredericton_path)
    elif current_city == "Grand Falls-Windsor":
       background_image = Image(file = windsor_path)
    elif current_city == "Halifax":
       background_image = Image(file = halifax_path)
    elif current_city == "Iqaluit":
       background_image = Image(file = iqaluit_path)
    elif current_city == "Montreal":
       background_image = Image(file = montreal_path)
    elif current_city == "Ottawa":
       background_image = Image(file = ottawa_path)
    elif current_city == "Quebec City":
       background_image = Image(file = quebec_path)
    elif current_city == "Regina":
       background_image = Image(file = regina_path)
    elif current_city == "Resolute":
       background_image = Image(file = resolute_path)
    elif current_city == "Saint John":
       background_image = Image(file = saint_path)
    elif current_city == "Saskatoon":
       background_image = Image(file = saskatoon_path)
    elif current_city == "St. Johns":
       background_image = Image(file = john_path)
    elif current_city == "Summerside":
       background_image = Image(file = summerside_path)
    elif current_city == "Toronto":
       background_image = Image(file = toronto_path)
    elif current_city == "Vancouver":
       background_image = Image(file = vancouver_path)
    elif current_city == "Victoria":
       background_image = Image(file = victoria_path)
    elif current_city == "Whitehorse":
       background_image = Image(file = whitehorse_path)
    elif current_city == "Winnipeg":
       background_image = Image(file = winnipeg_path)
    elif current_city == "Yellowknife":
       background_image = Image(file = yellowknife_path)
    else:
        background_image = Image(file = image_path)
    view = ImageTestView(size = window.size)
    print "changed the view"
    pass
 
    #view = ImageTestView(size = window.size)


join_button = Button(position = (30, 30), 
        title = "Join City", 
        action = occupied_city_list, 
        style = 'cancel')

join_list_button = ListButton(position = (30, join_button.bottom + 30), 
    titles = ["Move to %s" % i for i in taken_cities], #need to add so only occupied free_cities are avaliable to be moved to
    action = joined_city)

create_button = Button(position = (300, 30), # create_button for creating a city
    title = "Create City", 
    action = empty_city_list, 
    style = 'cancel')

create_list_button = ListButton(position = (300, create_button.bottom + 30), #button 4 for list of not yet created free_cities
    titles = ["Found %s" % i for i in free_cities], #need to add so only occupied free_cities are avaliable to be moved to
    action = founded_city)

leave_button = Button(position = (600, 30), 
    title = "Leave City", 
    action = leave_city, 
    style = 'cancel') 

send_button = Button(position = (610,690),
    title = "Send Message",
    action = send_message,
    style = 'cancel')

join_list_button.enabled = 0
create_list_button.enabled = 0
leave_button.enabled = 0

def refresh_buttons():
    global join_button
    global join_list_button
    global create_button
    global create_list_button
    global leave_button
    global free_cities
    global taken_cities
    global window

    join_button = Button(position = (30, 30), 
        title = "Join City", 
        action = occupied_city_list, 
        style = 'cancel')

    join_list_button = ListButton(position = (30, join_button.bottom + 30), 
        titles = ["Move to %s" % i for i in taken_cities], #need to add so only occupied free_cities are avaliable to be moved to
        action = joined_city)

    create_button = Button(position = (300, 30),
        title = "Create City", 
        action = empty_city_list, 
        style = 'cancel')

    create_list_button = ListButton(position = (300, create_button.bottom + 30), 
        titles = ["Found %s" % i for i in free_cities], #need to add so only occupied free_cities are avaliable to be moved to
        action = founded_city)

    leave_button = Button(position = (600, 30), 
        title = "Leave City", 
        action = leave_city, 
        style = 'cancel')   

    window.room_field = TestTextField(3,
    position = (30, 260),
    width = 300,
    editable = False,
    value = current_alias + " currently resides in " + current_city)

    window.output_field = TestTextField(2, #output
    position = (30, 290),
    width = 700,
    height = 400,
    editable = False,
    value = "Welcome to " + current_city) # have value change with input from other people 

    create_window() 

def refresh_output(): #going to require this to constantly feed the output from the server to the user
    global window
    window.output_field.text = window.output_field.text # + latest output 
    pass

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

class ImageTestView(View):

    def draw(self, c, r):
        c.backcolor = blue
        c.erase_rect(r)
        main_image_pos = (20, 10)
        src_rect = rect_sized((10,10), (700,260))
        #src_rect = rect_sized((180, 160), (100, 100))
        dst_rect = offset_rect(src_rect, main_image_pos)
        #dst_rect = rect_sized((10, 340), (150, 150))
        #dst_rect = rect_sized((200, 340), (100, 100))
        #dst_rect = rect_sized((10, 10), (800, 790))
        background_image.draw(c, src_rect, dst_rect)

def create_window():
    window.add(view)
    window.add(join_button)
    window.add(join_list_button)
    window.add(create_button)
    window.add(create_list_button)
    window.add(leave_button)
    window.add(window.input_field)
    window.add(window.output_field)
    window.add(window.room_field)
    window.add(send_button)
    #window.add(window.alias)
    window.show()

def remove_window():
    window.remove(view)
    window.remove(join_button)
    window.remove(join_list_button)
    window.remove(create_button)
    window.remove(create_list_button)
    window.remove(leave_button)
    window.remove(window.room_field)
    window.remove(window.input_field)
    window.remove(window.output_field)
    window.remove(window.room_field)
    window.remove(send_button)

window = TestWindow(title = "Chatcity!", 
    bounds = (50, 70, 810, 800),
    auto_position = False,
    resizable = 0)

view = ImageTestView(size = window.size)

window.input_field = TestTextField(1, #input
    position = (30, 690),
    width = 580)

window.output_field = TestTextField(2, #output
    position = (30, 290),
    width = 700,
    height = 400,
    editable = False,
    value = "Welcome to " + current_city + "DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG ") # have value change with input from other people 

window.room_field = TestTextField(3,
    position = (30, 260),
    width = 300,
    editable = False,
    value = current_alias + " currently resides in " + current_city)

#window.alias = TestTextField(4, #consider condensing this with the alias textfield, and add phrase such as alias currently resides in city
 #   position = (230, 170),
  #  width = 200,
   # editable = False,
    #value = current_alias)

create_window()


while(1):
	print ("DEBUG")

application().run()



