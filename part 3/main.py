import pygame
import random

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
        self.alive = True
        self.score = 0

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
        if self.alive:
            for i in range(len(self.segments)-1, 0, -1):
                self.segments[i].x = self.segments[i-1].x
                self.segments[i].y = self.segments[i-1].y
            self.head.x += self.vel_x * SIZE
            self.head.y += self.vel_y * SIZE

    def check_collision(self):
        # cek apakah snake masih hidup/tidak
        if self.head.x < 0 or self.head.x > WIDTH-SIZE or self.head.y < 0 or self.head.y > HEIGHT-SIZE:
            self.alive = False
        for segment in self.segments:
            if not segment == self.head:
                if self.head.colliderect(segment):
                    self.alive = False
        # cek collision dengan food
        if self.head.colliderect(food.rect):
            self.add_segment(self.segments[-1].x, self.segments[-1].y)
            food.reset_pos()
            self.score += 1
            return True

    def up(self):
        if not self.head.y - self.segments[1].y == SIZE:
            self.vel_x = 0
            self.vel_y = -1

    def down(self):
        if not self.head.y - self.segments[1].y == -SIZE:
            self.vel_x = 0
            self.vel_y = 1

    def left(self):
        if not self.head.x - self.segments[1].x == SIZE:
            self.vel_x = -1
            self.vel_y = 0

    def right(self):
        if not self.head.x - self.segments[1].x == -SIZE:
            self.vel_x = 1
            self.vel_y = 0

    def restart(self):
        self.__init__()

# buat class food


class Food:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, SIZE, SIZE)
        self.reset_pos()

    def reset_pos(self):
        is_valid = False
        while not is_valid:
            self.rect.x = random.randint(0, WIDTH//SIZE-1) * SIZE
            self.rect.y = random.randint(0, HEIGHT//SIZE-1) * SIZE
            collide = False
            for segment in player.segments:
                if self.rect.colliderect(segment):
                    collide = True
            is_valid = not collide

    def draw(self):
        pygame.draw.circle(
            window, "red", (self.rect.centerx, self.rect.centery), SIZE//2)

    def restart(self):
        self.__init__()


pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
player = Snake()
food = Food()
clock = pygame.time.Clock()

# atur speed snake
speed = 0.25
running = True


def display_score():
    scoreboard = font.render(f"Score: {player.score}", False, "green")
    scoreboard.set_alpha(100)
    window.blit(scoreboard, (0, 0))


def redraw_window():
    window.fill((0, 0, 0))
    # draw seluruh elemen game
    food.draw()
    player.draw()
    display_score()
    pygame.display.flip()


while running:
    clock.tick(FPS*speed)
    redraw_window()
    player.update()
    if player.check_collision():
        speed += 0.01
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
            elif event.key == pygame.K_F2 and not player.alive:
                player.restart()
                food.restart()
