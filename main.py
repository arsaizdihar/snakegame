import pygame

WIDTH, HEIGHT = 600, 600
SIZE = 20

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

running = True
x = 0
y = 0


def redraw_window():
    window.fill((0, 0, 0))
    # draw seluruh elemen game
    pygame.draw.rect(window, "white", (x*SIZE, y*SIZE, SIZE, SIZE))
    pygame.display.flip()


while running:
    redraw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 1
            elif event.key == pygame.K_DOWN:
                y += 1
            elif event.key == pygame.K_LEFT:
                x -= 1
            elif event.key == pygame.K_RIGHT:
                x += 1
