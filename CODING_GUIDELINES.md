# Coding Guidelines

the guidelines keep our codebase clean, readable, and easy for everyone innterested to work on it.

---

## 1. AI-Assisted Coding
AI tools are **allowed and encouraged**, with three rules:
1. **Understand what you commit:** If you can't explain what a function does, don't push it.
2. **Test before pushing:** Run and verify the feature (don't trust AI output blindly).
3. **Keep changes focused:** make small and atomic commits so that it's easy to undo changes.

---

## 2. Naming Conventions :|
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

## 3. Code Style & Structure
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

## 4. Git & Collaboration Workflow
- **Pull before you start:** Always `git pull` before writing new code.
- **One feature per branch/PR (or small commits):** Don't work for days without pushing. Small, frequent commits are easier to merge.
- **Clear commit messages:** Say *what* changed, e.g. `Add tile hover highlight` or `Fix camera offset math`.
- **Don't commit environment files:** Keep `.venv/`, `__pycache__/`, and `.pyc` files out of Git (use `.gitignore`).
- **Update `requirements.txt`:** If you install a new package, run `pip freeze > requirements.txt` (or add it to `requirements.txt`) so everyone stays in sync.
