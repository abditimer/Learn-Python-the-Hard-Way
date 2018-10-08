#High level overview of the classess needed:

#Map: map controls the scenes you go into
#	-next_scene
#	-opening_scene
#Engine
	#-play
#Scene: scene class that have that entire scene.
#   -enter: enter function that lets you enter the room
	#Death
	#Central Corridor
	#Laser weapon armory
	#the bridge
	#escape pod

###
#Game Title:   Gothons from Planet Percal #25
###


from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement the error()."
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n----------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):
	def enter(self):
		print ("You are on an alient spaceship. There is an alien infront of you")
		print ("What do you do? Do you shoot, dodge or tell a joke?")
		action = raw_input(">")

		if action == "shoot":
			print "You cant kill no gothon. He shoots you first and eats you."
			return 'death'
		elif action == 'dodge':
			print "Gothon stomps on you, you die...and then he eats you."
			return 'death'
		elif action == 'tell a joke':
			print "you made the gothon laugh! Then you shoot him in his ugly face."
			print "Congrats, you now run into the weapons room!"
			return 'laser_weapon_armory'
		else:
			print "DOES NOT COMPUTE"
			return "central_corridor"


class LaserWeaponArmory(Scene):

	def enter(self):
		print "guess the password to remove the neutron bomb."
		print "Get the code right...."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]>")
		guesses = 0
		while guess != code and guesses < 10:
			print "BZZZZZEED"
			guesses += 1
			guess = raw_input("[keypad]>")

		if guess == code:
			print "You did it! Now run to the bridge and place it!"
			return 'the_bridge'
		else:
			print "Too late..."
			return 'death'

class TheBridge(Scene):

	def enter(self):
		print "You are now on the bridge, with some Goftons. What do you do?"
		print "Do you throw the bomb or slowly place the bomb?"

		action = raw_input("> ")

		if action == "throw the bomb":
			print "Too bad, the bomb goes off."
			return 'death'
		elif action == "slowly place the bomb":
			print "you place the bomb and slowly move towards the lift."
			print "you point your weapon at the bomb as you jump in the lift and close it"
			print "you've escaped, and you're now on the way to the escape pods."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE"
			return "the_bridge"

class EscapePod(Scene):

	def enter(self):
		print "pick a pod to escape, some are damaged."

		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")

		if int(guess) != good_pod:
			print "Your pod blew up."
			return 'death'
		else:
			print "You made it! The aliens all died."
			return 'finished'

class Map(object):
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()




















