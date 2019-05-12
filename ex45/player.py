import random
from action import Action
from inventory import items, Inventory

class Player(object):

    def __init__(self, base_stats, inventory):
        self.base_stats = base_stats
        self.inventory = inventory
        self.current_stats = self.base_stats

    def add_item(self, item):
        self.inventory.append(item)
        print "You got %s!" % item

    def update_stats(self):
        self.current_stats[0] = 50
        if 'Euler\'s Sword' in self.inventory:
            self.current_stats[1] = 15
        if 'Axiomatic Armor' in self.inventory:
            self.current_stats[2] = -10

    def reset_stats(self):
        self.current_stats = self.base_stats
