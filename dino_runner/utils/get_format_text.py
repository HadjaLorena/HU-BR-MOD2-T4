import pygame

class get_format_text:
    def __init__(self):
        #print("Display menu")
        self.screen.fill((255,255,255))

        #melhorar o codigo para nao repetir
        font_size = 32
        color = (0,0,0)
        FONT = 'freesansbold.ttf'

        font = pygame.font.Font(FONT, font_size)