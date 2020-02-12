import pygame

class Menu(object):
    def __init__(self, player):
        self.player = player
        self.maxItems = {'PART':'AMOUNT AS INT'}
        self.inventory = {}
        self.image = "ADD TEMPLATE IMAGE HERE"
        self.currentlyDisplayed = False

    def maxQuantity(item, itemQuantity):
        if self.inventory[item] + itemQuantity > self.maxItems[item]:
            itemQuantity = self.maxItems[item] - self.inventory[item]
        return itemQuantity

    def add_item(self, item, itemAmount):
        if len(self.inventory) == 9:
            print("You have too many items in your inventory")
        else:
            itemQuantity = maxQuantity(item, itemAmount)
            if itemQuantity != itemAmount:
                print("You tried to add {} items but can only add {}".format(itemAmount, itemQuantity))
            self.inventory[item] = self.inventory[item] + itemQuantity if item in self.inventory else itemQuantity

    def drop_item(self, item, itemAmount):
        if item in self.inventory:
            if itemAmount > self.inventory[item]:
                print("You tried to delete {} items but can only delete {}".format(itemAmount, self.inventory[item]))
                del self.inventory[item]
            else:
                self.inventory[item] -= itemAmount
        else:
            print("This item was not found")
    def display(self, sceneMananger):
        self.currentlyDisplayed = True
        sceneMananger.drawImage(self.image, (0,0))
        sceneMananger.drawImage(player.equipped['CPU'] if 'CPU' in player.equipped else 'DEFAULT IMAGE', ('(X,Y) CPU LOCATION'))
        sceneMananger.drawImage('HOTBAR IMAGE', ('SOME LOW POINT'))
        i = 0
        for part in self.inventory.keys():
            i += 1
            sceneMananger.drawImage('./Assets/Sprites/{}'.format(part), ('HOTBAR X VAL' + i * 'IMAGE SIZE + 10', 'HOTBAR Y VAL'))

    def close(self, sceneMananger, currentTime, events):
        self.currentlyDisplayed = False
        sceneMananger.update(currentTime, events)
        
