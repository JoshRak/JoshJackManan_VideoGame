import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
from pygame.locals import *
import data.menu as menu
import data.items as items
import itertools
import data.terminal as terminal
import copy
import os
import socket
import sys

HOST = '192.168.43.227'  # The server's hostname or IP address
PORT = 65433    # The port used by the server

class GhostPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, posesList):
        super(GhostPlayer, self).__init__()
        self.roomNum = None
        self.roomThreeCompleted = False 
        self.roomFourCompleted = False
        self.roomFiveCompleted = False
        self.roomSixCompleted = True
        self.roomSevenCompleted = False
        self.roomEightCompleted = False
        self.roomNineCompleted = False
        self.roomTenCompleted = False
        self.roomElevenCompleted = False
        self.roomTwelveCompleted = False
        self.inventory = menu.Menu(self)
        self.keysCollection = []
        self.keysQueue = []
        self.equipped = None 
        self.x = x
        self.y = y
        self.netChange = 0 
        self.posesDict = self.initPoses(posesList)
        self.positions = self.initPositions()
        self.challengeStates = self.refreshChallengeStates()
        self.image = self.posesDict["restingDownImage"]
        self.movedLeft = False
        self.canMoveUp = True
        self.canMoveDown = True
        self.canMoveRight = True
        self.canMoveLeft = True
        self.lastPressedButtons = ""
        self.isAccessingChest = False
        self.terminal = terminal.Terminal((460,490), self)
        self.originalDirectory = os.getcwd()
        
    # initalizes positions for ghost player
    def initPositions(self):
        widthOffset = 80
        heightOffset = 40

        positionsDict = {
            "top" : (224, 135 + heightOffset),
            "bottom" : (224, 480 - heightOffset),
            "right" : (448 - widthOffset, 240),
            "left" : (widthOffset, 240)
        }
        return positionsDict
    
    # initalizes poses for ghost player
    def initPoses(self, posesList):
        poseNames = ["restingDownImage", "restingUpImage", "restingLeftImage", "restingRightImage",
                    "walkingDown1Image", "walkingDown2Image",
                    "walkingUp1Image", "walkingUp2Image",
                    "walkingLeft1Image", "walkingLeft2Image",
                    "walkingRight1Image", "walkingRight2Image"]
        return dict(zip(poseNames, posesList))

    def selectStartPos(self, pos, coords=None):
        if coords:
            if coords[0]:
                self.x = coords[0]
                self.y = self.positions[pos][1]
            elif coords[1]:
                self.x = self.positions[pos][0]
                self.y = coords[1]
            return
        self.x, self.y = self.positions[pos]

    def refreshChallengeStates(self):
        challengeStatesDict = {
            3:self.roomThreeCompleted,
            4:self.roomFourCompleted,
            5:self.roomFiveCompleted,
            6:self.roomSixCompleted,
            7:self.roomSevenCompleted,
            8:self.roomEightCompleted,
            9:self.roomNineCompleted,
            10:self.roomTenCompleted,
            11:self.roomElevenCompleted,
            12:self.roomTwelveCompleted
        }
        return challengeStatesDict
    
    def setXY(self, x, y):
        self.x = x
        self.y = y

    # goes to end screen based on if user won or lost
    def endCondition(self, screen): 
        for i in range (0, 4):
            self.scene.player.pushServer()
            sleep(.15)
        if self.scene.player.numRoomsCompleted > 4: # display win
            self.scene.manager.renderClosingScene(screen, True)
            pygame.display.update()
        else: # display loss
            self.scene.manager.renderClosingScene(screen, False)
            pygame.display.update()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    sys.exit(1)

    # displays ghost player on the screen after parsing through feedback from server and updates player based on server feedback
    def draw(self, surface, x=None, y=None):
        if self.scene.player.feedback:
            self.x = self.scene.player.feedback["x"]
            self.y = self.scene.player.feedback["y"]
            self.roomNum = self.scene.player.feedback["roomNum"]
            if self.scene.player.feedback["imageStr"] != '0':
                self.image = self.posesDict[self.scene.player.feedback["imageStr"]]
            if not self.scene.player.roomThreeCompleted:
                self.scene.player.roomThreeCompleted = self.scene.player.feedback["roomThreeCompleted"]
            if not self.scene.player.roomFourCompleted:
                self.scene.player.roomFourCompleted = self.scene.player.feedback["roomFourCompleted"]
            if not self.scene.player.roomFiveCompleted:
                self.scene.player.roomFiveCompleted = self.scene.player.feedback["roomFiveCompleted"]
            if not self.scene.player.roomSixCompleted:
                self.scene.player.roomSixCompleted = self.scene.player.feedback["roomSixCompleted"]
            if not self.scene.player.roomSevenCompleted:
                self.scene.player.roomSevenCompleted = self.scene.player.feedback["roomSevenCompleted"]
            if not self.scene.player.roomEightCompleted:
                self.scene.player.roomEightCompleted = self.scene.player.feedback["roomEightCompleted"]
            if not self.scene.player.roomNineCompleted:
                self.scene.player.roomNineCompleted = self.scene.player.feedback["roomNineCompleted"]
            if not self.scene.player.roomTenCompleted:
                self.scene.player.roomTenCompleted = self.scene.player.feedback["roomTenCompleted"]
            if not self.scene.player.roomElevenCompleted:
                self.scene.player.roomElevenCompleted = self.scene.player.feedback["roomElevenCompleted"]
            if not self.scene.player.roomTwelveCompleted:
                self.scene.player.roomTwelveCompleted = self.scene.player.feedback["roomTwelveCompleted"]
            if self.scene.player.numRoomsCompleted + int(self.scene.player.feedback["numRoomsCompleted"]) == 9:
                self.endCondition(surface)
            
            for chest in self.scene.player.chestDict:
                if not self.scene.player.chestDict[chest]:
                    try:
                        self.scene.player.chestDict[chest] = self.scene.player.feedback[chest]
                        self.scene.chests[chest].alreadyAccessed = self.scene.player.feedback[chest]
                    except:
                        continue

        if x is None and y is None:
            x = self.x
            y = self.y

        if self.roomNum == self.scene.roomNum:
            surface.blit(self.image, (x, y))