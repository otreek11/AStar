from trajectory import *
import pygame as pg
from configs import *

class GridMap:
    def __init__(self, rows: int = DEFAULT_MAP_HEIGHT, cols: int = DEFAULT_MAP_WIDTH):
        self.rows: int = rows
        self.cols: int = cols
        self.grid: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        self.robotpos = None
        self.objecpos = None

    def set_grid(self, grid: list[list[int]]):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid.copy()

        self.robotpos = None
        self.objecpos = None

    def clear(self) -> None:
        self.grid: list[list[int]] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.robotpos = None
        self.objecpos = None

    def is_open(self, p: tuple[int, int]) -> bool:
        return (self.grid[p[0]][p[1]] == 0)
    
    def set_open(self, p: tuple[int, int]) -> None:
        self.grid[p[0]][p[1]] = 0

    def set_wall(self, p: tuple[int, int]) -> None:
        self.grid[p[0]][p[1]] = 1

    def get_drawn(self, surf: pg.Surface) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                auxsurf = pg.surface.Surface((TILESIZE, TILESIZE))
                auxrect = auxsurf.get_rect(topleft = (col * TILESIZE, row * TILESIZE))
                auxsurf.fill(COLORS[self.grid[row][col]])
                surf.blit(auxsurf, auxrect)
                pg.draw.rect(surf, pg.Color("black"), auxrect, BORDER_SIZE) # borders on each cell

        if self.robotpos != None:
            auxsurf = pg.surface.Surface((TILESIZE, TILESIZE))
            auxrect = auxsurf.get_rect(topleft = (self.robotpos[1] * TILESIZE, self.robotpos[0] * TILESIZE))
            auxsurf.fill(ROBOT_COLOR)
            pg.draw.rect(auxsurf, pg.Color("black"), pg.Rect((0, 0), (TILESIZE, TILESIZE)), BORDER_SIZE)
            surf.blit(auxsurf, auxrect)

        if self.objecpos != None:
            auxsurf = pg.surface.Surface((TILESIZE, TILESIZE))
            auxrect = auxsurf.get_rect(topleft = (self.objecpos[1] * TILESIZE, self.objecpos[0] * TILESIZE))
            auxsurf.fill(OBJECTIVE_COLOR)
            pg.draw.rect(auxsurf, pg.Color("black"), pg.Rect((0, 0), (TILESIZE, TILESIZE)), BORDER_SIZE)
            surf.blit(auxsurf, auxrect)

    def AStarTrajectory(self) -> Trajectory:
        if self.robotpos == None or self.objecpos == None: return None
        # TODO: implement A* Algorithm
        pass
