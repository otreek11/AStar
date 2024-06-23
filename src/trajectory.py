import pygame as pg
from configs import *
from collections.abc import Sequence

class Trajectory(Sequence):
    def __init__(self, path:list[tuple[int, int]] = []):
        self.trajectory: list[tuple[int, int]] = path

    def add(self, p: tuple[int, int]):
        self.trajectory.append(p)

    def __getitem__(self, idx: int) -> tuple[int, int]:
        return self.trajectory[idx]
    
    def __len__(self) -> int:
        return len(self.trajectory)
    
    def __iter__(self) -> list[tuple[int, int]]:
        return self.trajectory
    
    def remove(self, p: tuple[int, int]) -> None:
        self.trajectory.remove(p)
    
    def is_empty(self) -> bool:
        for _ in self.trajectory:
            return True
        return False
    
    def get_drawn(self, surf: pg.Surface):
        drawn = pg.surface.Surface((TILESIZE, TILESIZE))
        drawn.fill(TRAJECTORY_COLOR)
        pg.draw.rect(drawn, pg.Color("black"), pg.rect.Rect((0, 0), (TILESIZE, TILESIZE)), BORDER_SIZE)
        for point in self.trajectory:
            surf.blit(drawn, (point[1] * TILESIZE, point[0] * TILESIZE))