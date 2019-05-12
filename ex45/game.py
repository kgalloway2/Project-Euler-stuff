from player import Player
from mathmaker import easy_question
from mathmaker import hard_question
from inventory import Inventory
import random
from action import Action
from sys import exit

class Map(object):
    
    current_map = [
        'Starting Room'
        
    ]

    total_map = [
        'Math Intro Room',
        'Combat Intro Room',
        'Battle Room',
        'Question Room',
        'Mini-Boss Room',
        'Question Room',
        'Battle Room',
        'Rest Room',
        'Boss Room',
        'Final Room'
    ]

    def add_room(self):
        new_room = self.total_map.pop(0)
        self.current_map.append(new_room)
        print "You discovered the %s!" % new_room

    def check_map(self):
        if len(self.current_map) <= 6:
            print "-" * (19 * len(self.current_map))
            print " --> ".join(self.current_map)
            print "-" * (19 * len(self.current_map))
        else:
            print "-" * (19 * len(self.current_map[0:6]))
            print " --> ".join(self.current_map[0:6])
            print "-" * (19 * len(self.current_map[0:6]))
            print " --> ".join(self.current_map[6:])
            print "-" * (19 * len(self.current_map[6:]))

class Spawner(object):

    adjectives = ['finite', 'double', 'triple', 'mathematical', 'complex', 'logarithmic', 'sinusoidal', 'asymptotic', 'recursive']
    nouns = ['slime', 'zombie', 'devil', 'elemental', 'drake', 'horror', 'hydra', 'goblin', 'demon']
    
    def minor_enemy(self):
        name = "%s %s" % (self.adjectives[random.randint(0, 3)], self.nouns[random.randint(0, 4)])
        health = random.randint(10, 35)
        power = random.randint(4, 9)
        armor = random.randint(-3, 0)
        enemy = [name, health, power, armor]
        return enemy

    def major_enemy(self):
        name = "%s %s" % (self.adjectives[random.randint(0, 8)], self.nouns[random.randint(0, 8)])
        health = random.randint(20, 50)
        power = random.randint(8, 14)
        armor = random.randint(-8, -2)
        enemy = [name, health, power, armor]
        return enemy

def combat(player, difficulty):
    spawner = Spawner()
    action = Action()
    player.update_stats()
    run_away = False
    alive = True

    if difficulty == 'mini-boss':
        enemy = ['Hyperreal Beast', 50, 10, -5]
    elif difficulty == 'boss':
        enemy = ['Dragon of Infinity', 100, 17, -5]
    elif (difficulty > 5):
        enemy = spawner.major_enemy()
    else:
        enemy = spawner.minor_enemy()

    print "An enemy! It's a %s." % enemy[0]
    while (enemy[1] > 0) and (player.current_stats[0] > 0):
        answer = action.wdyd("What do you do?   1. Attack   2. Heal   3. Run")
        damage = (player.current_stats[1] + enemy[3] + random.randint(-2, 2))
        if answer == '1':
            if damage <= 0:
                damage = 0
                print "You attack, but it's flawed! The %s takes no damage." % enemy[0]
            else:
                if random.randint(1, 15) == 15:
                    print "Critical hit! The %s takes %s damage." % (enemy[0], (2 * damage))
                    enemy[1] -= (2 * damage)
                else:
                    print "The %s takes %s damage." % (enemy[0], damage)
                    enemy[1] -= (damage)
        elif answer == '2':
            if "Salve of Eratosthenes" in player.inventory:
                print "You used a salve. +15 Health"
                player.current_stats[0] += 15
                player.inventory.remove('Salve of Eratosthenes')
            else:
                action.impossible()
        elif answer == '3':
            run_away = True
            break
        else:
            action.impossible()
        print "The %s now has %d health." % (enemy[0], enemy[1])
        if (enemy[1] > 0):
            damage = (enemy[2] + player.current_stats[2] + random.randint(-2, 2))
            if damage <= 0:
                damage = 0
                print "The %s attacks, but it's too weak to pierce your logic! You take no damage!" % enemy[0]
            else:
                print "The %s attacks! You take %s damage." % (enemy[0], damage)
                player.current_stats[0] -= damage
        else:
            break
        print "You now have %d health." % player.current_stats[0]
        if (player.current_stats[0] < 1):
            alive = False
            break
    if run_away == True:
        print "You ran away!"
        return None
    elif alive == False:
        action.dead("You were killed!")
        print "Your adventure is over. You fought valiantly, but it was not enough. Better luck next time!"
        exit()
    else: 
        print "You killed the %s! Good job!" % enemy[0]
        player.add_item('Salve of Eratosthenes')
        return 'win'

def basic_actions(answer, player, map, obstacle):
    if 'inventory' in answer:
        inv = Inventory(player.inventory)
        inv.check_inventory()
    elif 'map' in answer:
        map.check_map()
    elif 'next' in answer and obstacle == False:
        map.add_room()
        rooms(map, player)
    elif 'next' in answer and obstacle == True:
        print "You must clear this room first."
    else:
        action = Action()
        action.impossible()

