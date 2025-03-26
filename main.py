import pygame
from constants import *
from player import Player

def main():
    pygame.init() #initialize the game engine
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # display mode
    clock = pygame.time.Clock()
    running = True
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while running: # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X button on window
                running = False # exits infinite loop

        player.update(dt)

        screen.fill("black") # screen color and fill
        player.draw(screen)
        pygame.display.flip() # updates display]
        
        dt = clock.tick(60) / 1000 # sets/limits the framerate to 60      


if __name__ == "__main__":
    main()