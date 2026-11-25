"""Shared configuration constants for Loose Land."""

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

TILE_SIZE = 32
MAP_WIDTH = 60
MAP_HEIGHT = 60

CAMERA_SPEED = 320.0  # pixels per second

TILE_COLORS: dict[str, tuple[int, int, int]] = {
    "grass": (68, 120, 62),
    "iron_ore": (110, 125, 145),
    "copper_ore": (184, 115, 51),
    "water": (45, 95, 165),
}

GRID_LINE_COLOR = (55, 100, 50)
HOVER_COLOR = (255, 230, 90)
