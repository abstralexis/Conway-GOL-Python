import sys

import numpy as np

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

WIDTH = 500
HEIGHT = 500
CLOCK = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
SYSFONT = pygame.font.SysFont(pygame.font.get_default_font(), 18)
mode = "draw"

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
    global mode
    for event in pygame.event.get():
        # Exit process on window close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Mouse button events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Right click changes mode
            if event.button == 3:
                mode = "erase" if mode == "draw" else "draw"
    
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
        
    # Click and drag
    mousebuttons = pygame.mouse.get_pressed()
    if mousebuttons[0]: # Left mouse button
        x, y = pygame.mouse.get_pos()
        i = y // 5
        j = x // 5
        matrix[i][j] = 1 if mode == "draw" else 0
            
def draw(matrix: np.ndarray) -> None:
    """
    Draws the matrix to the screen
    """
    global mode
    WIN.fill(WHITE)
    for i, row in enumerate(matrix):
        y = i * 5
        for j, col in enumerate(row):
            x = j * 5
            if col == 1:
                rect = pygame.rect.Rect(x, y, 5, 5)
                pygame.draw.rect(WIN, BLACK, rect)

    draw_mode_text(mode)
    pygame.display.flip()
    
def draw_mode_text(mode):
    text = "Draw" if mode == "draw" else "Erase"
    mode_text = SYSFONT.render(text, True, GREY)
    WIN.blit(mode_text, (5, 5))
    
def new_array() -> np.ndarray:
    """
    Gets new (100, 100) ndarray
    # TODO fix hard-coding
    """
    return np.zeros((100, 100))
        
if __name__ == "__main__":
    main()