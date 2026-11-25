import pygame as pg
from config import TILE_SIZE

def load_textures() -> dict[str, pg.Surface]:
    names = ["grass"]
    textures = {}
    for name in names:
        img = pg.image.load(f"assets/{name}.png").convert_alpha()
        textures[name] = pg.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    return textures