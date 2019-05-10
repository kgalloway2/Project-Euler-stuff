class Scene(object):

    def enter(self):
        self.enter

    def wdyd(self):
        print "What do you do?"
        return raw_input("> ")


class Engine(object):

    def __init__(self, scene_map):
        pass
        
    def play(self):
        central_corridor = CentralCorridor()
        central_corridor.enter1()
        

class Death(Scene):

    def enter(self, why):
        print why, "You died."
        

class CentralCorridor(Scene):

    def enter1(self):
        print "You find yourself in the central corridor of the Gothon ship."
        print "An enemy Gothon is standing nearby."
        action = self.wdyd()
        if "funny" in action or "joke" in action:
            print "The Gothon thought that was hilarious!"
            print "He laughs himself to death!"
            print "There are three doors with signs above them."
            print "Laser Weapon Armory"
            print "The Bridge"
            print "Escape Room"
            print "Where do you go?"
            where = raw_input("> ")
            next = Map(where)
            next.next_scene(where)
        else:
            death = Death()
            death.enter("The Gothon is unamused. He shoots you! ZAP")
    def enter2(self):
        global bomb
        print "You're back in the corridor."
        while True:
            if bomb == True:
                while True:
                    print "Where do you go?"
                    where = raw_input("> ")
                    if 'escape' in where:
                        next = Map(where)
                        next.next_scene(where)
                    else:
                        print "You probably should try to escape."
            else:
                print "Where do you go>"
                where = raw_input("> ")
                next = Map(where)
                next.next_scene(where)


class LaserWeaponArmory(Scene):

    def enter(self):
        global bomb
        if bomb == True:
            print "You need to escape!"
            while True:
                action = self.wdyd()
                if 'corridor' in action:
                    corridor = CentralCorridor()
                    corridor.enter2()
                else:
                    print "You can't do that. At least not in that way."
        else:    
            print "You have entered the Laser Weapon Armory."
            print "There is a neutron bomb container, but it's locked."
            print "There is a 9-digit keypad and a 3 character code."
            while True:
                action = self.wdyd()
                if 'code' in action:
                    while True:
                        print "What code will you try?"
                        code = raw_input("> ")
                        if code == '123':
                            bomb = True
                            print "You set off the bomb!"
                            print "You better escape soon!"
                            while True:
                                action = self.wdyd()
                                if 'corridor' in action:
                                    corridor = CentralCorridor()
                                    corridor.enter2()
                                else:
                                    print "You can't do that. At least not in that way."
                        else:
                            print "WRONG"
                else:
                    print "You can't do that. At least not in that way."
        

class TheBridge(Scene):

    def enter(self):
        global bomb
        if bomb == True:
            print "You need to escape!"
            while True:
                action = self.wdyd()
                if 'corridor' in action:
                    corridor = CentralCorridor()
                    corridor.enter2()
                else:
                    print "You can't do that. At least not in that way."
        else:
            print "You find yourself on the bridge of the Gothon ship."
            print "The Gothon captain notices you."
            action = self.wdyd()
            if "funny" in action or "joke" in action:
                print "The captain thought that was hilarious!"
                print "\'Don't try 123 as a code!\' He forces through his laughter."
                print "He laughs himself to death!"
                while True:
                    action = self.wdyd()
                    if 'corridor' in action:
                        corridor = CentralCorridor()
                        corridor.enter2()
                    else:
                        print "You can't do that. At least not in that way."
            else:
                death = Death()
                death.enter("The Captain is unamused. He shoots you! ZAP")
    

class EscapePod(Scene):

    def enter(self):
        global bomb
        if bomb == True:
            print "You need to escape!"
            while True:
                action = self.wdyd()
                if 'corridor' in action:
                    corridor = CentralCorridor()
                    corridor.enter2()
                elif 'pod' in action:
                    print "You find an escape pod and activate it. You get away safely!"
                else:
                    print "You can't do that. At least not in that way."
        else:
            print "There's nothing to do here now."
            while True:
                action = self.wdyd()
                if 'corridor' in action:
                    corridor = CentralCorridor()
                    corridor.enter2()
                else:
                    print "You can't do that. At least not in that way."


class Map(object):

    def __init__(self, start_scene): 
        pass
        
    def next_scene(self, scene_name):
        if "bridge" in scene_name:
            bridge = TheBridge()
            bridge.enter()
        elif "armory" in scene_name:
            armory = LaserWeaponArmory()
            armory.enter()
        elif "escape" in scene_name:
            escape = EscapePod()
            escape.enter()
        else:
            death = Death()
            death.enter("You took too long. A Gothon appears and shoots you! ZAP")
            

    def opening_scene(self):
        pass

bomb = False
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()