import pygame
from constants import *
from player import Player

def main():
    pygame.init() #initialize the game engine
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # display mode
    clock = pygame.time.Clock()
    running = True
    updatable = pygame.sprite.Group() # group for objects that can be updated
    drawable = pygame.sprite.Group() # group for objects that can be drawn
    # add player containers to groups
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    # object groups 
    

    while running: # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X button on window
                running = False # exits infinite loop

        updatable.update(dt)

        screen.fill("black") # screen color and fill

        for obj in drawable: # iterate over and draw each object in group
            obj.draw(screen)

        pygame.display.flip() # updates display]

        dt = clock.tick(60) / 1000 # sets/limits the framerate to 60      


if __name__ == "__main__":
    main()