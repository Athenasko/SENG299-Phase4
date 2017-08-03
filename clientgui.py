#PUT DOCCUMENTATION HERE 

import re
import socket
import os, sys
import threading
import select
import time
import Queue
from GUI import Window, Button, Font, ListButton, application, TextField, View, Image
from GUI.Geometry import offset_rect, rect_sized
from GUI.StdFonts import system_font
from GUI.StdColors import red,black,yellow,blue 
from testing import say

#if(len(sys.argv) < 3): #MIGHT STILL WANT ALL OF THIS
# print 'Usage : python chat_client.py hostname port'
# sys.exit()
#host = sys.argv[1] #MIGHT STILL WANT TO IMPLEMENT THIS FOR SYSTEM 
#port = int(sys.argv[2])

#ALL THE GLOBAL STUFF

supertestcounter = 1
sending = 0
received = ""
MAX_SEND_LEN = 69
MAX_LINE = 22
line_counter = 0
received_city = ""
received_alias = ""
message_queue = Queue.Queue()
temp_message_queue = Queue.Queue()

#list of all the different chat rooms - 2 of each city per province + Detroit
free_cities = ["Detroit" , "Montreal", "Vancouver", "Victoria", "Calgary", "Edmonton", "Quebec City", "Ottawa", "Toronto", "Winnipeg", "Churchill", "Saskatoon", "Regina", "Yellowknife", "Whitehorse", "Dawson City", "Fort Simson", "Iqaluit", "Resolute", "Fredericton", "Saint John", "Halifax", "Dartmouth", "St. Johns", "Grand Falls-Windsor", "Charlottetown", "Summerside"]
Alias_MAX = 10 #
test_counter = 1
current_city = "Earth" #Default chatroom for the system, also acts as global message sender
current_alias = "Anonymus" #Default alias for the alias system

#ALL THE PATHING FOR SWITCHING THE BACKGROUND FOR EACH CHAT ROOM
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



#MULTITHREADING

class clientThread (threading.Thread): #Thread for running client - server communication behind GUI
  def __init__(self, threadID, name, counter):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.counter = counter
  def run(self):
    print "Starting " + self.name
    chat_client("localhost",6969)
    print "Exiting " + self.name




#CHAT CLIENT FOR BOGO TO BOGO CONNECTION TO SERVER

def chat_client(host,port):
  #testlock2.acquire()
  global testlock
  global threadtest
  global supertestcounter
  global sending
  global window
  global received
  global received_city
  global received_alias
     
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.settimeout(2)
     
  #connect to remote host
  try:
    server_socket.connect((host, port))
  except:
    print 'Unable to connect'
    sys.exit()
     
  print 'Connected to remote host. You can start sending messages'
  
  socket_list = [sys.stdin, server_socket]
  

  while 1:
    socket_list = [server_socket]
    supertestcounter += 1
    #Get the list sockets which are readable
    ready_for_reading, ready_for_writing, error_condition = select.select(socket_list , [], [], 0)  
    for sock in ready_for_reading:  

      if sock == server_socket: #incoming message from remote server, server_socket
        data = sock.recv(4096)
        if not data:
          sys.exit()
        else:
          
          tempdata = data
          received = re.findall('\((.*?)\)',tempdata) # core message
          tempdata = data
          received_city = re.findall('\{(.*?)\}',tempdata) # message city
          tempdata = data
          received_alias = re.findall('\[(.*?)\]',tempdata) # message alias 
    
          refresh_output_receive()
          pass 
            
      else:
  
        pass 

    if sending == 1: #user entered a message
      message_data = '{' + current_city + '}' +  '[' + current_alias + ']' + '(' + window.input_field.text + ')' #+ '\n'
      server_socket.send(message_data)
      refresh_output_send()
      sending = 0;




#GUI CODE USING PYGUI


#ALL THE CORE FUNCTIONS FOR BUTTON USAGE

def joined_city(): #Joining chatrooms
    global free_room_counter
    global free_cities
    global taken_cities
    global current_city
    global line_counter
    current_city = free_cities[join_list_button.value]
    switch_background()
    remove_window()
    refresh_buttons()
    join_list_button.enabled = 0
    line_counter = 0
    join_button.enabled = 0
    leave_button.enabled = 1

def occupied_city_list(): # enables the list button for changing rooms
    join_list_button.enabled = 1

