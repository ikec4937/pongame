import pygame

from settings import Settings

class Rod:
    def __init__(self, main, x, y, width, height):
        self.main = main
        self.__settings = Settings()
        
        self.x = x
        self.y = y
        #Width and height should reasonably resemble a rectangle
        self.width = width
        self.height = height

        self.mov_sp = 2 #mov_sp = movement speed

    def draw(self, colour):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.main.WIN, colour, self.rect)
    
    def move_up(self):
        self.y -= self.mov_sp
    
    def move_down(self):
        self.y += self.mov_sp