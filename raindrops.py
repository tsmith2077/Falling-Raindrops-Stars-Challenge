import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """A class to represent a single raindrop."""
    
    def __init__(self, r_game):
        """Initialize the rain and set its starting position."""
        super().__init__()
        self.screen = r_game.screen
        self.settings = r_game.settings
        
        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        
        # Start each star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the star's exact horizontal position.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the rain down"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y