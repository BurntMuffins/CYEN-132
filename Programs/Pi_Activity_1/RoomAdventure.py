###########################################################################################
# Name: Aidan Schaubhut
# Date: 4/13/23
# Description: A room adventure game
# Additions:  - inspect command: Allows you to inspect items in your inventory.
#             - use command: Allows the user to use certain items in certain rooms.
# 			  - Different items, rooms, grabbables
###########################################################################################
from tkinter import *

filePath = "images/"
# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room:
	# the constructor
	def __init__(self, name, image):
		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits = {}
		self.items = {}
		self.grabbables = {}

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate dictionary
		self._items[item] = desc

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item, desc):
		# append the item to the list
		self._grabbables[item] = desc

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the dictionary
		del self._grabbables[item]

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
	# the constructor
	def __init__(self, parent):
		# call the constructor in the superclass
		Frame.__init__(self, parent)

	# creates the rooms
	def createRooms(self):
		r1 = Room("Kitchen", filePath+"kitchen.gif") 
		r2 = Room("Study", filePath+"study.gif") 
		r3 = Room("Bathroom", filePath+"bathroom.gif") 
		r4 = Room("Bedroom", filePath+"bedroom.gif") 

		## KITCHEN ##
		# exits for r1
		r1.addExit("study", r2)
		r1.addExit("bathroom", r3)

		# grabbables for r1
		r1.addGrabbable("key", 'A golden key with "Mirror" written on it')
		
		# items for r1
		r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
		r1.addItem("table", "It is made of oak. A golden key rests on it.")

		## STUDY ##
		# add exits for r2
		r2.addExit("kitchen", r1)
		r2.addExit("bedroom" ,r4)

		# add items to r2
		r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
		r2.addItem("desk", "There is a note on it.")

		# add grabables to r2
		r2.addGrabbable("note", "I can reflect your image,\nBut theres more to me than meets the eye.\nTo exit this house,\nLook behind me and you'll find the way to fly.")

		## BATHROOM ##
		# add exits to r3
		r3.addExit("kitchen", r1)
		r3.addExit("bedroom", r4)

		# add grabbables to r3
		r3.addGrabbable("book", 'An old tattered book')

		# add items to r3
		r3.addItem("sink", "Its kinda dirty.")
		r3.addItem("toilet", "I am definetly not looking in there.")
		r3.addItem("mirror", "a mirror with a key hole on it.")
		
		## BEDROOM ##
		# add exits to r4
		r4.addExit("study", r2)
		r4.addExit("bathroom", r3)
		r4.addExit("closet", None) # DEATH

		# add grabbables to r4
		r4.addGrabbable("bed", "Its shockingly well kept")
		r4.addItem("dresser", "Its falling apart")
		
		# set r1 as the current at the beginning of the game
		Game.currentRoom = r1
		Game.inventory = []


	# sets up the GUI
	def setupGUI(self):
		self.pack(fill=BOTH, expand=1)
		
		# user input stuff
		Game.player_input = Entry(self, bg="white")
		Game.player_input.bind("<Return>", self.process)
		Game.player_input.pack(side=BOTTOM, fill=X)
		Game.player_input.focus()

		# image on left
		img = None
		Game.image = Label(self, width=WIDTH//2, image=img)
		Game.image.image = img
		Game.image.pack(side=LEFT, fill=Y)
		Game.image.pack_propagate(False) # doesn't allow widget to determine size

		# text information on right
		text_frame = Frame(self, width=WIDTH//2)
		Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
		Game.text.pack(fill=Y, expand=1)
		text_frame.pack(side=RIGHT, fill=Y)
		text_frame.pack_propagate(False) # doesn't allow widget to determine size

	# sets the current room image
	def setRoomImage(self):
		if Game.currentRoom == None:
			Game.img = PhotoImage(file=filePath+"skull.gif")
		else:
			Game.img = PhotoImage(file=Game.currentRoom.image)
		
		# displaying the image on the left
		Game.image.config(image=Game.img)
		Game.image.image = Game.img

	# sets the status displayed on the right of the GUI
	def setStatus(self, status):
		Game.text.config(state=NORMAL)
		Game.text.delete("1.0", END)
		if (Game.currentRoom == None):
			# dead state
			Game.text.insert(END, "You are dead. The only thing you can do now is quit.\n")
		else:
			# display current room and other info
			inv_keys = [list(item.keys())[0] for item in Game.inventory]
			inv_str = ", ".join(inv_keys)
			Game.text.insert(END, f"{Game.currentRoom}\nYou are carrying: {inv_str}\n\n{status}")
		Game.text.config(state=DISABLED)

	# plays the game
	def play(self):
		# add the rooms to the game
		self.createRooms()
		# configure the GUI
		self.setupGUI()
		# set the current room
		self.setRoomImage()
		# set the current status
		self.setStatus("")

	# processes the player's input
	def process(self, event):
		# grab the player's input from the input at the bottom of the GUI
		action = Game.player_input.get()
		# set the user's input to lowercase to make it easier to compare the verb and noun to known values
		action = action.lower()
		# set a default response
		response = "I don't understand.  Try verb noun.  Valid verbs are go, look, and take"

		# exit the game if the player wants to leave (supports quit, exit, and bye)
		if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
			exit(0)

		# if the player is dead if goes/went south from room 4
		if (Game.currentRoom == None):
			# clear the player's input
			Game.player_input.delete(0, END)
			return

		# split the user input into words (words are separated by spaces) and store the words in a list
		words = action.split()

		# the game only understands two word inputs
		if (len(words) >= 2):
			# isolate the verb and noun
			verb = words[0]
			noun = words[1]

			# the verb is: go
			if (verb == "go"):
				# set a default response
				response = "Invalid exit."

				# check for valid exits in the current room
				if (noun in Game.currentRoom.exits):
					# if one is found, change the current room to the one that is associated with the specified exit
					Game.currentRoom = Game.currentRoom.exits[noun]
					# set the response (success)
					response = "Room changed."

			# the verb is: look
			elif (verb == "look"):
				# set a default response
				response = "I don't see that item."

				# check for valid items in the current room
				if (noun in Game.currentRoom.items):
					# if one is found, set the response to the item's description
					response = Game.currentRoom.items[noun]

			# the verb is: take
			elif (verb == "take"):
				# set a default response
				response = "I don't see that item."

				# check for valid grabbable items in the current room
				for grabbable in Game.currentRoom.grabbables:
					# a valid grabbable item is found
					if (noun == grabbable):
						# add the grabbable item to the player's inventory
						for item in Game.currentRoom.grabbables:
							if noun in item:
								Game.inventory.append({noun:Game.currentRoom.grabbables[noun]})
								# remove the grabbable item from the room
								Game.currentRoom.delGrabbable(grabbable)
								# set the response (success)
								response = "Item grabbed."
								# no need to check any more grabbable items
								break
						break

			# The verb is: inspect
			elif (verb == 'inspect'):
				# set the default response
				response = "You don't have that item in your inventory"

				# check for the vaild grabable in inventory
				for item in Game.inventory:
					# if a vaild item is found
					if noun in item:
						response = item[noun]

			# The verb is: use
			elif (verb == 'use'):
				if Game.currentRoom.name == "Bathroom":
					for item in Game.inventory:
						if noun in item.keys():
							# do something with the item
							response = "You opened the mirror!\
								\nYou found the secret riches hidden in the house!"
							break
					else:
						# the given noun is not in the inventory
						response = "You don't have that item in your inventory."
				else:
					# the player is not in the bathroom
					response = "There isn't a use for that here."
						
		# display the response on the right of the GUI
		# display the room's image on the left of the GUI
		# clear the player's input
		self.setStatus(response)
		self.setRoomImage()
		Game.player_input.delete(0, END)

##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()