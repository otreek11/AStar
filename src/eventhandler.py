import pygame as pg
from button import *
from gridmap import *
import sys

class EventHandler:
    def __init__(self, grid: GridMap, buttons: list[Button] = []):
        self.buttons = buttons
        self.grid = grid

    def run(self) -> None:
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    pg.quit()
                    sys.exit()
                case pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    self.handle_pressing(mouse_pos)
                case pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    self.handle_release(mouse_pos)

    def handle_pressing(self, mouse_pos: tuple[int, int]) -> None:
        for button in self.buttons:
            if button.contains(mouse_pos):
                button.hold()

    def handle_release(self, mouse_pos: tuple[int, int]):
        for button in self.buttons:
            if button.is_pressed():
                button.release()
                button.do_action()