import pygame as pg

class Button:
    def __init__(self, surf: pg.Surface, rect: pg.Rect, action = lambda : None):
        self.bright_surf = surf.copy()
        self.darkened_surf = surf.copy()
        overlay = pg.surface.Surface(surf.get_size(), pg.SRCALPHA)
        overlay.fill((0, 0, 0, 20))

        self.darkened_surf.blit(overlay, (0, 0))
        self.img = self.bright_surf
        self.rect = rect
        self.action = action

    def contains(self, p: tuple[int, int]) -> bool:
        return self.rect.collidepoint(p)
    
    def do_action(self) -> None:
        self.action()

    def hold(self) -> None:
        self.img = self.darkened_surf
    
    def release(self) -> None:
        self.img = self.bright_surf

    def is_pressed(self) -> bool:
        return self.img is self.darkened_surf

    def get_drawn(self, surf: pg.Surface) -> None:
        surf.blit(self.img, self.rect)