def leave_city(): #leaving chatrooms for the default main room
    global current_city
    global line_counter
    current_city = "Earth"
    switch_background()
    remove_window()
    refresh_buttons()
    join_button.enabled = 1
    line_counter = 0
#    create_button.enabled = 1
    join_list_button.enabled = 0
#    create_list_button.enabled = 0
    leave_button.enabled = 0
   
def send_message(): #need to implement 
    global sending
    global MAX_SEND_LEN
    global line_counter
    global MAX_LINE
    #global window
    #window.output_field.value = window.output_field_text + window.input_field.text + '/n'
    #remove_window()
    
    if len(window.input_field.text) > MAX_SEND_LEN:
      print("Message too long") #will want to move to error dialog box 
    elif line_counter > MAX_LINE:
      pass
    else:
      sending = 1
      #refresh_output_send()

def change_alias(): #need to implement 
  global current_alias
  global Alias_MAX
  if len(window.alias.text) > Alias_MAX:
    print("Name too long")
    pass #needs to pop up dialog telling them it wont work
  else:
    current_alias = window.alias.text 
  remove_window()
  #refresh_buttons()
  refresh_buttonsv2()
  pass

#Code to check city tags and change the pathing for the background image
def switch_background():
    global current_city
    global view
    global background_image
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
    view = ImageView(size = window.size)
 
def test(): #Testing the sending of shared data between the threads - this is where we discovered the Python GIL killed the system
  global threadtest
  global testlock
  global supertestcounter
  global received_alias
  global received_city
  global received
  print supertestcounter
  print received_alias
  print received_city
  print received

def queue_refresh(message):
  global message_queue
  global temp_message_queue
  global line_counter
  for i in range(0,1):
    discard = message_queue.get()
    line_counter -= 1
  window.output_field.value = ""
  while not message_queue.empty():
    pop = message_queue.get()
    temp_message_queue.put(pop)
    print "DEBUG"
    window.output_field.value = window.output_field.text + pop + '\n'
  while not temp_message_queue.empty():
    message_queue.put(temp_message_queue.get())
  message_queue.put(message)
  window.output_field.value = window.output_field.text + message + '\n'

def refresh_output_receive():
    global received
    global window
    global test_counter
    global MAX_LINE
    global line_counter
    global received_city
    global received_alias
    global message_queue
    global temp_message_queue

    if len(received_city)<=0:
        pass
    else:
        if received_city[0] == current_city or received_city[0] == "Earth":
          temp_message = '[' + received_alias[0] + '] ' + received[0]
          line_counter += 1
          print line_counter
          if line_counter >= MAX_LINE:
            queue_refresh(temp_message)
            print "Too many lines" #This is where we'd have to figure out how to remove the lines
          else: 
            message_queue.put(temp_message)
            window.output_field.value = window.output_field.text + temp_message + '\n'
            remove_window()
            create_window()

def refresh_output_send():
    global received
    global window
    global test_counter
    global MAX_LINE
    global line_counter
    global message_queue
    global temp_message_queue
    line_counter += 1
    temp_sending = '[' + current_alias + '] ' +  window.input_field.text
    print line_counter
    if line_counter >= MAX_LINE:
      queue_refresh(temp_sending)
      print "Too many lines" # - same thing as the recieving
    else:
      message_queue.put(temp_sending)
      window.output_field.value = window.output_field.text + temp_sending + '\n'
    remove_window()
    create_window()


#ALL THE BUTTONS 

join_button = Button(position = (30, 30), 
        title = "Join City", 
        action = occupied_city_list, 
        style = 'cancel')

join_list_button = ListButton(position = (30, join_button.bottom + 30), 
    titles = ["Move to %s" % i for i in free_cities], #need to add so only occupied free_cities are avaliable to be moved to
    action = joined_city)

leave_button = Button(position = (600, 30), 
    title = "Leave City", 
    action = leave_city, 
    style = 'cancel') 

send_button = Button(position = (610,690),
    title = "Send Message",
    action = send_message,
    style = 'cancel')

alias_button = Button(position = (600, join_button.bottom + 30),
  title = "Change alias",
  action = change_alias,
  style = 'cancel')


mail_button = Button(position = (600, alias_button.bottom + 30),
 title = "Check Mailbox",
 action = test,
 style = 'cancel')

join_list_button.enabled = 0
leave_button.enabled = 0


#REFRESH FUNCTIONS 

