print "You enter a dark room with three doors. Do you go through door #1, door #2, or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else: 
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jellp. Good job!"
    else: 
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You encounter a nasty Gordon Palmer desk. What do you do?"
    print "1. Sit in the desk."
    print "2. Burn it!"

    desk = raw_input("> ")

    if desk == "1":
        print "Sorry bro. You have to take a math test."
    elif desk == "2":
        print "Great choice! That desk is older than the university! It deserves a fiery death!"
    else: 
        print "I don't think \"%s\" will help." % desk 

else: 
    print "How many hours do you want to wait?"

    time = int(raw_input("> "))

    if time <= 5:
        print "You fall asleep."
    elif 5 < time <=10:
        print "You take a nice nap and wake up feeling rested."
    else:
        print "Why would you wait for %d hours?!" % time 