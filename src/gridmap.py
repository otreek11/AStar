from heapq import heappop, heappush
from trajectory import *
import pygame as pg
from configs import *

class GridMap:
    def __init__(self, rows: int = DEFAULT_MAP_HEIGHT, cols: int = DEFAULT_MAP_WIDTH):
        self.rows: int = rows
        self.cols: int = cols
        self.grid: list[list[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        self.robotpos: tuple[int, int] = None
        self.objecpos: tuple[int, int] = None
        self.trajectory: Trajectory = None

    def set_grid(self, grid: list[list[int]]):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = [row[:] for row in grid]

        self.robotpos: tuple[int, int] = None
        self.objecpos: tuple[int, int] = None
        self.trajectory: Trajectory = None

    def clear(self) -> None:
        self.grid: list[list[int]] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.robotpos: tuple[int, int] = None
        self.objecpos: tuple[int, int] = None
        self.trajectory: Trajectory = None

    def contains_cell(self, cell: tuple[int, int]) -> bool:
        return (0 <= cell[0] < self.rows) and (0 <= cell[1] < self.cols)

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

        if self.trajectory != None:
            self.trajectory.get_drawn(surf)


    def AStarTrajectory(self) -> None:
        self.trajectory = None
        if self.robotpos is None or self.objecpos is None or self.robotpos == self.objecpos: return
        
        opens = [(0, self.robotpos)]
        closeds: set[tuple[int, int]] = set()
        came_from: dict[tuple[int, int], tuple[int, int]] = {}
        g_score: dict[tuple[int, int], float] = {self.robotpos: 0}
        f_score: dict[tuple[int, int], float] = {self.robotpos: GridMap.manhattan(self.robotpos, self.objecpos)}

        while opens:
            _, current = heappop(opens)
            
            if current in closeds:
                continue
            
            if current == self.objecpos:
                self.reconstruct_path(came_from, current)
                return
            
            closeds.add(current)
            
            for neighbor in self.get_neighbors(current):
                if neighbor in closeds:
                    continue
                
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in [n[1] for n in opens] or tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + GridMap.manhattan(neighbor, self.objecpos)
                    heappush(opens, (f_score[neighbor], neighbor))
    
    def get_neighbors(self, k: tuple[int, int]) -> list[tuple[int, int]]:
        neighbors = []
        directions: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for direction in directions:
            neighbor = (k[0] + direction[0], k[1] + direction[1])
            if self.contains_cell(neighbor) and self.is_open(neighbor):
                neighbors.append(neighbor)
        
        return neighbors

    def reconstruct_path(self, came_from: dict, current: tuple[int, int]) -> Trajectory:
        self.trajectory = Trajectory([])
        current = came_from[current]
        while current in came_from:
            self.trajectory.add(current)
            current = came_from[current]

    @staticmethod
    def manhattan(p1: tuple[int, int], p2: tuple[int, int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    @staticmethod
    def contains(p: tuple[int, int]) -> bool:
        return (MAP_POS[0] <= p[0] <= MAP_ENDPOS[0] and MAP_POS[1] <= p[1] <= MAP_ENDPOS[1])
    
    @staticmethod
    def get_cell(p: tuple[int, int]) -> tuple[int, int]:
        return ((p[1] - MAP_DEVIATION) // TILESIZE, (p[0] - MAP_DEVIATION) // TILESIZE)