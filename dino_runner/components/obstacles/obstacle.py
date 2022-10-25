import pygame
from pygame.sprite import Sprite 
# importando os sprites dos obstaculo

from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite): # questão de herança (reutilização de código) -> herda todas as funções de outra classe e passam a ser do mesmo tipo, um sub tipo da primeira classe
    def __init__(self, images, type): # recebe um conjunto de imagem e as imagens que quer mostar
        self.images = images
        self.type = type

        self.rect = self.images[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed # se move com o background

        if(self.rect.x <- self.rect.width):
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
