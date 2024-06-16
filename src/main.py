from gridmap import *
from trajectory import *
from configs import *
from eventhandler import *
from button import *

import pygame as pg

def AStar(map: GridMap, start_point: tuple[int]) -> Trajectory:
    # TODO: implement A* Algorithm
    pass


FPS = 60
clock = pg.time.Clock()

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("A* Algorithm Showcase")
    pg.display.set_icon(SCREEN_ICON)  

    map_surf = pg.surface.Surface((DEFAULT_MAP_WIDTH * TILESIZE, DEFAULT_MAP_HEIGHT * TILESIZE))
    map_rect = map_surf.get_rect(topleft = MAP_POS)
    map_surf.fill("white")

    map = GridMap()
    map.set_grid(DEFAULT_MAP)


    # TODO: Add buttons, make button sprites
    # TODO: Add options for brushes
    buttons: list[Button] = []
    handler = EventHandler(map, buttons)

    while True:
        handler.run()

        screen.fill(SCREEN_BG_COLOR)
        screen.blit(map_surf, map_rect)
        map.get_drawn(map_surf)
        
        for button in buttons:
            button.get_drawn(map_surf)

        pg.display.update()
        clock.tick(FPS)

        
