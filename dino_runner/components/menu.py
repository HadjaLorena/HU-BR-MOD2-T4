import random

import pygame
from pygame.sprite import Sprite
# importando os sprites dos obstaculo

from dino_runner.utils.constants import SCREEN_WIDTH, DINO_START, DINO_DEAD, GAME_OVER, SCREEN_HEIGHT
from dino_runner.components.font_manager import FontManager

X_POSITION = 2
Y_POSITION = 2
Y_POS_SCORE = 1.5
Y_POS_DEATH_COUNT = 1.7
X_POS_DINO_DEAD = 4
Y_POS_DINO_DEAD = 3.8
Y_POS_GAME_OVER = 3
Y_POS_DINO_START = 3
Y_POS_RULES = 1.8

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen.fill((255,255,255))
       
        self.start_menu_font = FontManager(40)

    def display_rules(self):

        rules_title = self.start_menu_font.font.render("- RULES -", True, self.start_menu_font.color)
        rules_title_rect = rules_title.get_rect()

        rules_1 = self.start_menu_font.font.render("1. Avoid obstacles to survive", True, self.start_menu_font.color)
        rules_1_rect = rules_1.get_rect()

        rules_2 = self.start_menu_font.font.render("2. Power ups have a time limit", True, self.start_menu_font.color)
        rules_2_rect = rules_2.get_rect()

        rules_3 = self.start_menu_font.font.render("3. Hammers don't work with birds", True, self.start_menu_font.color)
        rules_3_rect = rules_3.get_rect()

        rules_4 = self.start_menu_font.font.render("4. Shields protect you from obstacles", True, self.start_menu_font.color)
        rules_4_rect = rules_4.get_rect()

        rules_title_rect.x = (SCREEN_WIDTH // X_POSITION) - (rules_title_rect.width // X_POSITION)
        rules_title_rect.y = (SCREEN_HEIGHT // Y_POS_SCORE) - (rules_title_rect.height // Y_POS_SCORE)

        self.screen.blit(rules_title, (rules_title_rect.x, rules_title_rect.y))

        self.screen.blit(rules_1, ((rules_title_rect.x - 175), (rules_title_rect.y + 30)))
        self.screen.blit(rules_2, ((rules_title_rect.x - 175), (rules_title_rect.y + 60)))
        self.screen.blit(rules_3, ((rules_title_rect.x - 200), (rules_title_rect.y + 90)))
        self.screen.blit(rules_4, ((rules_title_rect.x - 240), (rules_title_rect.y + 120)))


    def display_menu(self, count_death, score):
            
            if(count_death == 0):

                dino_start_image = DINO_START
                dino_start_rect = dino_start_image.get_rect()

                text = self.start_menu_font.font.render("Press any key to start", True, self.start_menu_font.color)
                text_rect = text.get_rect()

                rules_option_text = self.start_menu_font.font.render("Or press 0 to see the rules", True, self.start_menu_font.color)
                rules_option_text_rect = rules_option_text.get_rect()

                # imagem do dino no início do game
                dino_start_rect.x = (SCREEN_WIDTH // X_POSITION) - (dino_start_rect.width // X_POSITION)
                dino_start_rect.y = (SCREEN_HEIGHT // Y_POS_DINO_START) - (dino_start_rect.height // Y_POS_DINO_START)

                self.screen.blit(dino_start_image, (dino_start_rect.x, dino_start_rect.y))

                rules_option_text_rect.x = (SCREEN_WIDTH // X_POSITION) - (rules_option_text_rect.width // X_POSITION)
                rules_option_text_rect.y = (SCREEN_HEIGHT // Y_POS_RULES) - (rules_option_text_rect.height // Y_POS_RULES)

                self.screen.blit(rules_option_text, (rules_option_text_rect.x, rules_option_text_rect.y))


            # se o número de mortes for maior que 0 então entra no elif
            else:
                self.screen.fill((255,255,255))

                dino_dead_image = DINO_DEAD
                dino_dead_rect = dino_dead_image.get_rect()

                game_over_image = GAME_OVER
                game_over_rect = game_over_image.get_rect()
                
                text = self.start_menu_font.font.render("Press any key to continue playing", True, self.start_menu_font.color)
                text_rect = text.get_rect()

                score_text = self.start_menu_font.font.render(f"Your Score: {score}", True, self.start_menu_font.color)
                score_rect = score_text.get_rect() 

                death_count = self.start_menu_font.font.render(f"Number of deaths: {count_death}", True, self.start_menu_font.color)
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