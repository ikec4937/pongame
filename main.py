import pygame

from settings import Settings
from ball import Ball

class Main:
    def __init__(self):
        self.__settings = Settings()
        self.__ball = Ball()
        #self.box = Box class initialised here
        #self.rod = Rod class initialised here
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
        pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.run()