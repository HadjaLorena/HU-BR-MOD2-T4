import pygame

from dino_runner.utils.constants import GAME_FONT

class FontManager:
    def __init__(self, font_size, color = (0,0,0), FONT = GAME_FONT):

        self.font_size = font_size
        self.color = color
        self.FONT = FONT
        self.font = pygame.font.Font(self.FONT, self.font_size)