from action import Action

items = {
    'Euler\'s Sword': ('A sword wielded by a powerful mathematician. + 10 Power'),
    'Salve of Eratosthenes': ('A healing salve. Heals 15 Health'),
    'Axiomatic Armor': ('The fundamentals of protection. Prevents up to 10 Damage')
}

class Inventory(object):

    def __init__(self, base_inventory):
        self.inventory = base_inventory

    def check_inventory(self):
        if not self.inventory:
            print "You have no items."
        else:
            print self.inventory
            action = Action()
            answer = action.question("Which item would you like to check? Answer with a number position or \'none\'.")
            if answer == 'none':
                pass
            try:
                self.check_item(int(answer))
            except ValueError:
                action.impossible()
            else:
                pass

    def check_item(self, item):
        if item <= len(self.inventory) and item > 0:
            print items[self.inventory[item-1]]
        else:
            action = Action()
            action.impossible()