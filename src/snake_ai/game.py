import pygame

CELL_SIZE = 20
GRID_SIZE = 25
TOTAL_SIZE = CELL_SIZE * GRID_SIZE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((TOTAL_SIZE, TOTAL_SIZE))
clock = pygame.time.Clock()
running = True

snake = [(12, 13), (12, 12), (12, 11)]
food = (12, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # RENDER GAME HERE
    for i in range(0, TOTAL_SIZE + 1, CELL_SIZE):
        # draw grid
        pygame.draw.line(screen, "lightgray", (i, 0), (i, TOTAL_SIZE - 1), 1)
        pygame.draw.line(screen, "lightgray", (0, i), (TOTAL_SIZE - 1, i), 1)

    for col, row in snake:
        pygame.draw.rect(
            screen,
            "green",
            pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )

    pygame.draw.rect(
        screen,
        "darkgreen",
        pygame.Rect(
            snake[0][0] * CELL_SIZE, snake[0][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE
        ),
    )
    pygame.draw.rect(
        screen,
        "red",
        pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
