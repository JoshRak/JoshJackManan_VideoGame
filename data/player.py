import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
from pygame.locals import *

restingDownImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingDown.png").convert_alpha(), (32,32))
walkingDown1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingDown1.png").convert_alpha(), (32,32))
walkingDown2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingDown2.png").convert_alpha(), (32,32))
restingUpImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingUp.png").convert_alpha(), (32,32))
walkingUp1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingUp1.png").convert_alpha(), (32,32))
walkingUp2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingUp2.png").convert_alpha(), (32,32))
restingLeftImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingLeft.png").convert_alpha(), (32,32))
walkingLeft1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingLeft1.png").convert_alpha(), (32,32))
walkingLeft2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingLeft2.png").convert_alpha(), (32,32))
restingRightImage = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/restingRight.png").convert_alpha(), (32,32))
walkingRight1Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingRight1.png").convert_alpha(), (32,32))
walkingRight2Image = pygame.transform.scale(pygame.image.load("./Assets/Images/Sprites/Characters/walkingRight2.png").convert_alpha(), (32,32))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.x = x
        self.y = y
        self.image = restingDownImage
        self.movedLeft = False
        self.canMoveUp = True
        self.canMoveDown = True
        self.canMoveRight = True
        self.canMoveLeft = True
        self.lastPressedButtons = ""
        self.inventory = []
        # self.velocityX = 0
        # self.velocityY = 0

    def update(self, keys, currentTime):
        dist = 7
        key = keys
        if any(key) and key.index(1) != 300:
            if (key[pygame.K_UP] or key[pygame.K_w]) and self.canMoveUp:
                self.y -= dist
                # self.velocityY = dist
                self.image = walkingUp1Image if self.movedLeft else walkingUp2Image
                self.lastPressedButtons = "UP"
            elif (key[pygame.K_DOWN] or key[pygame.K_s]) and self.canMoveDown:
                self.y += dist
                # self.velocityY = -dist
                self.image = walkingDown1Image if self.movedLeft else walkingDown2Image
                self.lastPressedButtons = "DOWN"
            # else:
                # self.velocityY = 0
            if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.canMoveLeft:
                self.x -= dist
                # self.velocityX = -dist
                self.image = walkingLeft1Image if self.movedLeft else walkingLeft2Image
                self.lastPressedButtons = "LEFT"
            elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.canMoveRight:
                self.x += dist
                # self.velocityX = dist
                self.image = walkingRight1Image if self.movedLeft else walkingRight2Image
                self.lastPressedButtons = "RIGHT"
            # else:
                # self.velocityX = 0
            self.movedLeft = not self.movedLeft
        else:
            # self.velocityX = self.velocityY = 0
            if self.lastPressedButtons == "LEFT":
                self.image = restingLeftImage
            elif self.lastPressedButtons == "UP":
                self.image = restingUpImage
            elif self.lastPressedButtons == "RIGHT":
                self.image = restingRightImage
            else:
                self.image = restingDownImage

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
