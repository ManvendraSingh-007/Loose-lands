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

        self.building[(grid_x, grid_y)] = Building(kind, grid_x, grid_y, direction)
        return True