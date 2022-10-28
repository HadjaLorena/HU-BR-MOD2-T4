from msilib.schema import Component
import random # gera valores aleatórios

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, images, y_pos): # y_pos -> atribui a posição específica para cada cacto na vertical
    
        self.images = images
        # tanto o small quanto o large cactus tem 3 imagens
        self.type = random.randint(0, 2) # gera números aleatórios entre 0 e 2
        # passando a lista das imagens para inicializar a classe "pai"
        super().__init__(self.images, self.type) # herda tudo da classe "pai" inclusive o draw (pega o que ele não tiver da classe "pai")

        self.rect.y = y_pos
        