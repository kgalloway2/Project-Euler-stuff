import random

# both functions take no input and return 1 if correct and 0 if wrong

def easy_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 2)
    if c == 1:
        print "What is %d + %d?" % (a, b)
        answer = raw_input("> ")
        if answer == str((a + b)):
            print "That's correct!"
            return 1
        else:
            print "Sorry! That's not right."
            return 0
    elif c == 2:
        print "What is %d - %d?" % (max(a, b), min(a, b))
        answer = raw_input("> ")
        if answer == str(abs(a - b)):
            print "That's correct!"
            return 1
        else:
            print "Sorry! That's not right."   
            return 0

def hard_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 3)
    if c == 1:
        print "What is %d * %d?" % (a, b)
        answer = raw_input("> ")
        if answer == str((a * b)):
            print "That's correct!"
            return 1
        else:
            print "Sorry! That's not right."
            return 0
    elif c == 2:
        print "If %d + X = %d, what is X?" % (min(a, b),max(a, b))
        answer = raw_input("> ")
        if answer == str((max(a, b) - min(a, b))):
            print "That's correct!"
            return 1
        else:
            print "Sorry! That's not right."
            return 0
    elif c == 3:
        print "If X - %d = %d, what is X?" % (max(a, b),min(a, b))
        answer = raw_input("> ")
        if answer == str((min(a, b) + max(a, b))):
            print "That's correct!"
            return 1
        else:
            print "Sorry! That's not right."
            return 0