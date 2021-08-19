import pygame

from settings import Settings
from ball import Ball
from rod import Rod

class Main:
    def __init__(self):
        self.__settings = Settings()
        self.__ball = Ball(self, self.__settings.DISP_W/2, self.__settings.DISP_H/2, 12)
        #self.box = Box class initialised here
        self.__rod_p1 = Rod(self, 10, 50, 20, 150)
        self.__rod_p2 = Rod(self, self.__settings.DISP_W-(10*3), 50, 20, 150)
        self.WIN = pygame.display.set_mode((self.__settings.SIZE), 0, 32)
    
    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.__settings.FPS)
            self._check_events()
            self._look_for_inputs()
            self._update_display()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    
    def _look_for_inputs(self):
        pass

    def _update_display(self):
        self.WIN.fill(self.__settings.background)
        self.__ball.draw(self.__settings.in_ball_colour)
        self.__rod_p1.draw(self.__settings.rod_colour)
        self.__rod_p2.draw(self.__settings.rod_colour)
        pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.run()