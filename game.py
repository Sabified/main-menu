import pygame
import os
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False

        self.UP_KEY, self.DOWN_KEY, self.LEFT_KEY, self.RIGHT_KEY, self.SELECT_KEY, self.BACK_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 900, 500

        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        pygame.display.set_caption("Main Menu")
        
        self.sel1 = pygame.mixer.Sound(os.path.join('assets', 'Select1.wav'))
        self.sel3 = pygame.mixer.Sound(os.path.join('assets', 'Select3.wav'))
        self.sel5 = pygame.mixer.Sound(os.path.join('assets', 'Select5.wav'))
        self.hit3 = pygame.mixer.Sound(os.path.join('assets', 'Hit3.wav'))

        self.soundVolume = 1.0

        self.channel = pygame.mixer.find_channel(True)
        self.channel.set_volume(self.soundVolume)

        self.font_name = os.path.join('assets', '8-BIT WONDER.TTF')
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.volume_menu = VolumeMenu(self)
        self.credits_menu = CreditsMenu(self)

        self.curr_menu = self.main_menu
    
    def game_loop(self):
        while self.playing:
            self.check_events()
            self.channel.set_volume(VolumeMenu(game).volVar)
            if self.SELECT_KEY:
                self.playing = False
            
            self.display.fill(self.BLACK)
            self.draw_text("Thanks for Playing", 50, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()

            self.reset_keys()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.SELECT_KEY = True
                elif event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                elif event.key == pygame.K_UP:
                    self.UP_KEY = True
                elif event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                elif event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                    
    
    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.SELECT_KEY = False
        self.BACK_KEY = False


    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        
        self.display.blit(text_surface, text_rect)