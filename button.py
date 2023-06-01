import pygame.font


class Button:
    def __init__(self, ai_game, msg, button_color, position_offset):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = button_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y += position_offset * self.rect.height + 10

        self.msg = msg

    def draw_button(self):
        msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        msg_image_rect = msg_image.get_rect()
        msg_image_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(msg_image, msg_image_rect)
