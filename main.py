import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps_timer = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

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
        for asteroid in asteroids:
            if(player.check_collision(asteroid) == True):
                print("Game Over!")
                return
        for asteroid in asteroids:
            for shot in shots:
                if(shot.check_collision(asteroid) == True):
                    shot.kill()
                    asteroid.split()


if __name__ == "__main__":
    main()
