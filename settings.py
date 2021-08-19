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
        self.in_ball_colour = self.__colours.red
        self.out_ball_colour = self.__colours.black
        self.rod_colour = self.__colours.grey
        self.background = self.__colours.white
        self.winning_text_colour = self.__colours.gold
        self.losing_text_colour = self.__colours.blue
        self.regular_text_colour = self.__colours.black
        

        #Frame rate
        self.FPS = 60