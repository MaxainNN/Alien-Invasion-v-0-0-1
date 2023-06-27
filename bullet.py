import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for control bullet from ship"""

    def __init__(self, ai_game):
        """Create bullet object in current position of the ship."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create bullet in position (0, 0) and declare right position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet position in float
        self.y = float(self.rect.y)

    def update(self):
        """Remove bullet up to screen."""
        # Refresh bullet position in float
        self.y -= self.settings.bullet_speed
        # Refresh triangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """Output bullet on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
