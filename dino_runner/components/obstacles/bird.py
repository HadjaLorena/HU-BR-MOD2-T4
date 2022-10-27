import pygame
from pygame import mixer
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, BIRD_SOUND

Y_POS_BIRD = 250

class Bird(Obstacle): # herda tudo da classe Obstacle
    def __init__(self, images):
        bird_sound = mixer.Sound(BIRD_SOUND) # o sound pode sobrepor a música de background
        bird_sound.play()
        self.type = 0
        self.images = BIRD

        super().__init__(images, self.type) # Volta para a classe "pai" inicializa do jeito que ela pede

      
        self.rect.y = Y_POS_BIRD
        self.fly_index = 0

    def draw(self, screen): # precisou de um draw próprio para ele, a classe "pai" era estatica e esse é dinâmico

        if(self.fly_index < 5): 
            image_index = 0 # procura na lista os valores (image index)
        else:
            image_index = 1
        
        screen.blit(self.images[image_index], (self.rect.x, self.rect.y)) # a cada meio segundo ele troca a imagem e atualiza a tela

        self.fly_index+= 1

        if(self.fly_index >=10): # reset
            self.fly_index = 0