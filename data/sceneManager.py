import pygame
from itertools import cycle
from time import sleep

class SceneManager(object):
    def __init__(self, scenes):
        for scene in scenes:
            scene.manager = self
        self.scenes = cycle(scenes)
        self.scene = next(self.scenes)
        self.scene.manager = self
        self.fading = None
        self.alpha = 0
        surfaceRect = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(surfaceRect.size)
        self.veil.fill((0, 0, 0))

    def nextScene(self):
        if not self.fading:
            self.fading = 'OUT'
            self.alpha = 0

    def pauseScene(self, screen):
        self.veil.set_alpha(100)
        screen.blit(self.veil, (0,0))

    def draw(self, screen):
        self.scene.render(screen)
        
    def update(self, screen, currentTime, events):
        fadeIncrement = 50
        self.scene.update(screen, currentTime, events)

        if self.fading == 'OUT':
            self.alpha += fadeIncrement
            if self.alpha >= 255:
                self.fading = 'IN'
                self.scene = next(self.scenes)
                self.draw(screen)
        else:
            self.alpha -= fadeIncrement
            if self.alpha <= 0:
                self.fading = None
        
        if self.fading:
            self.veil.set_alpha(self.alpha)
            screen.blit(self.veil, (0, 0))