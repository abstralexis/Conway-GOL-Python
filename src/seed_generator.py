import sys

import numpy as np

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 500
HEIGHT = 500
CLOCK = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Life seed generator") 
pygame.init()

def main() -> None:
    """
    Main function for seed creation program
    """
    array: np.ndarray = new_array()         # Gets a new array
    # Main loop handles events and draws array at 60 fps
    running = True                          
    while running:
        handle_events(array)                
        draw(array) 
        CLOCK.tick(60)
        
def handle_events(matrix: np.ndarray) -> None:
    """
    Handles window events e.g inputs
    """
    for event in pygame.event.get():
        # Exit process on window close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Mouse button events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left click gets current tile and makes it live
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                i = y // 5
                j = x // 5
                matrix[i][j] = 1
            # Right click gets current tile and makes it dead
            elif event.button == 3:
                x, y = pygame.mouse.get_pos()
                i = y // 5
                j = x // 5
                matrix[i][j] = 0
    
    # If Return/Enter pressed, save array to seed.txt
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        with open("seed.txt", "w") as seedfile:
            seed = ""
            for i in matrix:
                for j in i:
                    seed += f"{j},"

            seedfile.write(seed)
        print("Write successful")
            
def draw(matrix: np.ndarray) -> None:
    """
    Draws the matrix to the screen
    """
    WIN.fill(WHITE)
    for i, row in enumerate(matrix):
        y = i * 5
        for j, col in enumerate(row):
            x = j * 5
            if col == 1:
                rect = pygame.rect.Rect(x, y, 5, 5)
                pygame.draw.rect(WIN, BLACK, rect)

    pygame.display.flip()
    
def new_array() -> np.ndarray:
    """
    Gets new (100, 100) ndarray
    # TODO fix hard-coding
    """
    return np.zeros((100, 100))
        
if __name__ == "__main__":
    main()