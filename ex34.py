from sys import exit

def gold_room():
	print "This room is full of gold. How much did you take?"

	next = raw_input("> ")
	
	#if "0" in next or "1" in next:
	#	how_much = int(next)
	#else:
	#	dead("Bro, type a number!")
	
	
	try:
		how_much = int(next)
	except ValueError:
		pass #its a string mate. try again
		dead('bro, type a number.')
	
	
		
	
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
	else:
		dead("You greedy scum.")
		
def bear_room():
	print """
There is a bear here.
The bear has a lot of honey.
The fat bear is in front of another door.
How are you going to move the bear?
You can either:
	- Take honey from bear.
	- taunt the bear.
	- open the door regardless.
"""
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "Take honey":
			dead("The bear looks at you, then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("Left or right?:  ")
	
	if next == "left" or next == "Left":
		bear_room()
	elif next == "right" or next == "Right":
		cthulhu_room()
	else:
		dead("You stumbled around the room untill you died.")
		
start()