import sys
import pygame

from rain_settings import Settings
from raindrops import Rain

class RaindropsGame:
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("13-3/12-4 Raindrops Challenge(Falling Stars)")
        
        self.raindrops = pygame.sprite.Group()
        self._create_drops()
        
    def run_game(self):
        while True: 
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()

            self.raindrops.update()
            self._update_drops()
            self._update_screen()
            
            pygame.display.flip()
            
    def _create_drops(self):
        # Create a raindrop and find the number of raindrops in a row.
        # Spacing between each raindrop is equal to one drop width.
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - drop_width
        number_drops_x = available_space_x // (2 * drop_width)
        
        # Determine the number of rows of raindrops that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * drop_height)
                
        # Create the rows of raindrops.
        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self._create_drop(drop_number, row_number)
        
    def _create_drop(self, drop_number, row_number):    
        # Create a raindrop and place it in the row.
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = drop_width + 2 * drop_width * drop_number
        drop.y = 2 * drop.rect.height * row_number
        drop.rect.y = drop.y
        self.raindrops.add(drop)
     
    def _create_drop_top(self):
        # Create a raindrop and find the number of raindrops in a row.
        # Spacing between each raindrop is equal to one drop width.
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - drop_width
        number_drops_x = available_space_x // (2 * drop_width)
                
        # Create the rows of raindrops.
        for drop_number in range(number_drops_x):
            self._create_drop(drop_number, row_number=0) 
        
    def _update_drops(self):
        """Delete raindrops that go off screen"""
        for drop in self.raindrops.copy():
            if drop.rect.top >= 800:
                self.raindrops.remove(drop)
                
            if drop.rect.top >= 800:
                drop = Rain(self) 
                drop_width, drop_height = drop.rect.size
                available_space_x = self.settings.screen_width - drop_width
                number_drops_x = available_space_x // (2 * drop_width)
                
                self._create_drop_top()
        
    def _update_screen(self):    
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        
        pygame.display.flip()
            
if __name__ == '__main__':
    r_game = RaindropsGame()
    r_game.run_game()
                