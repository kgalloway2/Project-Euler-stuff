from random import randint

def generic_action_funtion(direction, paths):
    return paths.get(direction, None)

class Room(object):

    def __init__(self, name, description, action_function):
        self.name = name
        self.description = description
        self.paths = {}
        self.action_function = action_function

    def go(self, direction):
        return self.action_function(direction, self.paths)
        
    def add_paths(self, paths):
        self.paths.update(paths)

def central_corridor_action(direction, paths):
    action = paths.get(direction, None)

    if action == None:
        print "DOES NOT COMPUTE!"
        central_corridor_action(raw_input("> "), paths)
    else:
        return paths.get(direction, None)

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.

You're running down the central corridor to the Weapons Armory when 
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body. He's blocking the door to the
Armory and about to pull a weapon to blast you.
""",
central_corridor_action)

def armory_action(direction, paths):
        pass_code = "%d%d%d" % (randint(0,9), randint(0,9), randint(0,9))
        action = direction
        tries = 0
        while action != pass_code:
            tries +=1
            if tries > 9:
                return generic_death('armory')
            else:
                print "WRONG! Try again."
                action = raw_input("Password: ")
            
        return the_bridge

laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container. There's a keypad lock on the box
and you need the code to get the bomb out. If you get the code
wrong 10 times then the lock closes forever and you can't 
get the bomb. The code is 3 digits.
""",
armory_action)

def bridge_action(direction, paths):
    action = paths.get(direction, None)

    if action == None:
        print "DOES NOT COMPUTE!"
        bridge_action(raw_input("> "), paths)
    else:
        return paths.get(direction, None)

the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out. 
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship. Each of them has an even uglier 
clown costume than the last. They haven't pulled their 
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""",
bridge_action)

def escape_pod_action(direction, paths):
    action = paths.get(direction, None)

    if action == None:
        print "DOES NOT COMPUTE!"
        escape_pod_action(raw_input("> "), paths)
    else:
        return paths.get(direction, None)

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, and then carefully 
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to
get off this tin can.

You rush through the ship desparately trying to make it o
the escape pod before the whole ship explodes. It seems like 
hardly any Gothons are on the ship, so your run is clear of
interference. You get to the chamber with the escape pods, and 
now need to pick one to take. Some of them coud be damaged
but you don't have time to look. There's 5 pods, which one 
do you take?
""",
escape_pod_action)


the_end_winner = Room("The End", 
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to 
the planet below. As it flies to the planet, you look
back and see yout ship implode then explode like a
bright star, taking out the Gothon ship at the same
tie. You won!
""",
None)


the_end_loser = Room("The End",
"""
You jump into a random  pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body 
into jam jelly.
""", 
None)

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

def generic_death(cause):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    
    if cause == 'bridge':
        return "You try to throw the bomb, but aren't quick enough. The Gothons shoot you before the bomb can activate.", quips[randint(0, len(quips) - 1)]
    elif cause == 'armory':
        return "The lock has closed forever. A Gothon finds you and shoots you in the back before you can react.", quips[randint(0, len(quips) - 1)]
    elif cause == 'corridor1':
        return "You try to shoot the Gothon, but it's quicker than you. It shoots you!", quips[randint(0, len(quips) - 1)] 
    elif cause == 'corridor2':
        return "You try to dodge the Gothon, but it's quicker than you. It shoots you!", quips[randint(0, len(quips) - 1)] 

the_bridge.add_paths({
    'throw the bomb': generic_death('bridge'),
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    'bridge': the_bridge,
    'wrong': generic_death('armory')
})

central_corridor.add_paths({
    'shoot!': generic_death('corridor1'),
    'dodge!': generic_death('corridor2'),
    'tell a joke': laser_weapon_armory
})

START = central_corridor

def test_function():
    inputs = raw_input()
    output = inputs + 'done'
    return output