import pygame

class Ship():
    """Class for control ship."""
    def __init__(self, ai_game):
        """Intialize ship and seting it start position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Every new ship spawn at bottom edge of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Save coords middle of ship
        self.x = float(self.rect.x)

        # Shift flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Refresh position of ship considering the flag."""
        # Refresh atribute x, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Refresh artibute rect according self.x
        self.rect.x = self.x

    def blitme(self):
        """Drawing ship in current position."""
        self.screen.blit(self.image, self.rect)
