import pygame
from itertools import cycle
from time import sleep

class SceneManager(object): # a class to hold the data of all the running scenes to display from the main program

    def __init__(self, sceneList, playerIsHacker): # intialize the object with all the necessary data
        self.playerIsHacker = playerIsHacker
        self.scenes = self.initScenes(sceneList) 
        for scene in sceneList:
            x = [x for x in self.scenes if scene in x][0]
            scene.xMapIndex = self.scenes.index(x)
            scene.yMapIndex = x.index(scene)
            scene.manager = self
        # self.scenes = cycle(scenes)
        # self.scene = next(self.scenes)
        if self.playerIsHacker:
            self.scene = sceneList[0]
        else:
            self.scene = sceneList[1]
        self.scene.manager = self
        self.fading = None
        self.alpha = 0
        self.veil = pygame.Surface(pygame.display.get_surface().get_rect().size)
        self.veil.fill((0, 0, 0))

    def renderOpeningScene(self, screen, openingSceneImg): # display the opening scene
        screen.blit(openingSceneImg, (0,0))

    def processSelection(self, screen, selection): # process the selection of operating system
        if selection == "./Assets/Images/selectionSceneMac.png":
            screen.blit(pygame.transform.scale(pygame.image.load("./Assets/Images/selectionSceneMacError.png").convert_alpha(), (448,480)), (0,0))
            val = True
            while val:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        val = False
            return False
        return True

    def renderSelectionScene(self, screen, selectionScenes, events): # display the selection scenes for operating system
        selectionScenesCycle = cycle(selectionScenes)
        selectedScene = next(selectionScenesCycle)

        for event in events:
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                selectedScene = next(selectionScenesCycle)
                selectedScene = next(selectionScenesCycle)
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                selectedScene = next(selectionScenesCycle)
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN):
                if self.processSelection(screen, selectedScene):
                    return False
                else:
                    continue

        screen.blit(pygame.transform.scale(pygame.image.load(selectedScene).convert_alpha(), (448,480)), (0,0))

    def renderClosingScene(self, screen, closingSceneImg): # display the closing scene
        screen.blit(closingSceneImg, (0,0))

    def initScenes(self, scenes): # initalize the map scene
        scenesDict = [  [None,          scenes[1],      None,           None],
                        [scenes[0],     scenes[2],      scenes[3],      None],
                        [None,          scenes[5],      scenes[4],      scenes[6]],
                        [scenes[10],    scenes[9],      scenes[7],      scenes[8]],
                        [None,          scenes[11],     None,           None]]
        return scenesDict

    def nextScene(self): # move to the nect scene
        if not self.fading:
            self.fading = 'OUT'
            self.alpha = 0
        
    def renderNextScene(self, screen): # change the scene to the next scene in the map
        if self.scene.nextRoom == "top":
            self.scene = self.scenes[self.scene.xMapIndex - 1][self.scene.yMapIndex]
        elif self.scene.nextRoom == "bottom":
            self.scene = self.scenes[self.scene.xMapIndex + 1][self.scene.yMapIndex]
        elif self.scene.nextRoom == "left":
            self.scene = self.scenes[self.scene.xMapIndex][self.scene.yMapIndex - 1]
        elif self.scene.nextRoom == "right":
            self.scene = self.scenes[self.scene.xMapIndex][self.scene.yMapIndex + 1]
        print (self.scene)
        self.draw(screen)

    def pauseScene(self, screen): # make the screen darker to pause the scene
        self.veil.set_alpha(100)
        screen.blit(self.veil, (0,0))

    def draw(self, screen): # dispaly the scene on the screen
        self.scene.render(screen)
        
    def update(self, screen, currentTime, events): # fade out from the previous scene and fade in tot he next scenes
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