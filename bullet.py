import pygame
from my_sprite import MySprite


class Bullet(MySprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.Surface((self.settings.bullet_width,
                                     self.settings.bullet_height))
        self.image.fill(self.settings.bullet_color)
        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.sprites()[0].rect.midtop

    def update(self):
        self.updated_y -= self.settings.bullet_speed
        self.update_rect()

