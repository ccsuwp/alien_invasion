import pygame
from my_sprite import MySprite


class Alien(MySprite):
    def __init__(self, ai_game):
        super().__init__()
        self.game_status = ai_game.game_status
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.move_left = True
        self.move_down = True

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.move_right:
            self.updated_x += self.game_status.alien_speed_x
        if self.move_left:
            self.updated_x -= self.game_status.alien_speed_x
        if self.move_down:
            self.updated_y += self.settings.alien_speed_y

        self.update_rect()

    @staticmethod
    def get_rect():
        return pygame.image.load("./images/alien.bmp").get_rect()
