import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        #initialize the setting class of setting.py
        self.settings = Settings()

        #create a display window, on which we’ll draw all the game’s graphical elements.
        ''' old way to set screen size
        #this is also known as surface.(self.screen)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        '''
        #set screen size at full screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        
        pygame.display.set_caption("Alien Invasion")

        #here we initialize ship image class
        self.ship = Ship(self)
        #here we initialize bullet class
        self.bullets = pygame.sprite.Group()

        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #_check_events method calling inside a old method run_game #helper method after Refactoring 
            self._check_events()

            #update ship moments by calling update method in ship.py
            self.ship.update()

            #It calls bullet.update() for each bullet we place in the group bullets.
            self.bullets.update()

            #_update_screen method is called which hels to update scrren status #helper method after Refactoring 
            self._update_screen()
            
            


    #creates diffrent methods for events and scren update after refactoring
    def _check_events(self):
        # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #here we check if keybord key is pressed down by user by keydown and then it trues the self.moving_right and relases by keyup it then false the self.moving_right
                elif event.type == pygame.KEYDOWN:
                    #calling helper keydown method and passing event argument
                    self._check_keydown_events(event)
                        
                elif event.type == pygame.KEYUP:
                    #calling helper keydown method and passing event argument
                    self._check_keyup_events(event)
                    
    #we do refraction for keyup and key down here by creating helper class
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        #here we also add quiting by pressing "Q"
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
                        



    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        #draw the ship on the screen by calling ship.blitme() method
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
