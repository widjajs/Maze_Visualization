import pygame
import sys
from maze_generator import muted_gold, charcoal_gray, dusty_rose, powder_blue


class Button:
    def __init__(self, x, y, width, height, msg, id):
        self.button_id = id
        self.rect = pygame.Rect(x, y, width, height)
        self.button_font = pygame.font.Font(None, 36)
        self.button_text = self.button_font.render(msg, True, charcoal_gray)
        self.base_color = muted_gold
        self.hover_color = dusty_rose
        self.text_color = charcoal_gray
        self.active_color = dusty_rose
        self.active = False

    def draw(self, screen, no_mod):
        color = powder_blue
        if not no_mod:
            if self.active:
                color = self.active_color
            elif self.rect.collidepoint(pygame.mouse.get_pos()):
                color = self.hover_color
            else:
                color = self.base_color
        pygame.draw.rect(screen, color, self.rect)

        text_rect = self.button_text.get_rect(center = self.rect.center)
        screen.blit(self.button_text, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return True
        return False



