import sys
import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init() #initialize the game engine
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # display mode
    clock = pygame.time.Clock()
    running = True
    updatable = pygame.sprite.Group() # group for objects that can be updated
    drawable = pygame.sprite.Group() # group for objects that can be drawn
    asteroids = pygame.sprite.Group()
    # add player containers to groups
    Player.containers = (updatable, drawable)
    # add asteroid containers to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    # static containers field for asteroid field
    AsteroidField.containers = (updatable,)
    # create asteroid field object
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    # object groups 
    

    while running: # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X button on window
                running = False # exits infinite loop

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print("Game over!")
                sys.exit()
        

        screen.fill("black") # screen color and fill

        for obj in drawable: # iterate over and draw each object in group
            obj.draw(screen)

        pygame.display.flip() # updates display]

        dt = clock.tick(60) / 1000 # sets/limits the framerate to 60      


if __name__ == "__main__":
    main()