import pygame as pg
from configs import *

class GridMap:
    def __init__(self, rows: int = 0, cols: int = 0):
        self.rows: int = rows
        self.cols: int = cols
        self.grid: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_grid(self, grid: list[list[int]]):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid

    def is_open(self, p: tuple[int]) -> bool:
        return (self.grid[p[0]][p[1]] == 0)
    
    def set_open(self, p: tuple[int]) -> None:
        self.grid[p[0]][p[1]] = 0

    def set_wall(self, p: tuple[int]) -> None:
        self.grid[p[0]][p[1]] = 1

    def set_robot(self, p: tuple[int]) -> None:
        self.grid[p[0]][p[1]] = 2

    def set_objective(self, p: tuple[int]) -> None:
        self.grid[p[0]][p[1]] = 3

    def get_drawn(self, surf: pg.Surface) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                auxsurf = pg.surface.Surface((TILESIZE, TILESIZE))
                auxrect = auxsurf.get_rect(topleft = (col * TILESIZE, row * TILESIZE))
                auxsurf.fill(COLORS[self.grid[row][col]])
                surf.blit(auxsurf, auxrect)
                pg.draw.rect(surf, pg.Color("black"), auxrect, BORDER_SIZE) # borders on each cell


