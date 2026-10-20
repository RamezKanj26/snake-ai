import random

import pygame

CELL_SIZE = 20
GRID_SIZE = 20
TOTAL_SIZE = CELL_SIZE * GRID_SIZE


class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [((GRID_SIZE - 1) // 2, (GRID_SIZE - 1) // 2)]
        self.food = self.spawn_food()
        self.direction = (1, 0)
        self.score = 0
        self.steps_since_food = 0

    def spawn_food(self):
        free_cells = []

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if (i, j) not in self.snake:
                    free_cells.append((i, j))
        return random.choice(free_cells)

    def is_collision(self, point):
        point = tuple(point)
        return (
            point[0] < 0
            or point[0] >= GRID_SIZE
            or point[1] < 0
            or point[1] >= GRID_SIZE
            or point in self.snake[1:]
        )


if __name__ == "__main__":
    game = SnakeGame()
    print(game.is_collision((-1, 0)))
    print(game.is_collision((GRID_SIZE, 5)))
    print(game.is_collision((5, 5)))
    print(game.is_collision(game.snake[0]))
