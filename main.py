import pygame
import random

from settings import Settings
from ball import Ball
from rod import Rod

class Main:
    def __init__(self):
        self.__settings = Settings()
        self.__ball = Ball(self, self.__settings.C_WIDTH, self.__settings.C_HEIGHT, 12)
        #self.box = Box class initialised here
        self.__rod_p1 = Rod(self, 10, 50, 20, 150)
        self.__rod_p2 = Rod(self, self.__settings.DISP_W-(10*3), 50, 20, 150)
        self.WIN = pygame.display.set_mode((self.__settings.SIZE), 0, 32)
        
        self.started = False
    
    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.__settings.FPS)
            self._manage_ball()
            self._check_events()
            self._look_for_inputs()
            self._update_display()
            
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    
    def _look_for_inputs(self):
        keys = pygame.key.get_pressed()
        
        #Player 1 Movement
        if keys[self.__settings.p1_up]:
            self.__rod_p1.move_up()
        if keys[self.__settings.p1_down]:
            self.__rod_p1.move_down()
        
        #Player 2 movement
        if keys[self.__settings.p2_up]:
            self.__rod_p2.move_up()
        if keys[self.__settings.p2_down]:
            self.__rod_p2.move_down()
        
        if not self.started and keys[self.__settings.start_key]:
            self.started = True
            self.__ball.get_started()

    def _manage_ball(self):
        if self.started:
            self.__ball.move()
        if self.__ball.x <= 0 or self.__ball.x >= self.__settings.DISP_W: #If the ball's out of bounds,
            self.__ball.x, self.__ball.y = self.__settings.CENTRE #Centre it again
            self.started = False

    def _update_display(self):
        self.WIN.fill(self.__settings.background)
        self.__ball.draw(self.__settings.in_ball_colour)
        self.__rod_p1.draw(self.__settings.rod_colour)
        self.__rod_p2.draw(self.__settings.rod_colour)
        pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.run()