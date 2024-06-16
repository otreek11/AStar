from collections.abc import Sequence
import pygame as pg
from configs import *

class Trajectory(Sequence):
    def __init__(self):
        self.trajectory: list[tuple[int, int]] = []

    def add(self, p: tuple[int, int]):
        self.trajectory.append(p)

    def __getitem__(self, i: int) -> tuple[int, int]:
        return self.trajectory[i]
    
    def __len__(self):
        return len(self.trajectory)
    
    def get_drawn(self, surf: pg.Surface):
        drawn = pg.surface.Surface((TILESIZE, TILESIZE))
        drawn.fill(TRAJECTORY_COLOR)
        pg.draw.rect(drawn, pg.Color("black"), pg.rect.Rect((0, 0), (TILESIZE, TILESIZE)), BORDER_SIZE)
        for point in self.trajectory:
            surf.blit(drawn, (point[0] * TILESIZE, point[1] * TILESIZE))