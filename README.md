# asteroids

A small Asteroids-style arcade game built with **Pygame** as a learning project.

- You control a ship in the center of the screen.
- Asteroids spawn and drift across the playfield.
- Shots can destroy/split asteroids.
- Colliding with an asteroid ends the game.

## Requirements

- Python 3.x
- Pygame (pinned in `requirements.txt`)

## Setup

(Optional) create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: source venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 main.py
```

## Controls

- `W` / `S` — move forward / backward
- `A` / `D` — rotate left / right
- `SPACE` — shoot
- Close the window to quit
