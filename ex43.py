#High level overview of the classess needed:

#Map
	#-next_scene
	#-opening_scene
#Engine
	#-play
#Scene
	#-enter
	#Death
	#Central Corridor
	#Laser weapon armory
	#the bridge
	#escape pod

###
#Game Title:   Gothons from Planet Percal #25
###


class Scene(object):
	def enter(self):
		pass


class Engine(object):
	#Starting the Engine.
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		#Player wants to play the game - launch
		self.scene_map.opening_scene()
		self.scene_map.next_scene(self.scene_map.start_scene)


#Each room does:
#1. Prints its own description
#2. tells engine what room to run next.



class Death(Scene):
	#Here player dies - funny death scenes (maybe cycle/randomise them.)
	def enter(self):
		print "Death room entered. You Died. Try again."




class CentralCorridor(Scene):
	#Here the player needs to defeat the user with a funny joke.
	def enter(self):
		print "You have enetered the Central Corridor."
		Death().enter()
		


class LaserWeaponArmory(Scene):
	#Neutron bomb is in this room. He needs to guess the pass key number or blows up.
	def enter(self):
		print('Well done, you have now entered the Weapons Room.')
		
class TheBridge(Scene):
	#battle scene where the hero must place the bomb
	def enter(self):
		print('Well done, you have now entered the Bridge Room.') 

class EscapePod(Scene):
	#hero must escape, but only after guessing the right escape pod.
	def enter(self):
		print('Well done, you have now entered the Evacuation Room.')






class Map(object):
	def __init__(self, start_scene):
		self.start_scene = start_scene

	#Pass the next scene and the map state changes
	def next_scene(self, sName):
		"""
		Depending where you are, go to the next room.
		"""
		if sName == 'central_corridor':
			CentralCorridor().enter()
		elif sName == 'Death':
			Death().enter()
		elif sName == 'LaserWeaponArmory':
			LaserWeaponArmory().enter()
		elif sName == 'TheBridge':
			TheBridge().enter()
		else:
			EscapePod().enter()

	def opening_scene(self):
		"""
		This scene introduces the player to the hero. The first time the user enters the game.
		"""
		print "Hello user. Welcome to the game. You will play a character caled:  Tim."




#The game involves an engine
#that runs a map full of scenes.

#Create a Map object that has a load of scenes.
a_map = Map('central_corridor')
#Start the game engine that has the map we created
a_game = Engine(a_map)
#Play.
a_game.play()




















