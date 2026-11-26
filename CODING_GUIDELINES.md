# Coding Guidelines

the guidelines keep our codebase clean, readable, and easy for everyone innterested to work on it.

---

## 1. Naming Conventions :|
Follow standard Python naming:

| Item | Style | Example |
| :--- | :--- | :--- |
| Files & Modules | `snake_case` | `tile_map.py`, `network_client.py` |
| Variables & Functions | `snake_case` | `grid_x`, `get_tile_at()` |
| Classes | `PascalCase` | `TileMap`, `ConveyorBelt`, `Player` |
| Constants | `UPPER_SNAKE_CASE` | `TILE_SIZE = 32`, `MAX_PLAYERS = 4` |
| Private / Internal | `_leading_underscore` | `_build_chunk()` |

- Use **descriptive names** (`iron_ore_count` instead of `cnt` or `x`).
- Boolean variables/functions should read like questions: `is_walkable`, `has_power`, `can_place()`.

---

## 2. Code Style & Structure
- **Type Hints:** Use type hints on function signatures so everyone knows what goes in and out:
  ```python
  def get_tile(grid_x: int, grid_y: int) -> str:
      ...
  ```
- **Docstrings:** Add a short one-line (or multi-line) docstring to every class and public function explaining *what* it does.
- **No Magic Numbers:** Put shared numbers (screen size, tile size, tick rate, colors) in a `constants.py` or `config.py` file.
- **Keep Functions Small:** If a function is getting long or deeply nested, split it into smaller helper functions and use early `return`s.
- **Separate Logic from Rendering:** Keep simulation/game state (grids, machines, items) separate from `pygame` drawing code. That makes multiplayer syncing much easier later.

---