def refresh_buttons():

  window.alias = TestTextField(5, #consider condensing this with the alias textfield, and add phrase such as alias currently resides in city
    position = (405, join_button.bottom + 30),
    width = 200,
    value = current_alias)

  window.input_alias = TestTextField(6, #consider condensing this with the alias textfield, and add phrase such as alias currently resides in city
    position = (30, 690),
    width = (len(current_alias) + 2) * 8,
    editable = False,
    value = current_alias + ":")

  window.input_field = TestTextField(1, #input
    position = (window.input_alias.right - 5, 690),
    width = 580-(len(current_alias)+2)*8)

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
    value = "Welcome to " + current_city + "\n") # have value change with input from other people 

  create_window() 

def refresh_buttonsv2():

  window.alias = TestTextField(5, #consider condensing this with the alias textfield, and add phrase such as alias currently resides in city
    position = (405, join_button.bottom + 30),
    width = 200,
    value = current_alias)

  window.input_alias = TestTextField(6, #consider condensing this with the alias textfield, and add phrase such as alias currently resides in city
    position = (30, 690),
    width = (len(current_alias) + 2) * 8,
    editable = False,
    value = current_alias + ":")

  window.input_field = TestTextField(1, #input
    position = (window.input_alias.right - 5, 690),
    width = 580-(len(current_alias)+2)*8)

  window.room_field = TestTextField(3,
    position = (30, 260),
    width = 300,
    editable = False,
    value = current_alias + " currently resides in " + current_city)

  create_window() 

# WINDOW VIEWS AND REFRESH FUNCTIONS

class TestTextField(TextField):

    def __init__(self, number, *args, **kwds):
        TextField.__init__(self, *args, **kwds)
        self.number = number

class ImageView(View):

    def draw(self, c, r):
        c.backcolor = blue
        c.erase_rect(r)
        main_image_pos = (20, 10)
        src_rect = rect_sized((10,10), (700,260))
        dst_rect = offset_rect(src_rect, main_image_pos)
        background_image.draw(c, src_rect, dst_rect)

def create_window(): #USED to create and later readd buttons and views to the window
    window.add(view)
    window.add(join_button)
    window.add(join_list_button)
    window.add(leave_button)
    window.add(window.input_field)
    window.add(window.output_field)
    window.add(window.room_field)
    window.add(send_button)
    window.add(mail_button)
    window.add(window.alias)
    window.add(window.alias_title)
    window.add(alias_button)
    window.add(window.input_alias)
    window.show()

def remove_window(): #Used to remove all the buttons and views for refresh
    window.remove(view)
    window.remove(join_button)
    window.remove(join_list_button)
    window.remove(leave_button)
    window.remove(window.room_field)
    window.remove(window.input_field)
    window.remove(window.output_field)
    window.remove(window.room_field)
    window.remove(send_button)
    window.remove(alias_button)
    window.remove(window.alias_title)
    window.remove(window.input_alias)
    window.remove(mail_button)
    window.remove(window.alias)


#WINDOW AND FIELD CREATION

window = Window(title = "Chatcity!", 
    bounds = (50, 70, 810, 800),
    auto_position = False,
    resizable = 0)

view = ImageView(size = window.size)

print len(current_alias)

window.input_alias = TestTextField(6, #consider condensing this with the alias textfield, and add phrase such as alias currently resides in city
    position = (30, 690),
    width = (len(current_alias) + 2) *8,
    editable = False,
    value = current_alias + ":")

window.input_field = TestTextField(1, #input
    position = (window.input_alias.right-5, 690),
    width = 580-(len(current_alias)+2)*8)

window.output_field = TestTextField(2, #output
    position = (30, 290),
    width = 700,
    height = 400,
    editable = False,
    value = "Welcome to " + current_city + '\n') #Testing overflow #+ "DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG ") # have value change with input from other people 

window.room_field = TestTextField(3,
    position = (30, 260),
    width = 300,
    editable = False,
    value = current_alias + " currently resides in " + current_city) 

window.alias_title = TestTextField(4, #consider condensing this with the alias textfield, and add phrase such as alias currently resides in city
    position = (290, join_button.bottom + 30),
    width = 120,
    editable = False,
    value = "Your current alias:")

window.alias = TestTextField(5, #consider condensing this with the alias textfield, and add phrase such as alias currently resides in city
    position = (405, join_button.bottom + 30),
    width = 200,
    value = current_alias)



#THREAD CREATION AND APPLICATION RUNNING

thread1 = clientThread(1, "Thread-1", 1)
thread1.start()
create_window()
application().run()



