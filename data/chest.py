import pygame
from interactiveObject import InteractiveObject
class Chest(InteractiveObject):
    def __init__(self, contents, chestType):
        self.contents = contents
        self.type = chestType