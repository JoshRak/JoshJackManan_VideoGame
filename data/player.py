import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
from pygame.locals import *
import data.menu as menu
import data.items as items

# restingDownImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingDown.png").convert_alpha(), (32,32))
# restingUpImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingUp.png").convert_alpha(), (32,32))
# restingLeftImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingLeft.png").convert_alpha(), (32,32))
# restingRightImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingRight.png").convert_alpha(), (32,32))
# walkingDown1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingDown1.png").convert_alpha(), (32,32))
# walkingDown2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingDown2.png").convert_alpha(), (32,32))
# walkingUp1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingUp1.png").convert_alpha(), (32,32))
# walkingUp2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingUp2.png").convert_alpha(), (32,32))
# walkingLeft1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingLeft1.png").convert_alpha(), (32,32))
# walkingLeft2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingLeft2.png").convert_alpha(), (32,32))
# walkingRight1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingRight1.png").convert_alpha(), (32,32))
# walkingRight2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingRight2.png").convert_alpha(), (32,32))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, posesList):
        super(Player, self).__init__()
        self.inventory = menu.Menu(Player)
        self.keysCollection = []
        self.equipped = items.computerTier0
        self.x = x
        self.y = y
        self.posesDict = self.initPoses(posesList)
        self.image = self.posesDict["restingDownImage"]
        self.movedLeft = False
        self.canMoveUp = True
        self.canMoveDown = True
        self.canMoveRight = True
        self.canMoveLeft = True
        self.lastPressedButtons = ""
        # self.inventory = []
        self.isAccessingChest = False
        # self.velocityX = 0
        # self.velocityY = 0

    def initPoses(self, posesList):
        poseNames = ["restingDownImage", "restingUpImage", "restingLeftImage", "restingRightImage",
                    "walkingDown1Image", "walkingDown2Image",
                    "walkingUp1Image", "walkingUp2Image",
                    "walkingLeft1Image", "walkingLeft2Image",
                    "walkingRight1Image", "walkingRight2Image"]
        return dict(zip(poseNames, posesList))

    def update(self, screen, keys, currentTime):
        dist = 7
        key = keys
        if any(key) and key.index(1) != 300 and not self.isAccessingChest:
            print("here")
            if (key[pygame.K_UP] or key[pygame.K_w]) and self.canMoveUp:
                self.y -= dist
                # self.velocityY = dist
                self.image = self.posesDict["walkingUp1Image"] if self.movedLeft else self.posesDict["walkingUp2Image"]
                self.lastPressedButtons = "UP"
            elif (key[pygame.K_DOWN] or key[pygame.K_s]) and self.canMoveDown:
                self.y += dist
                # self.velocityY = -dist
                self.image = self.posesDict["walkingDown1Image"] if self.movedLeft else self.posesDict["walkingDown2Image"]
                self.lastPressedButtons = "DOWN"
            # else:
                # self.velocityY = 0
            if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.canMoveLeft:
                self.x -= dist
                # self.velocityX = -dist
                self.image = self.posesDict["walkingLeft1Image"] if self.movedLeft else self.posesDict["walkingLeft2Image"]
                self.lastPressedButtons = "LEFT"
            elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.canMoveRight:
                self.x += dist
                # self.velocityX = dist
                self.image = self.posesDict["walkingRight1Image"] if self.movedLeft else self.posesDict["walkingRight2Image"]
                self.lastPressedButtons = "RIGHT"
            # else:
                # self.velocityX = 0
            self.movedLeft = not self.movedLeft
            if (key[pygame.K_q] and not self.inventory.currentlyDisplayed):
                print (self.inventory)
                print(self.equipped)
        else:
            # self.velocityX = self.velocityY = 0
            if self.lastPressedButtons == "LEFT":
                self.image = self.posesDict["restingLeftImage"]
            elif self.lastPressedButtons == "UP":
                self.image = self.posesDict["restingUpImage"]
            elif self.lastPressedButtons == "RIGHT":
                self.image = self.posesDict["restingRightImage"]
            else:
                self.image = self.posesDict["restingDownImage"]
        # screen.blit(self.image, (self.x, self.y))
        sleep(0.04)

    def equipPart(self, part):
        currentPart = getattr(self.equipped, str(type(part))[19:-2].lower())
        if currentPart == None:
            setattr(self.equipped, str(type(part))[19:-2].lower(), part)
            print (self.equipped.mouse)
        else:
            if len(self.inventory.inventory) == 9:
                raise ValueError("Could not equip or add to inventory!")
            else:
                self.inventory.add_item(getattr(self.equipped, str(type(part))[19:-2].lower()), 1)
                setattr(self.equipped, str(type(part))[19:-3].lower(), part)
                raise ValueError("You already have a part equipped!")

    def equipComputer(self, computer):
        self.equipped = computer

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
