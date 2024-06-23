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

run_button_rect = BUTTON_IMG.get_rect(midtop = (SCREEN_WIDTH//2 + 14 * TILESIZE, MAP_DEVIATION + TILESIZE * (1 + 4 * BUTTON_HEIGHT)))
run_button = Button(BUTTON_IMG, run_button_rect, lambda : map.AStarTrajectory(), "Run")

wk_rect = WALL_KEY_TEXT.get_rect(midtop = (SCREEN_WIDTH//2 + 14 * TILESIZE, MAP_DEVIATION + TILESIZE * (1 + 6 * BUTTON_HEIGHT)))
op_rect = OPEN_KEY_TEXT.get_rect(midtop = (SCREEN_WIDTH//2 + 14 * TILESIZE, MAP_DEVIATION + TILESIZE * (1 + 7 * BUTTON_HEIGHT)))
rob_rect = ROBOT_KEY_TEXT.get_rect(midtop = (SCREEN_WIDTH//2 + 14 * TILESIZE, MAP_DEVIATION + TILESIZE * (1 + 8 * BUTTON_HEIGHT)))
obj_rect = OBJECTIVE_KEY_TEXT.get_rect(midtop = (SCREEN_WIDTH//2 + 14 * TILESIZE, MAP_DEVIATION + TILESIZE * (1 + 9 * BUTTON_HEIGHT)))

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

        screen.blit(WALL_KEY_TEXT, wk_rect)
        screen.blit(OPEN_KEY_TEXT, op_rect)
        screen.blit(ROBOT_KEY_TEXT, rob_rect)
        screen.blit(OBJECTIVE_KEY_TEXT, obj_rect)

        handler.run()
        pg.display.update()
        clock.tick(FPS)

        
