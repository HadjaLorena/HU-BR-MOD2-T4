import random
import pygame
from pygame.sprite import Sprite
# importando os sprites dos obstaculo

from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD, DINO_START, DINO_DEAD, GAME_OVER, SCREEN_HEIGHT

X_POSITION = 2
Y_POSITION = 2
Y_POS_SCORE = 1.5
Y_POS_DEATH_COUNT = 1.7
X_POS_DINO_DEAD = 4
Y_POS_DINO_DEAD = 3.8
Y_POS_GAME_OVER = 3
Y_POS_DINO_START = 3

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen.fill((255,255,255))
        self.font_size = 32
        self.color = (0,0,0)
        self.FONT = 'freesansbold.ttf'

        self.font = pygame.font.Font(self.FONT, self.font_size)
  
    def display_menu(self, count_death, score):
            
            if(count_death == 0):

                dino_start_image = DINO_START
                dino_start_rect = dino_start_image.get_rect()

                text = self.font.render("Press any key to start", True, self.color)
                text_rect = text.get_rect()

                # imagem do dino no início do game
                dino_start_rect.x = (SCREEN_WIDTH // X_POSITION) - (dino_start_rect.width // X_POSITION)
                dino_start_rect.y = (SCREEN_HEIGHT // Y_POS_DINO_START) - (dino_start_rect.height // Y_POS_DINO_START)

                self.screen.blit(dino_start_image, (dino_start_rect.x, dino_start_rect.y))


            # se o número de mortes for maior que 0 então entra no elif
            elif(count_death > 0):
                self.screen.fill((255,255,255))

                dino_dead_image = DINO_DEAD
                dino_dead_rect = dino_dead_image.get_rect()

                game_over_image = GAME_OVER
                game_over_rect = game_over_image.get_rect()
                
                text = self.font.render("Press any key to continue playing", True, self.color)
                text_rect = text.get_rect()

                score_text = self.font.render(f"Your Score: {score}", True, self.color)
                score_rect = score_text.get_rect() 

                death_count = self.font.render(f"Number of deaths: {count_death}", True, self.color)
                death_count_rect = death_count.get_rect()

                # pontuação
                score_rect.x = (SCREEN_WIDTH // X_POSITION) - (score_rect.width // X_POSITION)
                score_rect.y = (SCREEN_HEIGHT // Y_POS_SCORE) - (score_rect.height // Y_POS_SCORE)

                self.screen.blit(score_text, (score_rect.x, score_rect.y))

                # contagem de mortes
                death_count_rect.x = (SCREEN_WIDTH // X_POSITION) - (death_count_rect.width // X_POSITION)
                death_count_rect.y = (SCREEN_HEIGHT // Y_POS_DEATH_COUNT) - (death_count_rect.height // Y_POS_DEATH_COUNT)

                self.screen.blit(death_count, (death_count_rect.x, death_count_rect.y))

                # imagem do dino morto
                dino_dead_rect.x = (SCREEN_WIDTH // X_POS_DINO_DEAD) - (dino_dead_rect.width // X_POS_DINO_DEAD)
                dino_dead_rect.y = (SCREEN_HEIGHT // Y_POS_DINO_DEAD) - (dino_dead_rect.height // Y_POS_DINO_DEAD)

                self.screen.blit(dino_dead_image, (dino_dead_rect.x, dino_dead_rect.y))

                # imagem gamer over
                game_over_rect.x = (SCREEN_WIDTH // X_POSITION) - (game_over_rect.width // X_POSITION)
                game_over_rect.y = (SCREEN_HEIGHT // Y_POS_GAME_OVER) - (game_over_rect.height // Y_POS_GAME_OVER)

                self.screen.blit(game_over_image, (game_over_rect.x, game_over_rect.y))
                
            # texto do jogar novamente
            text_rect.x = (SCREEN_WIDTH // X_POSITION) - (text_rect.width // X_POSITION)
            text_rect.y = (SCREEN_HEIGHT // Y_POSITION) - (text_rect.height // Y_POSITION)

        
            self.screen.blit(text, (text_rect.x, text_rect.y))

            pygame.display.update()