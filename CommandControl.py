import socket
import sys

# COMMANDS
# - Join room
# - Leave room
# - Create room
# - Delete room
# - List rooms
# - List users
# - Block user
# - Unblock user
# - Quit
# - Server shutdown
# - Help

QUIT_COMMAND = "/QUIT"

SHUTDOWN_COMMAND = "/SHUTDOWN"

class Earth:
	def __init__(self):
		self.cities = {}
		self.world_map = {}

	def list_rooms(self, user):
		city_list = "Current cities:\n"
		for city in self.cities
			city_list += city + "| Population: " + len(self.cities[city].users)
		user.socket.sendall(cities)

	def create_room(self, user, room):

	def delete_room(self, user, room):

	def list_users(self, user, room):

	def change_alias(self, user, new_alias):
		user.alias = new_alias

	def block_user(self, user, bl_user):

	def unblock_user(self, user, bl_user):

	def help(self, user):
		help_message = "Everyone needs help once in a while!\n"\
					 + "Here are the currently supported commands:\n"\
					 + "[/ALIAS] - Changes your alias. Be who you want to be!\n"\
					 + "[/MOVECITY city_name] - Move to a new city and make some new friends!\n"\
					 + "[/FOUNDCITY city_name] - Create a new city to meet new people!\n"\
					 + "[/LEAVECITY] - Take a vacation. Don't forget to say goodbye!\n"\
					 + "[/DESTROYCITY] - Nukes a city. You can only do this is you're the creator.\n"\
					 + "[/LISTCITIES] - Lists all cities on Earth and displays their population.\n"\
					 + "[/LISTUSERS] - Lists all users in room you're currently in\n"\
					 + "[/BLOCK] - Blocks the desired user. You won't hear a peep from them no more!\n"\
					 + "[/UNBLOCK] - Unblocks the desired user. Let there be speech!\n"\
					 + "[/HELPME] - Repeats this help message.\n"

		user.socket.sendall(help_message)

	def handler(self, user, message):
		print("[" + user.alias + "]: " + message)

class City:
	def __init__(self, name):
		self.user_list = []
		self.name = name

	def broadcast(self, user, message):
		message = "[" + user.alias + "]: " + message
		for user in self.user_list:
			user.socket.sendall(message)

class User:
	def __init__(self, socket, alias = "Anonymous"):
		socket.setblocking(0)
		self.alias = alias