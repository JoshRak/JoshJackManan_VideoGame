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

HOST = '192.168.1.228'  # The server's hostname or IP address
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

    def delay(self):
        delay = 0
        if self.equipped:
            delay += self.equipped.delay
            if self.equipped.gpu:
                delay += self.equipped.gpu.delay
            else:
                delay += 0.25
            if self.equipped.cpu:
                delay += self.equipped.cpu.delay
            else:
                delay += 0.25
            if self.equipped.coolingsystem:
                delay += self.equipped.coolingsystem.delay
            else:
                delay += 0.25
            if self.equipped.mouse:
                delay += self.equipped.mouse.delay
            else:
                delay += 0.25
            if self.equipped.keyboard:
                delay += self.equipped.keyboard.delay
            else:
                delay += 0.25
        return delay

    def openInventory(self, screen):
        print(self.inventory)
        self.inventory.render(screen)
        pygame.display.update()
        if self.inventory.inventory:
            sleep(0.02)
            val = True
            while val:
                print("In loop")
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            val = False
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.inventory.select_next()
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.inventory.select_prev()
                        elif event.key == pygame.K_RETURN:
                            print (self.inventory.currentItem)
                            if isinstance(self.inventory.currentItem, items.Computer):
                                if self.equipped:
                                    if self.equipped.tier < self.inventory.currentItem.tier:
                                        for a in dir(self.inventory.currentItem):
                                            if not a.startswith('__'):
                                                if getattr(self.inventory.currentItem, a) is None and getattr(self.equipped, a) is not None:
                                                    setattr(self.inventory.currentItem, a, getattr(self.equipped, a))
                                        x = self.equipped
                                        self.inventory.drop_item(self.inventory.currentItem, 1)
                                        self.inventory.add_item(self.equipped, 1)
                                        self.equipped = self.inventory.currentItem
                                        self.inventory.select_next()
                                else:
                                    x = copy.deepcopy(self.equipped)
                                    self.inventory.drop_item(self.inventory.currentItem, 1)
                                    self.inventory.add_item(self.equipped, 1)
                                    self.equipped = self.inventory.currentItem
                                    self.inventory.select_next()
                                    # self.inventory.update(screen)
                                    # self.inventory.add_item(getattr(self.equipped, str(type(self.inventory.currentItem))[19:-2].lower()), 1)
                            else:
                                if self.equipped and self.equipped.tier >= self.inventory.currentItem.tier:
                            # if hasattr(self.equipped, str(type(self.inventory.currentItem))[19:-2]):
                                    self.inventory.drop_item(self.inventory.currentItem, 1)
                                    self.inventory.add_item(getattr(self.equipped, str(type(self.inventory.currentItem))[19:-2].lower()), 1)
                                    setattr(self.equipped, str(type(self.inventory.currentItem))[19:-2].lower(), self.inventory.currentItem)
                                    self.inventory.select_next()
                        elif event.key == pygame.K_f:
                            self.inventory.drop_item(self.inventory.currentItem, 1)
                            self.inventory.select_next()
                self.inventory.update(screen)
                # self.inventory.select_item(select)
                pygame.display.update()
        else:
            self.inventory.render(screen)
            pygame.display.update()
            sleep(0.02)
            val = True
            while val:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            val = False

    def pushServer(self, command):
        self.keysQueue.append(command)
        payload = ' '.join(self.keysQueue)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(payload.encode())
                feedback = s.recv(1024).decode()
                self.feedback = feedback
        except:
            pass
    
    def update(self, screen, keys, currentTime):
        self.x, self.y, self.roomNum = [int(x) for x in self.scene.player.feedback[0:3]]
        dist = 4
        key = keys
        if any(key) and key.index(1) != 300 and not self.isAccessingChest:
            self.netChange += 4
            # print("here")
            if (key[pygame.K_UP] or key[pygame.K_w]) and self.canMoveUp:
                print("Moved y", self.canMoveUp)
                self.y -= dist
                # self.velocityY = dist
                self.image = self.posesDict["walkingUp1Image"] if self.movedLeft else self.posesDict["walkingUp2Image"]
                self.lastPressedButtons = "UP"
                # self.pushServer("up")
            elif (key[pygame.K_DOWN] or key[pygame.K_s]) and self.canMoveDown:
                self.y += dist
                # self.velocityY = -dist
                self.image = self.posesDict["walkingDown1Image"] if self.movedLeft else self.posesDict["walkingDown2Image"]
                self.lastPressedButtons = "DOWN"
                #send down to server
                # self.pushServer("down")
            # else:
                # self.velocityY = 0
            if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.canMoveLeft:
                self.x -= dist
                # self.velocityX = -dist
                self.image = self.posesDict["walkingLeft1Image"] if self.movedLeft else self.posesDict["walkingLeft2Image"]
                self.lastPressedButtons = "LEFT"
                self.pushServer("left")
            elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.canMoveRight:
                self.x += dist
                # self.velocityX = dist
                self.image = self.posesDict["walkingRight1Image"] if self.movedLeft else self.posesDict["walkingRight2Image"]
                self.lastPressedButtons = "RIGHT"
                self.pushServer("right")
            # else:
                # self.velocityX = 0
            if self.netChange % 12 == 0:
                self.movedLeft = not self.movedLeft
            if (key[pygame.K_q]):
                self.openInventory(screen)
            elif key[pygame.K_t] and self.equipped:
                os.chdir(os.getcwd() + "/challenges")
                print(os.getcwd())
                val = True
                while val:
                    events = pygame.event.get()
                    for event in events:
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            val = False
                            os.chdir(self.originalDirectory)
                    self.terminal.update(events)
                    sleep(self.delay()*0.15)
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
        sleep(0.01)

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def equipPart(self, part):
        if self.equipped and not self.equipped.tier < part.tier:
            currentPart = getattr(self.equipped, str(type(part))[19:-2].lower())
            if currentPart == None:
                setattr(self.equipped, str(type(part))[19:-2].lower(), part)
                print (self.equipped.mouse)
            else:
                if len(self.inventory.inventory) == 5:
                    raise ValueError("Could not equip or add to inventory!")
                else:
                    self.inventory.add_item(getattr(self.equipped, str(type(part))[19:-2].lower()), 1)
                    setattr(self.equipped, str(type(part))[19:-3].lower(), part)
                    raise ValueError("You already have a part equipped!")
        else:
            self.inventory.add_item(part, 1)

    def equipComp(self, computer):
        if self.equipped:
            if len(self.inventory.inventory == 5):
                self.inventory.add_item(computer)
                raise ValueError("Could not equip or add to inventory!")
            else:
                raise ValueError("Could not equip!")
        else:
            self.equipped = computer
        print(self.equipped)

    def draw(self, surface, x=None, y=None):
        if self.scene.player.feedback:
            print(self.scene.player.feedback)
            self.x, self.y, self.roomNum = [int(val) for val in self.scene.player.feedback[0:3]]
            self.image = self.posesDict[self.scene.player.feedback[4]]

        if x is None and y is None:
            x = self.x
            y = self.y

        if self.roomNum == self.scene.roomNum:
            surface.blit(self.image, (x, y))
        