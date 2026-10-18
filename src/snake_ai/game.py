import pygame
import random

CELL_SIZE = 20
GRID_SIZE = 25
TOTAL_SIZE = CELL_SIZE * GRID_SIZE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((TOTAL_SIZE, TOTAL_SIZE))
clock = pygame.time.Clock()
running = True

snake = [(8, 12), (7, 12), (6, 12)]
food = (16, 12)
direction = (1, 0)
queue = []

directions = {
    pygame.K_RIGHT: (1, 0),
    pygame.K_LEFT: (-1, 0),
    pygame.K_DOWN: (0, 1),
    pygame.K_UP: (0, -1),
}


def draw_cell(col, row, colour):
    pygame.draw.rect(
        screen,
        colour,
        pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    )


def spawn_food(snake):
    free_cells = []

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) not in snake:
                free_cells.append((i, j))
    return random.choice(free_cells)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key in directions and len(queue) <= 2:
            queue.append(event.key)

    if queue:
        key = queue.pop(0)
        new_direction = directions[key]

        if new_direction[0] + direction[0] != 0 or new_direction[1] + direction[1] != 0:
            direction = new_direction

    snake.insert(0, (snake[0][0] + direction[0], snake[0][1] + direction[1]))

    if snake[0] != food:
        snake.pop()
    else:
        food = spawn_food(snake)

    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_SIZE
        or snake[0][1] < 0
        or snake[0][1] >= GRID_SIZE
    ):
        print("Game Over")
        running = False

    if snake[0] in snake[1:]:
        print("Game Over")
        running = False

    screen.fill("white")

    for i in range(0, TOTAL_SIZE + 1, CELL_SIZE):
        # draw grid
        pygame.draw.line(screen, "lightgray", (i, 0), (i, TOTAL_SIZE - 1), 1)
        pygame.draw.line(screen, "lightgray", (0, i), (TOTAL_SIZE - 1, i), 1)

    for col, row in snake:
        draw_cell(col, row, "green")

    draw_cell(snake[0][0], snake[0][1], "darkgreen")

    draw_cell(food[0], food[1], "red")

    pygame.display.flip()

    clock.tick(8)

pygame.quit()
