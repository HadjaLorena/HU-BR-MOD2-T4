import random
import pygame
from pygame.sprite import Sprite
# importando os sprites dos obstaculo

from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD

class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
 
 
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(100, 500)
        self.rect.y = random.randint(50, 150) # permite a criação da nuvem em alturas aleatórias

    def update(self, game_speed):
        self.rect.x -= game_speed # se move com o background

        if(self.rect.x < -self.rect.width):
            self.rect.x = SCREEN_WIDTH + random.randint(500, 1500)
            self.rect.y = random.randint(50, 150)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))