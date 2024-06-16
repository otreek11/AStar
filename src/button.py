import pygame as pg
from typing import Callable
from configs import FONT, BUTTON_BORDER_COLOR

class Button:
    def __init__(self, surf: pg.Surface, rect: pg.Rect, action: Callable = lambda : None, name: str = ""):
        self.bright_surf = surf.copy()
        fontrender = FONT.render(name, False, BUTTON_BORDER_COLOR)
        fontrender_rect = fontrender.get_rect(center = surf.get_rect(topleft = (0, 0)).center)
        self.bright_surf.blit(fontrender, fontrender_rect)

        self.darkened_surf = self.bright_surf.copy()
        overlay = pg.surface.Surface(surf.get_size(), pg.SRCALPHA)
        overlay.fill((0, 0, 0, 40))

        self.darkened_surf.blit(overlay, (0, 0))
        self.img = self.bright_surf
        self.rect = rect
        self.action = action

    def contains(self, p: tuple[int, int]) -> bool:
        return self.rect.collidepoint(p)

    def hold(self) -> None:
        self.img = self.darkened_surf
    
    def release(self) -> None:
        self.img = self.bright_surf
        self.action()

    def is_pressed(self) -> bool:
        return self.img == self.darkened_surf

    def get_drawn(self, surf: pg.Surface) -> None:
        surf.blit(self.img, self.rect)