import pygame

CELL_SIZE = 20
GRID_SIZE = 25
TOTAL_SIZE = CELL_SIZE * GRID_SIZE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((TOTAL_SIZE, TOTAL_SIZE))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # RENDER GAME HERE
    for i in range(0, TOTAL_SIZE + 1, CELL_SIZE):
        pygame.draw.line(screen, "lightgray", (i, 0), (i, TOTAL_SIZE - 1), 1)
        pygame.draw.line(screen, "lightgray", (0, i), (TOTAL_SIZE - 1, i), 1)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
