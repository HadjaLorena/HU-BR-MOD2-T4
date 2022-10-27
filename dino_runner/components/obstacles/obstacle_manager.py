import pygame

import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if(len(self.obstacles) == 0):

            obstacle_type_index = random.randint(0, 1)

            if(obstacle_type_index == 0):
                self.obstacles.append(Cactus()) # adicionando um cactus e para criar um cactus estou enviando uma imagem
            #elif(obstacle_type_index == 1):
                #self.obstacles.append(Cactus (LARGE_CACTUS, Y_POSITION_LARGE_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            #manage the collision
            if(game.player.dino_rect.colliderect(obstacle.rect)):
                game.playing = False
                game.count_death += 1
                pygame.time.delay(500)
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles = []