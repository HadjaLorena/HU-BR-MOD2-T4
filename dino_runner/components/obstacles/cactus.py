import random # gera valores aleatórios

from dino_runner.components.obstacles.obstacle import Obstacle

#Y_POS_CACTUS = 325
#Y_POS_LARGE_CACTUS = 300

class Cactus(Obstacle):
    def __init__(self, images, y_pos): # y_pos -> atribui a posição específica para cada cacto na vertical
        self.type = random.randint(0, 2) # gera números aleatórios entre 0 e 2
        super().__init__(images, self.type) # herda tudo da classe "pai" inclusive o draw (pega o que ele não tiver da classe "pai")

        self.rect.y = y_pos