import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DINO_DEAD, GAME_OVER, DINO_START
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.cloud import Cloud
#from dino_runner.utils.get_format_text import get_format_text

X_POSITION = 2
Y_POSITION = 2
Y_POS_SCORE = 1.5
Y_POS_DEATH_COUNT = 1.7
X_POS_DINO_DEAD = 4
Y_POS_DINO_DEAD = 3.8
Y_POS_GAME_OVER = 3
Y_POS_DINO_START = 3


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = 0
        self.cloud = Cloud()

        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False

        self.count_death = 0

        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def execute(self):
        self.executing = True

        while(self.executing):
            self.display_menu()

        pygame.display.quit()
        pygame.quit()

    def display_menu(self):
        #print("Display menu")
        self.screen.fill((255,255,255))

        #melhorar o codigo para nao repetir
        font_size = 32
        color = (0,0,0)
        FONT = 'freesansbold.ttf'

        font = pygame.font.Font(FONT, font_size)

        if(self.count_death == 0):

            dino_start_image = DINO_START
            dino_start_rect = dino_start_image.get_rect()

            text = font.render("Press any key to start", True, color)
            text_rect = text.get_rect()

            # imagem do dino no início do game
            dino_start_rect.x = (SCREEN_WIDTH // X_POSITION) - (dino_start_rect.width // X_POSITION)
            dino_start_rect.y = (SCREEN_HEIGHT // Y_POS_DINO_START) - (dino_start_rect.height // Y_POS_DINO_START)

            self.screen.blit(dino_start_image, (dino_start_rect.x, dino_start_rect.y))


        # se o número de mortes for maior que 0 então entra no elif
        elif(self.count_death > 0):

            dino_dead_image = DINO_DEAD
            dino_dead_rect = dino_dead_image.get_rect()

            game_over_image = GAME_OVER
            game_over_rect = game_over_image.get_rect()
            
            text = font.render("Press any key to continue playing", True, color)
            text_rect = text.get_rect()

            score_text = font.render(f"Your Score: {self.score}", True, color)
            score_rect = score_text.get_rect() 

            death_count = font.render(f"Number of deaths: {self.count_death}", True, color)
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

        # para atualizar para visualizar

        pygame.display.update()

        self.events_on_menu()

    def events_on_menu(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.playing = False
                self.executing = False
            if(event.type == pygame.KEYDOWN):
                self.reset()
                self.run()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.update(self.game_speed)
        self.obstacle_manager.update(self)

        self.update_score()
        self.update_game_speed()

    def update_score(self):
        self.score += 1
        
    def update_game_speed(self):
        if(self.score % 100 == 0):
            self.game_speed += 5

    def reset(self):
        self.score = 0
        self.game_speed = 20
        self.obstacle_manager.reset_obstacle()
    
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        #draw score
        self.draw_score()

        pygame.display.update()
        pygame.display.flip()

# adicionado na aula 26/10/2022
    def draw_score(self):
       # print(self.score)
        font_size = 32
        color = (0,0,0)
        FONT = 'freesansbold.ttf'

        font = pygame.font.Font(FONT, font_size)
        text = font.render(f"Score: {self.score}", True, color)

        score_text_rect = text.get_rect()
        score_text_rect.x = 850
        score_text_rect.y = 30

        self.screen.blit(text, (score_text_rect.x, score_text_rect.y))

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
