import random

import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer



class PowerUpManager:
    def __init__(self):
        self.power_ups = []

        self.power_type = 0

    def generate_power_up(self, score):

        if(len(self.power_ups) == 0):
            self.power_type = random.randint(0, 1)

            if(self.power_type == 0):
                self.power_ups.append(Shield())

            else:
                self.power_ups.append(Hammer())

    def update(self, game):

        self.generate_power_up(game.score)

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

       
            #add the code to the collision
            if(game.player.dino_rect.colliderect(power_up.rect)):
                power_up.start_time = pygame.time.get_ticks() #getting the time that the application is running

                if(self.power_type == 0):
                    game.player.has_shield = True
                    game.player.has_hammer = False
                else:
                    game.player.has_shield = False
                    game.player.has_hammer = True

                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)

                self.power_ups.remove(power_up)
        
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_up(self):
        self.power_ups = []
    