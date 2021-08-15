import pygame

from settings import Settings

class Ball:
    def __init__(self, main, x, y, radius):
        self.main = main
        self.__settings = Settings()
        
        #Ball Properties
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = self.__settings.player_box_colour

        #Velocity
        self.velocity = 4

        #Direction - both variables takes integers.  
        self.x_direction = 0 #1 for left, 2 for right.
        self.y_direction = 0 #1 for up, 2 for down.
        
        #Bools?
        self.out_of_bounds = True
    
    def draw(self):
        pygame.draw.circle(self.main.WIN, self.colour, (self.x, self.y), (self.radius))
    
    def move_x(self):
        if self.x_direction == 1: 
            self.x -= self.velocity
        if self.x_direction == 2:
            self.x += self.velocity
        
    def move_y(self):
        if self.y_direction == 1:
            self.y -= self.velocity
        if self.y_direction == 2:
            self.y += self.velocity
    
    def get_oob(self):
        return self.out_of_bounds