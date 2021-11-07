import pygame
import random

from settings import Settings

class Ball:
    def __init__(self, main, x, y, radius):
        self.main = main
        self.__settings = Settings()
        
        #Ball Properties
        self.x = x
        self.y = y
        self.radius = radius

        #Velocity
        self.velocity = 4

        #Direction - both variables takes integers.  
        self.x_direction = 0 #1 for left, 2 for right.
        self.y_direction = 0 #1 for up, 2 for down.
        
        #Bools?
        self.out_of_bounds = True
    
    def draw(self, colour):
        pygame.draw.circle(self.main.WIN, colour, (self.x, self.y), (self.radius))
        rect = pygame.Rect(self.x-self.radius, self.y-self.radius, 2*self.radius, 2*self.radius)
        self.boundary = pygame.draw.rect(self.main.WIN, (0,0,0), rect, 1)

    
    def move(self):
        if self.x_direction == 1: 
            self.x -= self.velocity
        if self.x_direction == 2:
            self.x += self.velocity
        if self.y_direction == 1:
            self.y -= self.velocity
        if self.y_direction == 2:
            self.y += self.velocity
        
        #To bounce from the walls
        if self.y <= 0:
            self.y_direction = 2
        elif self.y >= (self.__settings.DISP_H - self.radius):
            self.y_direction = 1
    
    def get_oob(self):
        return self.out_of_bounds
    
    def get_started(self):
        if self.main.started:
            self.x_direction = random.randint(1, 2)
            self.y_direction = random.randint(1, 2)
