import pygame
from constants import *

def main():
    pygame.init() #initialize the game engine
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # display mode
    while True: # game loop
        screen.fill("black")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X button on window
                return # exits infinite loop

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()