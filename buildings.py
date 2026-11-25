from dataclasses import dataclass
import pygame as pg

from config import BUILDING_COLORS, SCREEN_HEIGHT, SCREEN_WIDTH, TILE_SIZE
from tile_map import TileMap


@dataclass
class Building:
    kind: str
    grid_x: int
    grid_y: int
    direction: str = "N"


class BuildingManager:
    def __init__(self) -> None:
        self.buildings: dict[tuple[int, int], Building] = {}
        self.selected_building_kind = None      # current selected building kind 
        self.selected_direction_index = 0       # current selected direction index 

    def can_place(self, kind: str, grid_x: int, grid_y: int, tile_map: TileMap) -> bool:
        # checks if building can be placed on the tile 

        tile = tile_map.get_tile(grid_x, grid_y)
        if tile is None or tile == "water": 
            return False

        # check if any other building occupy that tile
        if (grid_x, grid_y) in self.buildings:
            return False

        # check if the kind is "miner" (tool)
        # only allow them on ore tiles
        if kind == "miner" and tile not in ("iron_ore", "copper_ore"):
            return False

        return True
    
    def place(self, kind: str, grid_x: int, grid_y: int, direction: str, tile_map: TileMap) -> bool:
        # place the building if can_place is true

        if not self.can_place(kind, grid_x, grid_y, tile_map):
            return False

        self.buildings[(grid_x, grid_y)] = Building(kind, grid_x, grid_y, direction)
        return True

    def remove(self, grid_x: int, grid_y: int) -> bool:
        """Remove a building at (grid_x, grid_y) if present. Return True on success."""
        return self.buildings.pop((grid_x, grid_y), None) is not None


    def draw(self, surface: pg.Surface, camera_x: float, camera_y: float) -> None:
        # draws buildings on the screen

        for building in self.buildings.values():
            # get pixel cooordinate x and y of tile
            rect_x, rect_y = TileMap.grid_to_screen(building.grid_x, building.grid_y, camera_x, camera_y)
            rect = pg.Rect(rect_x, rect_y, TILE_SIZE, TILE_SIZE)
            pg.draw.rect(surface, BUILDING_COLORS[building.kind], rect)