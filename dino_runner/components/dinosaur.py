import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
Y_POS_DUCK = 340 # a imagem é mai baixa do que a do dino correndo

class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.jump_vel = JUMP_VEL

    def run(self):

        self.dino_rect.y = Y_POS

        if(self.step_index < 5): 
            self.image = RUNNING[0] 
        else:
            self.image = RUNNING[1]

        self.step_index+=1

    def update(self, user_input):

        if(self.step_index >=10):
            self.step_index = 0

        if(self.dino_run):
            self.run()
        elif(self.dino_jump):
            self.jump()
        elif(self.dino_duck):
            self.duck()

        # própria função do pygame (pygame.K_UP) --> manda a seta para cima e o dinossauro pula
        if(user_input[pygame.K_UP] and not self.dino_jump):
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif(not self.dino_jump):
            self.dino_jump = False
            self.dino_run = True
            
        # adicionei o comando do próprio pygame para o dinossauro abaixar
        if(user_input[pygame.K_DOWN] and not self.dino_jump):
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        # ambos não estão acontecendo (permite que a primeira ação depois de run seja o jump)
        elif(not self.dino_duck and not self.dino_jump):
            self.dino_jump = False
            self.dino_run = True   
            self.dino_duck = False


    def jump(self):
        self.image = JUMPING

        if(self.dino_jump):
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if(self.jump_vel < -JUMP_VEL):
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def duck(self): #ATIVIDADE: DESENVOLVER O MÉTODO e fazer toda a atuazlizacao do novo codigo
        self.image = DUCKING

        if(self.step_index < 5):
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]
        
        self.step_index+= 1

        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK

     
          