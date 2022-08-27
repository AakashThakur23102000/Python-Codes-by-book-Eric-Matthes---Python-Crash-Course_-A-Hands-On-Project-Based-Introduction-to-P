import sys
import pygame

from settings import Settings
from ship import Ship



class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        #initialize the setting class of setting.py
        self.settings = Settings()

        #create a display window, on which we’ll draw all the game’s graphical elements.
        #this is also known as surface.(self.screen)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #here we initialize ship class
        self.ship = Ship(self)

        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            #draw the ship on the screen by calling ship.blitme()
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
