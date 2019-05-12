class Action(object):
    
    def question(self, why):
        print why
        answer = raw_input("> ")
        return answer

    def wdyd(self, what):
        print what
        answer = raw_input("> ")
        return answer

    def impossible(self):
        print "You can't do that. At least not in that way."

    def dead(self, what):
        print what