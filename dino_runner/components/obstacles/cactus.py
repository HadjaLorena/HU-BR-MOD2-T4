import random # gera valores aleatórios

from dino_runner.components.obstacles.obstacle import Obstacle

Y_POS_CACTUS = 325

class Cactus(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0, 2) # gera números aleatórios entre 0 e 2
        super().__init__(images, self.type) # está enviando para a classe "pai"

        self.rect.y = Y_POS_CACTUS