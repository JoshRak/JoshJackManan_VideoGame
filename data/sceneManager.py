import pygame
from itertools import cycle
from time import sleep

class SceneManager(object):
    def __init__(self, scenes):
        self.scenes = cycle(scenes)
        self.scene = next(self.scenes)
        self.fading = None
        self.alpha = 0
        sr = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0, 0, 0))

    def nextScene(self):
        if not self.fading:
            self.fading = 'OUT'
            self.alpha = 0

    def draw(self, screen):
        self.scene.render(screen)
        if self.fading:
            self.veil.set_alpha(self.alpha)
            screen.blit(self.veil, (0, 0))
    
    def drawImage(self, screen, image, point):
        while self.alpha <= 255:
            self.veil.set_alpha(self.alpha) 
            sleep(0.01)
        screen.blit(self.veil, point)
        self.fading = 'IN'

    def update(self, currentTime, events):
        self.scene.update(currentTime, events)

        if self.fading == 'OUT':
            self.alpha += 10
            if self.alpha >= 255:
                self.fading = 'IN'
                self.scene = next(self.scenes)
        else:
            self.alpha -= 10
            if self.alpha <= 0:
                self.fading = None
