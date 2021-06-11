import pygame

WIDTH, HEIGHT = 600, 600
SIZE = 20
FPS = 30


class Snake:
    def __init__(self):
        self.segments = []
        self.vel_x = 1
        self.vel_y = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 300
        for _ in range(3):
            self.add_segment(x, 300)
            x -= SIZE

    def add_segment(self, posx, posy):
        new_segment = pygame.Rect(posx, posy, SIZE, SIZE)
        self.segments.append(new_segment)

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(window, (255, 255, 255), segment)

    def update(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].x = self.segments[i-1].x
            self.segments[i].y = self.segments[i-1].y
        self.head.x += self.vel_x * SIZE
        self.head.y += self.vel_y * SIZE

    def up(self):
        self.vel_x = 0
        self.vel_y = -1

    def down(self):
        self.vel_x = 0
        self.vel_y = 1

    def left(self):
        self.vel_x = -1
        self.vel_y = 0

    def right(self):
        self.vel_x = 1
        self.vel_y = 0


pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
player = Snake()
clock = pygame.time.Clock()
running = True


def redraw_window():
    window.fill((0, 0, 0))
    # draw seluruh elemen game
    player.draw()
    pygame.display.flip()


while running:
    clock.tick(FPS)
    redraw_window()
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
