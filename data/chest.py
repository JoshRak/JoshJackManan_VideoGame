import pygame
from interactiveObject import InteractiveObject
class Chest(InteractiveObject):
    def __init__(self, contents, , contentAmount, chestType):
        self.contents = contents
        self.contentAmount = contentAmount
        self.type = chestType
    
    def display(self, screen, player):
        pass

    def closeDisplay(self, screen):
        pass

    def open(self, sceneManager, player):
        if self.type == 'KEY':
            sceneManager.drawImage('DEFAULT KEY CHEST IMAGE', (0,0))
        else:
            sceneManager.drawImage('DEFAULT TOOL CHST IMAGE', (0,0))
    
    def selected(self, sceneManager, player, selection):
        if self.type == 'TOOL':
            if selection == 'LEAVE':
                closeDisplay()
            elif selection == 'EQUIP':
                player.equip(self.contents)
            else:
                player.inventory.add_item(self.contents)
        else:
            player.keysCollection.append(self.contents)