import pygame.image
from my_sprite import MySprite


class Ship(MySprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.ship_centre()

        self.settings = ai_game.settings

    def update(self):
        if self.move_up and self.screen_rect.top <= self.rect.top:
            self.updated_y -= self.settings.ship_speed
        if self.move_down and self.screen_rect.bottom >= self.rect.bottom:
            self.updated_y += self.settings.ship_speed
        if self.move_left and self.screen_rect.left <= self.rect.left:
            self.updated_x -= self.settings.ship_speed
        if self.move_right and self.screen_rect.right >= self.rect.right:
            self.updated_x += self.settings.ship_speed
        self.update_rect()

    def ship_centre(self):
        self.rect.midbottom = self.screen_rect.midbottom
