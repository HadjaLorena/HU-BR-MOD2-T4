import random
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, SHIELD_TYPE

Y_POS = 200

class PowerUp(Sprite):
    def __init__(self, image):
        self.image = image
        self.type = SHIELD_TYPE

        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = Y_POS

        self.start_time = 0
        self.duration = random.randint(125, 175)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed

        if(self.rect.x < self.rect.width): # se o tamanho do rect.x for menor que da tela, então elimina o objeto
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)