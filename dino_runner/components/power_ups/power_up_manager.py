from turtle import Screen
from dino_runner.components.power_ups.shield import Shield


class PowerUpManager:
    def __init__(self):
        self.power_ups = []

    def update(self, game):

        if(len(self.power_ups) == 0):
            self.power_ups.append(Shield(Screen))

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            #add the code to the collision
            if(game.player.dino_rect.colliderect(power_up.rect)):
                game.player.has_shield = True
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)

                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_up(self):
        self.power_ups = []