def rooms(map, player):
    progress = len(map.current_map)
    action = Action()
    if progress == 1:
        obstacle = True
        print "Welcome! You have entered the Dungeon of Mathematical Monsters!"
        print "There are obstacles ahead that will test all of your strengths."
        action.wdyd("Are you ready?")
        print "Okay! Before you get started, let me give you some advice:"
        print "\t1. To check your map, type \'map\'."
        print "\t2. To check your inventory, type \'inventory\'."
        print "\t3. To keep going to the next room or challenge, type \'next\'."
        action.wdyd("Want to give it a try?")
        action_counter = 0
        while action_counter < 2:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
            action_counter += 1
        while progress == 1:
            obstacle = False
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
        
    elif progress == 2:
        obstacle = True
        print "You're now in the Math Intro Room!"
        print "To advance here, you need to solve three problems!"
        action.wdyd("Ready to start?")
        correct_answers = 0
        while correct_answers < 3:
            correct_answers += easy_question()
            print "You have solved %d problem(s) so far." % correct_answers
        obstacle = False
        print "Congrats! You solved three problems!"
        print "Here's a reward!"
        player.add_item('Salve of Eratosthenes')
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
    
    elif progress == 3:
        obstacle = True
        print "Great job in the last room! Now it's time to learn how to fight!"
        print "You have three options during combat."
        print "You can attack, heal, or run away."
        print "You can choose an action by selecting its number during combat."
        action.wdyd("Ready to start?")
        while obstacle == True:
            battle = combat(player, progress)
            if battle == 'win':
                obstacle = False
            elif battle == 'dead':
                pass
            else:
                print "Let's try again."
        print "Nice fight!"
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
    
    elif progress == 4:
        obstacle = True
        print "Now it's time for a real challenge!"
        print "Win three battles and you can advance!"
        wins = 0
        while wins < 3:
            battle = combat(player, progress)
            if battle == 'win':
                wins += 1
            else:
                print "Let's try again."
        obstacle = False
        print "Great battling!  You're getting really good at this!"
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
    
    elif progress == 5:
        obstacle = False
        print "After this room, you're going to face a stronger challenge than ever before!"
        print "If you can answer 5 questions correctly in a row..."
        print "...Then I'll give you a special sword."
        answer = action.wdyd("What will you do? If you want to try answering questions, say \'challenge\'.")
        correct_answers = 0
        if answer == 'challenge':
            while correct_answers < 5:
                current_question = easy_question()
                if current_question == 1:
                    correct_answers += 1
                    print "Fantastic! That's %d in-a-row!" % correct_answers
                else:
                    correct_answers = 0
        if correct_answers >= 5:
            player.add_item('Euler\'s Sword')
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
     
    elif progress == 6:
        obstacle = True
        while obstacle == True:
            battle = combat(player, 'mini-boss')
            if battle == 'win':
                obstacle = False
                print "It looks like the beast dropped some armor."
                player.add_item('Axiomatic Armor')
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
    
    elif progress == 7:
        obstacle = True
        print "You're now in a Question Room!"
        print "To advance here, you need to solve five harder problems!"
        action.wdyd("Ready to start?")
        correct_answers = 0
        while correct_answers < 5:
            correct_answers += hard_question()
            print "You have solved %d problem(s) so far." % correct_answers
        obstacle = False
        print "Congrats! You solved three problems!"
        print "Here's some rewards!"
        player.add_item('Salve of Eratosthenes')
        player.add_item('Salve of Eratosthenes')
        player.add_item('Salve of Eratosthenes')
        player.add_item('Salve of Eratosthenes')
        player.add_item('Salve of Eratosthenes')
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
    
    elif progress == 8:
        obstacle = True
        print "Now it's time for the hardest combat challenge yet!"
        print "Win five battles and you can advance!"
        wins = 0
        while wins < 5:
            battle = combat(player, progress)
            if battle == 'win':
                wins += 1
            else:
                print "Let's try again."
        obstacle = False
        print "Great battling! You're a very skilled fighter!"
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
    
    elif progress == 9:
        obstacle = False
        print "Congratulations brave adventurer! You are nearly through the dungeon."
        print "This room is your final chance to rest before you fight the strongest enemy yet."
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
    
    elif progress == 10:
        obstacle = True
        while obstacle == True:
            battle = combat(player, 'boss')
            if battle == 'win':
                obstacle = False
                print "The dragon is slain!"
        while True:
            answer = action.wdyd("What will you do?")
            basic_actions(answer, player, map, obstacle)
    
    elif progress == 11:
        print "Many, many congratulations adventurer! You have conquered the Dungeon of Mathematical Monsters!"
        print "I hope you will play again someday!"
        exit()
        
def main():
    base_stats = [50, 5, 0]
    base_inventory = []
    base_map = Map()
    player = Player(base_stats, base_inventory)
    while True:
        rooms(base_map, player)

if __name__ == '__main__':
    main()
    