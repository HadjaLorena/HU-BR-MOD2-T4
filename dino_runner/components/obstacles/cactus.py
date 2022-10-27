from msilib.schema import Component
import random # gera valores aleatórios

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

Y_POS_SMALL_CACTUS = 325
Y_POS_LARGE_CACTUS = 300

class Cactus(Obstacle):
    def __init__(self): # y_pos -> atribui a posição específica para cada cacto na vertical
        
        self.cactus_type = random.randint(0, 1) # chamo o objeto cactus e faço um random
        self.images = [] # criei uma lista de imagens inicializada como vazia
        self.cactus_position = 0 # variável que cuida da posiçao do cactus

        if(self.cactus_type == 0): # se random for igual a 0 então é criado um small cactus
            self.images = SMALL_CACTUS
            self.cactus_position = Y_POS_SMALL_CACTUS
        else: # se random for 1 é criado um large cactus
            self.images = LARGE_CACTUS
            self.cactus_position = Y_POS_LARGE_CACTUS

        # tanto o small quanto o large cactus tem 3 imagens
        self.type = random.randint(0, 2) # gera números aleatórios entre 0 e 2
        # passando a lista das imagens para inicializar a classe "pai"
        super().__init__(self.images, self.type) # herda tudo da classe "pai" inclusive o draw (pega o que ele não tiver da classe "pai")

        self.rect.y = self.cactus_position
        