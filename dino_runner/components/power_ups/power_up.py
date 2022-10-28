import random
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

#Y_POS = 200

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        

        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 5000)
        self.rect.y = random.randint(125, 175) #any position in y 
        #self.rect.y = Y_POS

        self.start_time = 0
        self.duration = random.randint(5, 10)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed

        if(self.rect.x < self.rect.width): # se o tamanho do rect.x for menor que da tela, então elimina o objeto
            power_ups.pop()
            self.rect.x = SCREEN_WIDTH + random.randint(800, 5000)
            self.rect.y = random.randint(125, 175) #any position in y 

    def draw(self, screen):
        screen.blit(self.image, self.rect)