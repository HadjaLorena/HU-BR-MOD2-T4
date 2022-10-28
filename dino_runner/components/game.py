import pygame
from pygame import mixer

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BACKGROUND_MUSIC, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.cloud import Cloud
from dino_runner.components.menu import Menu
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        mixer.music.load(BACKGROUND_MUSIC) # o jogo começou, a música tem que começar a tocar
        mixer.music.play(-1) # musica em loop
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

        self.score = 0
        self.cloud = Cloud()
        self.menu = Menu(self.screen)
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

    # função principal para desenhar o tempo restante do power up na tela, utiliza da função draw_time_to_screen
    def draw_power_up_time(self):
        if(self.player.has_power_up):
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
           
            if(time_to_show >= 0):
                self.draw_time_to_screen(time_to_show)
                
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
    
    
    def draw_time_to_screen(self, time_to_show):
        
        font_size = 15
        color = (0,0,0)
        FONT = 'freesansbold.ttf'
        font = pygame.font.Font(FONT, font_size)
        
        text_to_display = f"Power up remaining time: {time_to_show}"
               
        text = font.render(text_to_display,True, color)
        text_rect = text.get_rect()
        
        text_rect.x = 850
        text_rect.y = 65
        self.screen.blit(text, (text_rect.x, text_rect.y))

    def display_menu(self):
        self.menu.display_menu(self.count_death, self.score)


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
        self.power_up_manager.update(self)

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
        self.power_up_manager.draw(self.screen)

        #draw score
        self.draw_score()
        # draw power_up remaining time
        self.draw_power_up_time()

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
