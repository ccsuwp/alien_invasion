from pygame.sprite import Sprite


class MySprite(Sprite):
    def __init__(self):
        super().__init__()
        self.updated_x = 0
        self.updated_y = 0
        self.rect = None

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def update_rect(self):
        if abs(self.updated_x) >= 1:
            self.rect.x += self.updated_x
            self.updated_x = self.updated_x % 1
        if abs(self.updated_y) >= 1:
            self.rect.y += self.updated_y
            self.updated_y = self.updated_y % 1

