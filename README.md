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
- [ ] Eating food and growing
- [ ] Random food placement
- [ ] Collision detection and game over
- [ ] Score display
- [ ] Refactor the game into a reusable environment
- [ ] Reinforcement learning agent with PyTorch
- [ ] Training and plotting results
- [ ] Beat the game

## Tech Stack

- **Python 3.12**
- **[pygame-ce](https://pyga.me/)** for the game window and rendering
- **[uv](https://docs.astral.sh/uv/)** for dependency and environment management
- **[PyTorch](https://pytorch.org/)** for the neural network (coming soon)
