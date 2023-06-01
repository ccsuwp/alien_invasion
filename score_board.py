import pygame.font


class ScoreBoard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (0, 0, 0)

    def draw(self):
        self.draw_current_score()
        self.draw_high_score()

    def draw_current_score(self):
        msg = str(self.settings.score[self.settings.game_level])
        image = self.font.render(msg, True, self.text_color, self.settings.bg_color)
        image_rect = image.get_rect()
        image_rect.top = self.screen.get_rect().top + 20
        image_rect.right = self.screen.get_rect().right - 20
        self.screen.blit(image, image_rect)

    def draw_high_score(self):
        msg = str(self.settings.max_score[self.settings.game_level])
        image = self.font.render(msg, True, self.text_color, self.settings.bg_color)
        image_rect = image.get_rect()
        image_rect.midtop = self.screen.get_rect().midtop
        image_rect.top += 20
        self.screen.blit(image, image_rect)

