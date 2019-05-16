class lexicon(object):

    direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    verb = ['go', 'stop', 'kill', 'eat', 'look']
    stop = ['the', 'in', 'of', 'from', 'at', 'it']
    noun = ['door', 'bear', 'princess', 'cabinet', 'trap']

    def scan(self, input_string):
        string = input_string.lower()
        sentence = []
        words = string.split()
        for i in words:
            word_type = self.find_type(i)
            try:
                int(i)
                sentence.append((word_type, int(i)))
            except ValueError:
                sentence.append((word_type, i))
        return sentence
    
    def find_type(self, word):
        if word in self.direction:
            return "direction"
        elif word in self.verb:
            return "verb"
        elif word in self.stop:
            return "stop"
        elif word in self.noun:
            return "noun"
        try:
            int(word)
            return "number"
        except ValueError:
            return "error"