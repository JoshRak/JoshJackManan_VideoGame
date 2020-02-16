import pygame
# from interactiveObject import InteractiveObject
class Chest():
    def __init__(self, contents, contentAmount, chestType, x, y):
        self.contents = contents
        self.alreadyAccessed = False
        self.contentAmount = contentAmount
        self.type = chestType
        self.x = x
        self.y = y
        if chestType == 'key':
            pass
        else:
            self.chestImage = pygame.transform.scale(pygame.image.load("./Assets/Images/ToolChestOpened.png"), (384, 426))
    
    def open(self, screen, currentTime):
        screen.blit(self.chestImage, (32,32))
        print(self.contents)
        screen.blit(pygame.transform.scale(pygame.image.load(self.contents.imagePath), (140, 155)), (155, 120))
        # if self.type == 'KEY':
        #     sceneManager.drawImage(self.toolChestImage, (0,0))
        # else:
        #     sceneManager.drawImage('DEFAULT TOOL CHST IMAGE', (0,0))
    
    def selected(self, screen, player, selection):
        print(selection)
        if self.type == 'TOOL':
            if selection == 'LEAVE':
                self.alreadyAccessed = False
                player.isAccessingChest = False
            elif selection == 'EQUIP':
                try:
                    player.isAccessingChest = False
                    self.alreadyAccessed = True
                    player.equipPart(self.contents)
                except ValueError as Er:
                    print(Er)
                    if 'not' in str(Er):
                        self.alreadyAccessed = False
                        player.isAccessingChest = True
            else:
                try:
                    player.inventory.add_item(self.contents, 1)
                    self.alreadyAccessed = True
                    player.isAccessingChest = False
                except ValueError as Er:
                    print(Er)
                    self.alreadyAccessed = False
                    player.isAccessingChest = True
        else:
            player.keysCollection.append(self.contents)