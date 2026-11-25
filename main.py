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
    BUILDING_TYPES,
    DIRECTIONS,
)
from tile_map import TileMap
from buildings import BuildingManager
from texture import load_textures


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


    # set max x and max y for the camera to stop the camera from going out of bounds
    # map_width(60) * tile_size(32) = 1920 (total map width in pixels)
    # 1920 - screen_width(800) = 1120 (maximum camera x position) 
    max_x = max(0, MAP_WIDTH * TILE_SIZE - SCREEN_WIDTH)
    max_y = max(0, MAP_HEIGHT * TILE_SIZE - SCREEN_HEIGHT)


    # new_x and new_y calculate where the camera wants to move next
    # add tiny dx and dy to the camera position to make it move smoothly
    # clamp it min(max_y (1120), change)
    target_x = min(float(max_x), camera_x + dx * CAMERA_SPEED * dt)
    target_y = min(float(max_y), camera_y + dy * CAMERA_SPEED * dt)
    new_x = max(0.0, target_x)
    new_y = max(0.0, target_y)
    return new_x, new_y


def draw_hover_highlight(
    surface: pg.Surface, tile_map: TileMap, camera_x: float, camera_y: float
) -> None:
    """Draw a highlight box around the tile currently under the mouse cursor."""
    mouse_x, mouse_y = pg.mouse.get_pos()
    grid_x, grid_y = tile_map.screen_to_grid(mouse_x, mouse_y, camera_x, camera_y)

    # stop the highlight from going out of bounds
    if not tile_map.in_bounds(grid_x, grid_y):
        return

    screen_x, screen_y = tile_map.grid_to_screen(grid_x, grid_y, camera_x, camera_y)
    rect = pg.Rect(screen_x, screen_y, TILE_SIZE, TILE_SIZE)
    pg.draw.rect(surface, HOVER_COLOR, rect, 2)


def select_building_kind(event: pg.event.Event, current_kind: str) -> str:
    if event.key == pg.K_1:
        return BUILDING_TYPES[0]
    elif event.key == pg.K_2:
        return BUILDING_TYPES[1]
    elif event.key == pg.K_3:
        return BUILDING_TYPES[2]
    return current_kind



def handle_building_placement(
    event: pg.event.Event,
    screen_x: int,
    screen_y: int,
    camera_x: float,
    camera_y: float,
    building_manager: BuildingManager,
    tile_map: TileMap,
) -> None:
    """Handle building placement"""

    # convert screen position to grid position
    grid_x, grid_y = tile_map.screen_to_grid(screen_x, screen_y, camera_x, camera_y)
    
    if event.button == 1:
        building_manager.place(
            building_manager.selected_building_kind, 
            grid_x, 
            grid_y, 
            DIRECTIONS[building_manager.selected_direction_index], 
            tile_map)

    elif event.button == 3:
        building_manager.remove(grid_x, grid_y)


def main() -> None:
    """Run the Loose Land game loop."""
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Loose Land")
    textures = load_textures()
    clock = pg.time.Clock()

    tile_map = TileMap()
    building_manager = BuildingManager()

    building_manager.selected_building_kind = BUILDING_TYPES[0]
    camera_x = 0.0
    camera_y = 0.0

    while True:
        dt = clock.tick(FPS) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                handle_building_placement(event, mouse_x, mouse_y, camera_x, camera_y, building_manager, tile_map)

            elif event.type == pg.KEYDOWN:
                building_manager.selected_building_kind = select_building_kind(event, building_manager.selected_building_kind)

        camera_x, camera_y = handle_camera_movement(dt, camera_x, camera_y)

        screen.fill((0, 0, 0))
        tile_map.draw(screen, camera_x, camera_y, textures)
        building_manager.draw(screen, camera_x, camera_y)
        draw_hover_highlight(screen, tile_map, camera_x, camera_y)
        pg.display.flip()


if __name__ == "__main__":
    main()
