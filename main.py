import pygame
from constants import *

def main():
    pygame.init() #initialize the game engine
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # display mode

    while True: # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X button on window
                return # exits infinite loop

        screen.fill("black") # screen color and fill
        pygame.display.flip() # updates display      


if __name__ == "__main__":
    main()