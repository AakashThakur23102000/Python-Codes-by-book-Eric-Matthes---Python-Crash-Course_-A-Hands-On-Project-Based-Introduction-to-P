#all the ship setting is done here
#here we import pygame
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        #creating ship screen
        self.screen = ai_game.screen


        self.setting = ai_game.settings



        
        #converting screen to rectangle
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        #converting image to rectangle
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom


        # Store a decimal value for the ship's horizontal position.#image position
        self.x = float(self.rect.x)
        

        ## Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag. and also we limit the values inside the pixles"""
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left == True and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
