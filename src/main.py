import sys

import numpy as np

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 500
HEIGHT = 500
CLOCK = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Life") 
pygame.init()

def main() -> None:
    """
    Main function for the Game of Life
    """
    # Read the seed file to a new array   
    array: np.ndarray = read_seed()

    # Main loop
    running = True
    generations = 0
    while running:
        handle_events()                 # Handle inputs
        array = process_matrix(array)   # Process array to new array
        draw(array)                     # Draw array

        # Increase generations count once per frame and set title
        generations += 1
        pygame.display.set_caption(f"Life | Generations: {generations}") 

        CLOCK.tick(12)  # 12 fps
        
def handle_events() -> None:
    """
    Handles the input events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close process on window close
            pygame.quit()
            sys.exit()
            
def draw(matrix: np.ndarray) -> None:
    """
    Takes in the board matrix and draws it to the screen

    #TODO change hard coded values
    """
    WIN.fill(WHITE)
    # Iterate through matrix and row to draw live cells to grid
    for i, row in enumerate(matrix):                
        y = i * 5
        for j, col in enumerate(row):
            x = j * 5
            if col == 1:
                rect = pygame.rect.Rect(x, y, 5, 5)
                pygame.draw.rect(WIN, BLACK, rect)

    pygame.display.flip()

def process_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    Returns a new matrix of of 0s and 1s based 
    off of argument matrix with the rules:

    If alive,
        if number of neighbours == 2 or 3
            stay alive
        else
            die
    if dead:
        if num neighbours == 3
            live
    """
    # Get new matrix to return as copy
    new = matrix.copy()

    # Iterate through new matrix then rows and update new
    # matrix based off of argument matrix
    for i, row in enumerate(new):
        for j, _ in enumerate(row):
            # Get neighbours and count number of live
            neighbours = get_neighbours(matrix, i, j)
            neighbours = neighbours.count(1)

            # Process the current tile with the rules
            if matrix[i][j] == 1:
                if neighbours == 2 or neighbours == 3:
                    new[i][j] = 1
                else:
                    new[i][j] = 0
            else:
                if neighbours == 3:
                    new[i][j] = 1

    return new

def get_neighbours(array: np.ndarray, i: int, j :int) -> list:
    """
    Gets list of the 8 neighbouring values to array[i][j].
    Assumes C-Style (row-major) ndarray.
    
    Does not return any neigbours for edge tiles. #TODO Fix
    """
    height_index = array.shape[0] - 1
    width_index = array.shape[1] - 1
    
    if (i == 0) or (j == 0):
        return []
    
    if (i == height_index) or (j == width_index):
        return []
    
    return [
        array[i-1][j-1],
        array[i-1][j],
        array[i-1][j+1],
        array[i][j+1],
        array[i+1][j+1],
        array[i+1][j],
        array[i+1][j-1],
        array[i][j-1]
    ]

def read_seed() -> np.ndarray:
    """
    Reads seed from seed.txt and returns ndarray

    Opens file and parses for a (100, 100 ndarray)
    TODO fix hard-coding
    """
    seed_matrix: list = []
    with open("seed.txt", "r") as seedfile:
        seed = seedfile.read().split(",")
        for i in range(100):
            row = []
            for j in range(100):
                index = (i*100) + j
                row.append(float(seed[index]))
            seed_matrix.append(row)
    return np.asarray(seed_matrix)
        
if __name__ == "__main__":
    main()