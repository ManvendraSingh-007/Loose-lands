import sys
import pygame as pg

from config import (
    CAMERA_SPEED,
    FPS,
    HOVER_COLOR,
    MAP_HEIGHT,
    MAP_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TILE_SIZE,
)
from tile_map import TileMap


def handle_camera_movement(dt: float, camera_x: float, camera_y: float) -> tuple[float, float]:
    """Update camera position based on WASD or arrow key input, clamped to map bounds."""
    keys = pg.key.get_pressed()
    dx = 0.0
    dy = 0.0

    if keys[pg.K_a] or keys[pg.K_LEFT]:
        dx -= 1.0
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        dx += 1.0
    if keys[pg.K_w] or keys[pg.K_UP]:
        dy -= 1.0
    if keys[pg.K_s] or keys[pg.K_DOWN]:
        dy += 1.0

    max_x = max(0, MAP_WIDTH * TILE_SIZE - SCREEN_WIDTH)
    max_y = max(0, MAP_HEIGHT * TILE_SIZE - SCREEN_HEIGHT)

    new_x = max(0.0, min(float(max_x), camera_x + dx * CAMERA_SPEED * dt))
    new_y = max(0.0, min(float(max_y), camera_y + dy * CAMERA_SPEED * dt))
    return new_x, new_y


def draw_hover_highlight(
    surface: pg.Surface, tile_map: TileMap, camera_x: float, camera_y: float
) -> None:
    """Draw a highlight box around the tile currently under the mouse cursor."""
    mouse_x, mouse_y = pg.mouse.get_pos()
    grid_x, grid_y = tile_map.screen_to_grid(mouse_x, mouse_y, camera_x, camera_y)

    if not tile_map.in_bounds(grid_x, grid_y):
        return

    screen_x = int(grid_x * TILE_SIZE - camera_x)
    screen_y = int(grid_y * TILE_SIZE - camera_y)
    rect = pg.Rect(screen_x, screen_y, TILE_SIZE, TILE_SIZE)
    pg.draw.rect(surface, HOVER_COLOR, rect, 2)


def main() -> None:
    """Run the Loose Land game loop."""
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Loose Land")
    clock = pg.time.Clock()

    tile_map = TileMap()
    camera_x = 0.0
    camera_y = 0.0

    while True:
        dt = clock.tick(FPS) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        camera_x, camera_y = handle_camera_movement(dt, camera_x, camera_y)

        screen.fill((0, 0, 0))
        tile_map.draw(screen, camera_x, camera_y)
        draw_hover_highlight(screen, tile_map, camera_x, camera_y)
        pg.display.flip()


if __name__ == "__main__":
    main()
