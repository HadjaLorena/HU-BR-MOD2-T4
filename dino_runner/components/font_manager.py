import pygame

from dino_runner.utils.constants import GAME_FONT

class FontManager:
    def __init__(self, font_size):

        self.font_size = font_size
        self.color = (0,0,0)
        self.FONT = GAME_FONT
        self.font = pygame.font.Font(self.FONT, self.font_size)