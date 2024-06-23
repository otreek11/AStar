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
                    self.handle_press(mouse_pos)
                case pg.MOUSEBUTTONUP:
                    self.handle_release()
                case pg.KEYDOWN:
                    self.grid.trajectory = None
                    mouse_pos = pg.mouse.get_pos()
                    self.handle_keyboard(mouse_pos)

    def handle_press(self, mouse_pos: tuple[int, int]) -> None:
        for button in self.buttons:
            if button.contains(mouse_pos):
                button.hold()
                return
        

    def handle_release(self):
        for button in self.buttons:
            if button.is_pressed():
                button.release()

    def handle_keyboard(self, mouse_pos: tuple[int, int]) -> None:
        if GridMap.contains(mouse_pos):
            cell = GridMap.get_cell(mouse_pos)
            keys = pg.key.get_pressed()
            if keys[WALL_KEY]:
                self.grid.set_wall(cell)
            elif keys[OPEN_KEY]:
                self.grid.set_open(cell)
            elif keys[ROBOT_KEY]:
                if self.grid.is_open(cell):
                    self.grid.robotpos = cell
            elif keys[OBJECTIVE_KEY]:
                if self.grid.is_open(cell):
                    self.grid.objecpos = cell
