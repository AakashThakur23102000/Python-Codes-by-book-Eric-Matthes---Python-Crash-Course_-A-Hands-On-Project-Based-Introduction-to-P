import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color


        # Create a bullet rect at (0, 0) and then set correct position.
        #we use  pygame.Rect to build rect from scratch and then we allot 0,0 cordeinate.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        #here we match ship's midtop postion to bullets to creat effect that bullet comes from ship
        self.rect.midtop = ai_game.ship.rect.midtop


        # Store the bullet's position as a decimal value.
        #here we store bullets y cordinate so that we can do adjustment with bullet's spped 
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect(bullet) position by updating y cordinate.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
