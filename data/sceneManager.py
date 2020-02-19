import pygame
from itertools import cycle
from time import sleep

class SceneManager(object):
    def __init__(self, sceneList):
        self.scenes = self.initScenes(sceneList) 
        for scene in sceneList:
            x = [x for x in self.scenes if scene in x][0]
            scene.xMapIndex = self.scenes.index(x)
            scene.yMapIndex = x.index(scene)
            scene.manager = self
        # self.scenes = cycle(scenes)
        # self.scene = next(self.scenes)
        
        self.scene = sceneList[0]
        self.scene.manager = self
        self.fading = None
        self.alpha = 0
        self.veil = pygame.Surface(pygame.display.get_surface().get_rect().size)
        self.veil.fill((0, 0, 0))

    def initScenes(self, scenes):
        scenesDict = [  [None,          scenes[1],      None,           None],
                        [scenes[0],     scenes[2],      scenes[3],      None],
                        [None,          scenes[5],      scenes[4],      scenes[6]],
                        [scenes[10],    scenes[9],      scenes[7],      scenes[8]],
                        [None,          scenes[11],     None,           None]]
        return scenesDict

    def nextScene(self):
        if not self.fading:
            self.fading = 'OUT'
            self.alpha = 0
        
    def renderNextScene(self, screen):
        if self.scene.nextRoom == "top":
            self.scene = self.scenes[self.scene.xMapIndex - 1][self.scene.yMapIndex]
        elif self.scene.nextRoom == "bottom":
            self.scene = self.scenes[self.scene.xMapIndex + 1][self.scene.yMapIndex]
        elif self.scene.nextRoom == "left":
            self.scene = self.scenes[self.scene.xMapIndex][self.scene.yMapIndex - 1]
        elif self.scene.nextRoom == "right":
            self.scene = self.scenes[self.scene.xMapIndex][self.scene.yMapIndex + 1]
        self.draw(screen)

    def pauseScene(self, screen):
        self.veil.set_alpha(100)
        screen.blit(self.veil, (0,0))

    def draw(self, screen):
        self.scene.render(screen)
        
    def update(self, screen, currentTime, events):
        fadeIncrement = 50
        self.scene.update(screen, currentTime, events)
        print(self.scene.roomNum)

        if self.fading == 'OUT':
            self.alpha += fadeIncrement
            if self.alpha >= 255:
                self.fading = 'IN'
                self.renderNextScene(screen)
        else:
            self.alpha -= fadeIncrement
            if self.alpha <= 0:
                self.fading = None
        
        if self.fading:
            self.veil.set_alpha(self.alpha)
            screen.blit(self.veil, (0, 0))