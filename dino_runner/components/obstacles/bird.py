
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

Y_POS_BIRD = 250

class Bird(Obstacle): # herda tudo da classe Obstacle
    def __init__(self, images):
        self.type = 0
        self.image = BIRD

        super().__init__(images, self.type) # Volta para a classe "pai" inicializa do jeito que ela pede

      
        self.rect.y = Y_POS_BIRD
        self.fly_index = 0

    def draw(self, screen): # precisou de um draw próprio para ele, a classe "pai" era estatica e esse é dinâmico

        if(self.fly_index < 5): 
            self.image = 0
        else:
            self.image = 1
        
        screen.blit(self.images[self.image], (self.rect.x, self.rect.y)) # a cada meio segundo ele troca a imagem e atualiza a tela

        self.fly_index+= 1

        if(self.fly_index >=10): # reset
            self.fly_index = 0