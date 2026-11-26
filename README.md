# Loose Land

A 2D factory/automation game built with Python and Pygame.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python install -e . # for maintainer and devs, do this for every updates ig
```

## Run

```bash
LooseLands
# or
python -m LooseLands
```

## Contributing

See [CODING_GUIDELINES.md](CODING_GUIDELINES.md).

## project structure

```txt
LooseLands                           -- project root
├── assets                           -- assets
│   └── grass.png                    -- 
├── CODING_GUIDELINES.md             -- guidelines
├── LICENSE                          -- GLPv3
├── pyproject.toml                   -- build stuff
├── pyrightconfig.json               -- for LS
├── README.md                        -- this file
├── src                              -- source directory
│   └── loose_lands                  -- project
│       ├── buildings.py             -- 
│       ├── config.py                -- 
│       ├── __init__.py              -- 
│       ├── __main__.py              -- 
│       ├── main.py                  -- main entry point
│       ├── texture.py               -- 
│       ├── tile_map.py              -- 
│       └── tools                    -- for some tools
├── tests                            -- test folder
└── _ToDo.txt                        -- 
```
