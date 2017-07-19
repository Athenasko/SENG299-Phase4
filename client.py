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

cities = ["Detorit" , "Montreal", "Vancouver", "Victoria", "Calgary", "Edmonton", "Quebec City", "Ottawa", "Toronto", "Winipeg", "Churchill", "Saskatoon", "Regina", "Yellowknife", "Whitehorse", "Dawson City", "Fort Simson", "Iqaluit", "Resolute", "Fredrickton","Saint John", "Halifax", "Dartmouth", "St. Johns", "Grand Falls-Windsor", "Charlottetown", "Summerside"]

def occupied_city_list(): # enables the list 
    btn2.enabled = 1

def empty_city_list():
    btn4.enabled = 1

def founded_city():
    btn4.enabled = 0
    btn2.enabled = 0

def joined_city():
    btn2.enabled = 0
    btn4.enabled = 0

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

join_button = Button(position = (30, 30), 
    title = "Join City", action = occupied_city_list, style = 'cancel')

join_list_button = ListButton(position = (30, join_button.bottom + 30), 
    titles = ["Move to %s" % i for i in cities], #need to add so only occupied cities are avaliable to be moved to
    action = joined_city)

# btn3 for creating a city

btn3 = Button(position = (btn2.right + 30, 30),
    title = "Create City", action = empty_city_list, style = 'cancel')

#button 4 for list of not yet created cities

btn4 = ListButton(position = (btn2.right + 30, btn3.bottom + 30), 
    titles = ["Found %s" % i for i in cities], #need to add so only occupied cities are avaliable to be moved to
    action = founded_city)


win = Window(title = "List Button")

window = TestWindow(title = "Chatcity!", 
    bounds = (50, 70, 1800, 800),
    auto_position = False)

btn2.enabled = 0
btn4.enabled = 0

window.add(join_button)
window.add(btn2)
window.add(btn3)
window.add(btn4)
window.show()



application().run()
