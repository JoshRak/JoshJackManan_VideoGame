# import pygame
import textboxify

class DialogBox(object):
    def __init__(self, text, color, size, background):
        self.dialogBox = textboxify.TextBoxFrame(text = text, text_width = 320,
                    lines = 2, pos = (50, 120), padding = (150,100), font_color = color,
                    font_size = size, bg_color = background)
        self.dialogBox.set_indicator()

    def render(self, position, screen):
        screen.blit(self.dialogBox, position)