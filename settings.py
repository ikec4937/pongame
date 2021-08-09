import pygame

from colours import Colours

class Settings:
    def __init__(self):
        self.__colours = Colours()
        
        #Display Settings
        self.DISP_W, self.DISP_H = 720, 480
        self.SIZE = self.DISP_W, self.DISP_H

        #Input buttons
        self.p1_up = pygame.K_w
        self.p1_down = pygame.K_s
        self.p2_up = pygame.K_UP
        self.p2_down = pygame.K_DOWN

        #Colour configurations
        self.player_box_colour = self.__colours.red
        self.random_box_colour = self.__colours.gold
        self.follow_box_colour = self.__colours.blue
        self.grid_colour = self.__colours.grey
        self.background = self.__colours.white
        

        #Frame rate
        self.FPS = 60