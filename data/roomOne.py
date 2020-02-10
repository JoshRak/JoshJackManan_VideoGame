import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from time import sleep
from pygame.locals import *

class RoomOne(Scene):
    def __init__(self, sceneMap, entities):
        super(RoomOne, self).__init__(1, sceneMap, entities)
        
        # build the room

    def render(self, screen):
        for entity in self.entities:
            entity.draw(screen)

    def update(self, currentTime):
        keys = pygame.key.get_pressed()
        self.player.update(keys, currentTime)

    # def exit(self):
    #     if self.roomNum+1 in rooms:
    #         self.manager.go_to(GameScene(self.roomNum+1))
    #     else:
    #         self.manager.go_to(CustomScene("You win!"))

    # def die(self):
    #     self.manager.go_to(CustomScene("You lose!"))

    def handle_events(self, events):
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.manager.go_to(TitleScene())
