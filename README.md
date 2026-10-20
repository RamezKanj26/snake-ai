Author: Ramez Kanj

# snake-ai

A classic Snake game built from scratch in Python with pygame, with one big long-term goal: teach the snake to play the game by itself using reinforcement learning with PyTorch.

## The Challenge

The game code is written entirely by hand, without AI coding assistants. No copy-pasting generated code, no autocomplete doing the thinking. It's slower, but the point is to really understand every line, from drawing the grid to training the agent.

## Goals

1. **Build the game.** A fully playable Snake game with a grid, movement, food, growth, score and game over.
2. **Make it AI-ready.** Restructure the game so an agent can control it step by step, without a human at the keyboard.
3. **Train an agent.** Use reinforcement learning with PyTorch so the snake learns to play on its own.
4. **Win the game.** The ultimate goal: an agent that fills the entire board.

## Progress

- [x] Project setup with uv and pygame-ce
- [x] Draw the grid
- [x] Draw the snake and food
- [x] Snake movement with arrow keys
- [x] Eating food and growing
- [x] Random food placement
- [x] Collision detection and game over
- [ ] Score display
- [ ] Refactor the game into a reusable environment (in progress)
- [ ] Reinforcement learning agent with PyTorch
- [ ] Training and plotting results
- [ ] Beat the game

## Current Stage: Making the Game AI-Ready

The game is playable. Before an agent can play it thousands of times, the code needs a cleanup. `game.py` stays untouched as the original hand-built game, and the AI-ready version is built in a new file, `snake_env.py`:

- [ ] Move the game state into a `SnakeGame` class instead of global variables
- [ ] Add a `reset()` method so a new game starts without restarting the program
- [ ] Add a `step(action)` method that advances the game by one move and reports the reward, whether the game is over, and the score
- [ ] Split game logic from drawing, so training can run without a window
- [ ] Pull collision checking into its own `is_collision(point)` function, so the agent can use it to sense danger
- [ ] Add a quick way to test the environment by playing it or running random moves
- [ ] Track the score
- [ ] End games where the snake wanders too long without eating
- [ ] Speed up food spawning and collision lookups for long snakes

## Tech Stack

- **Python 3.12**
- **[pygame-ce](https://pyga.me/)** for the game window and rendering
- **[uv](https://docs.astral.sh/uv/)** for dependency and environment management
- **[PyTorch](https://pytorch.org/)** for the neural network (coming soon)

## Getting Started

Make sure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed, then:

```bash
git clone https://github.com/RamezKanj26/snake-ai.git
cd snake-ai
uv sync
uv run python src/snake_ai/game.py
```

## Controls

| Key | Action |
| --- | --- |
| ↑ | Move up |
| ↓ | Move down |
| ← | Move left |
| → | Move right |

The snake can't reverse directly into itself.

## Project Structure

```
snake-ai/
├── src/
│   └── snake_ai/
│       ├── __init__.py
│       ├── game.py      # the original hand-built Snake game
│       └── snake_env.py # AI-ready version of the game (in progress)
├── pyproject.toml
└── README.md
```

## Reinforcement Learning Plan

The rough plan for the AI side of the project:

- **State:** what the snake "sees", such as danger nearby, its current direction, and where the food is relative to its head.
- **Actions:** go straight, turn left or turn right.
- **Rewards:** positive for eating food, negative for dying, possibly small penalties for wandering around too long.
- **Model:** start with a Deep Q-Network (DQN) in PyTorch, then explore improvements once it learns the basics.

This will evolve as I learn more along the way.
