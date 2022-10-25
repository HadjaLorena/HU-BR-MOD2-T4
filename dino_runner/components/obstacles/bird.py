
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

Y_POS_BIRD = 250

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type) # está enviando para a classe "pai"

        self.rect.y = Y_POS_BIRD
        self.index = 0

    def fly(self):
        self.image = BIRD

        if(self.step_index < 5):
            self.image = BIRD[0]
        else:
            self.image = BIRD[1]
        
        self.step_index+= 1