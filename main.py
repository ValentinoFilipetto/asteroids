import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    dt = 0

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        for item in asteroids:
            if item.isColliding(player):
                print("Game over!")
                return 
    
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        for item in asteroids:
            for bullet in shots:
                if item.isColliding(bullet):
                    item.split()
                    bullet.kill()

        pygame.display.flip()
        time_since_last_thick = clock.tick(60) # 60 is an upper bound
        dt = time_since_last_thick / 1000 # we divide by 1000 to convert to seconds
    

if __name__ == "__main__":
    main()