import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps_timer = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        pygame.Surface.fill(screen, (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatable in updatables:
            updatable.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = fps_timer.tick(60) / 1000


if __name__ == "__main__":
    main()
