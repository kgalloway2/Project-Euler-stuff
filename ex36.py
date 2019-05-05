from sys import exit

def treasure_room():
    print "You made it!"
    print "This is the treasure room!"
    print "It has \'treasure\'."
    
    while True:
        print "What do you do?"

        action = raw_input("> ")

        if "take" in action:
            print "You find nothing."
            print "Perhaps you should look harder next time."
            exit(0)
        elif "friendship" in action or "inside" in action:
            print "Yes! Friendship is the real treasure!"
            print "It was inside you all along!"
            print "CONGRATULATIONS"
            exit(0)
        else:
            print "You can't do that. At least not that way."
            print "What do you do?"
            action = raw_input("> ")

def nothing_room():
    print "There is nothing in this room."
    print "What do you do?"

    action = raw_input("> ")

    while True:

        if "keep going" in action:
            print "You search the room and find a door."
            print "What do you do?"

            action2 = raw_input("> ")

            while True: 
                if action2 == "open door":
                    treasure_room()
                elif action2 == "give up":
                    exit(0)
                else: 
                    print "You can't do that. At least not that way."
                    print "What do you do?"
                    action2 = raw_input("> ")
        elif "give up" in action:
            exit(0)
        else:
            print "You can't do that. At least not that way."
            print "What do you do?"
            action = raw_input("> ")

def sword_room():
    print "You enter a room with a swordsman."
    print "He shows off his skills with a fanciful display."
    print "What do you do?"

    action = raw_input("> ")

    if "compliment" in action or "clap" in action:
        print "The swordsman blushes and allows you to go to the next room."
        nothing_room()
    elif "gun" in action or "shoot" in action:
        print "Nice one Indy. He's dead."
        print "You can continue to the next room."
        nothing_room()
    else:
        dead("He is not pleased. He slices you in twain (destroy target artifact of enchantment and draw a card.")

def riddle_room():
    print "You're in an empty room."
    print "You here a voice."
    print "\"What is 10 + 10?\""
    
    answer = raw_input("> ")

    if answer == "20":
        print "CORRECT"
        print "At least, it's one correct answer."
        print "You may advance to the next room."
        nothing_room()
    elif answer == "100":
        print "Clever answer. Here is an extra room."
        sword_room()
    else:
        dead("WRONG")

def bear_room():
    print "This room has a bear trap in it."
    print "What do you do?"

    action = raw_input("> ")

    while True:

        if "trap" in action and "avoid" not in action and "around" not in action:
            print "You accidently set off the trap!"
            print "A bear skeleton falls from the ceiling."
            print "Looks like this trap hasn't been refeshed in a while."
            print "What do you do?"

            action = raw_input("> ")

        elif "avoid" in action or "around" in action or "look" in action:
            print "You avoid the trap and look around the room."
            print "There is a door!"
            print "You go through the door."
            nothing_room()
        else: 
            print "You can't do that. At least not in that way."
            print "What do you do?"
            action = raw_input("> ")

def start_room():
    print "You are in a dark room."
    print "There is a door to your left and a door to your right."
    print "Which one do you take?"

    door = raw_input("> ")

    while True:
        if door == 'left':
            print "You take the door on the left."
            riddle_room()
        elif door == 'right':
            print "You take the door on the right."
            bear_room()
        else:
            print "You can't do that. At least not in that way."
            print "What do you do?"
            door = raw_input("> ")

def dead(why):
    print why, "You died."
    exit(0)

start_room()
    