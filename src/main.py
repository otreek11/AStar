from gridmap import *
from trajectory import *
from configs import *
from eventhandler import *
from button import *

import pygame as pg

if not pg.get_init(): pg.init()

FPS = 60
clock = pg.time.Clock()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("A* Algorithm Showcase")
pg.display.set_icon(SCREEN_ICON)

map_surf = pg.surface.Surface((DEFAULT_MAP_WIDTH * TILESIZE, DEFAULT_MAP_HEIGHT * TILESIZE))
map_rect = map_surf.get_rect(topleft = MAP_POS)
map = GridMap()

default_button_rect = BUTTON_IMG.get_rect(midtop = (SCREEN_WIDTH//2 + 14 * TILESIZE, MAP_DEVIATION + TILESIZE))
default_button = Button(BUTTON_IMG, default_button_rect, lambda : map.set_grid(DEFAULT_MAP), "Default")

clear_button_rect = BUTTON_IMG.get_rect(midtop = (SCREEN_WIDTH//2 + 14 * TILESIZE, MAP_DEVIATION + TILESIZE * (1 + 2 * BUTTON_HEIGHT)))
clear_button = Button(BUTTON_IMG, clear_button_rect, lambda : map.clear(), "Clear")

def Run(map: GridMap, surf: pg.Surface) -> None:
    trajectory = map.AStarTrajectory()
    if trajectory != None:
        trajectory.get_drawn(surf)

run_button_rect = BUTTON_IMG.get_rect(midtop = (SCREEN_WIDTH//2 + 14 * TILESIZE, MAP_DEVIATION + TILESIZE * (1 + 4 * BUTTON_HEIGHT)))
run_button = Button(BUTTON_IMG, run_button_rect, lambda : Run(map, map_surf), "Run")

if __name__ == "__main__":
    map.set_grid(DEFAULT_MAP)

    # TODO: Add buttons, make button sprites
    # TODO: Add options for brushes
    buttons: list[Button] = [default_button, clear_button, run_button]
    handler = EventHandler(map, buttons)

    while True:
        screen.fill(SCREEN_BG_COLOR)
        screen.blit(map_surf, map_rect)
        map.get_drawn(map_surf)
        
        for button in buttons:
            button.get_drawn(screen)

        handler.run()
        pg.display.update()
        clock.tick(FPS)

        
