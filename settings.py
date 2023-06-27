class Settings():
    """Class for all game settings "Alien Invasion"."""
    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (120, 60, 60)

        self.bullet_allowed = 15

        # Alein settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
