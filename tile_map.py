"""Tile map generation, coordinate conversion, and rendering."""

import random
import pygame as pg

from config import (
    GRID_LINE_COLOR,
    MAP_HEIGHT,
    MAP_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TILE_COLORS,
    TILE_SIZE,
)


class TileMap:
    """Represents the 2D world grid of terrain and resource tiles."""

    def __init__(self, width: int = MAP_WIDTH, height: int = MAP_HEIGHT, seed: int = 42) -> None:
        """Initialize the tile map with terrain and ore patches."""

        # set width, height
        self.width = width
        self.height = height

        # set tiles with grass and generate world
        self.tiles: list[list[str]] = [["grass" for _ in range(width)] for _ in range(height)]
        self._generate_world(seed)

    def _generate_world(self, seed: int) -> None:
        """Populate the map with simple ore and water patches."""

        rng = random.Random(seed)
        self._place_patches(rng, "iron_ore", count=8, radius=2)
        self._place_patches(rng, "copper_ore", count=8, radius=2)
        self._place_patches(rng, "water", count=5, radius=3)

    def _place_patches(self, rng: random.Random, tile_type: str, count: int, radius: int) -> None:
        """Scatter circular patches of a given tile type across the map."""
        for _ in range(count):
            
            # select a random center for x axis and y axis in the range [radius, width-radius-1, height-radius-1]
            center_x = rng.randint(radius, self.width - radius - 1)
            center_y = rng.randint(radius, self.height - radius - 1)

            # iterate over a square area around the center
            # the side of square is from -radius to radius + 1
            #                            = 2*radius + 1 
            for dy in range(-radius, radius + 1):
                for dx in range(-radius, radius + 1):

                    # checks if the point lies inside the circle using pythagoras theorem
                    if dx * dx + dy * dy <= radius * radius:
                        self.tiles[center_y + dy][center_x + dx] = tile_type

    def in_bounds(self, grid_x: int, grid_y: int) -> bool:
        """Return True if the grid coordinates are inside the map."""
        return 0 <= grid_x < self.width and 0 <= grid_y < self.height

    def get_tile(self, grid_x: int, grid_y: int) -> str | None:
        """Return the tile type at (grid_x, grid_y), or None if out of bounds."""
        if not self.in_bounds(grid_x, grid_y):
            return None
        return self.tiles[grid_y][grid_x]

    @staticmethod
    def screen_to_grid(screen_x: int, screen_y: int, camera_x: float, camera_y: float) -> tuple[int, int]:
        """Convert screen pixel coordinates to grid tile coordinates."""

        # camera_x and camera_y = represent how far the camera has scrolled across the full game map
        # screen_x and screen_y = relative position to the top-left corner of the game window (0, 0).

        # [0,0] Absolute Top Left of The Game (Full game Map)
        #   +---------------------------------------------------+
        #   |                                                   |
        #   |                                                   |
        #   |                     [0,0]                         |
        #   |   <-- camera_x -->  +---[ pygame   Window ]---+   | 
        #   |                     |                         |   |
        #   |                     |  <- screen_x -> (X)     |   |
        #   |                     |                Click!   |   |
        #   |                     +-------------------------+   |
        #   +---------------------------------------------------+


        world_x = screen_x + camera_x
        world_y = screen_y + camera_y
        # Convert world pixels to tile index (e.g., world_x = 500, TILE_SIZE = 50 -> tile index 10)
        return int(world_x // TILE_SIZE), int(world_y // TILE_SIZE)

    @staticmethod
    def grid_to_screen(grid_x: int, grid_y: int, camera_x: float, camera_y: float) -> tuple[int, int]:
        """Convert grid tile coordinates to screen pixel coordinates."""
        return int(grid_x * TILE_SIZE - camera_x), int(grid_y * TILE_SIZE - camera_y)

    def draw(self, surface: pg.Surface, camera_x: float, camera_y: float, textures: dict[str, pg.Surface]) -> None:
        """Draw only the tiles currently visible on screen."""
        start_x = max(0, int(camera_x // TILE_SIZE))
        end_x = min(self.width, int((camera_x + SCREEN_WIDTH) // TILE_SIZE) + 1)
        start_y = max(0, int(camera_y // TILE_SIZE))
        end_y = min(self.height, int((camera_y + SCREEN_HEIGHT) // TILE_SIZE) + 1)

        for grid_y in range(start_y, end_y):
            screen_y = int(grid_y * TILE_SIZE - camera_y)
            for grid_x in range(start_x, end_x):
                screen_x = int(grid_x * TILE_SIZE - camera_x)
                tile_type = self.tiles[grid_y][grid_x]
                rect = pg.Rect(screen_x, screen_y, TILE_SIZE, TILE_SIZE)
                if tile_type in textures:
                    surface.blit(textures[tile_type], (screen_x, screen_y))
                else:
                    pg.draw.rect(surface, TILE_COLORS[tile_type], rect)
