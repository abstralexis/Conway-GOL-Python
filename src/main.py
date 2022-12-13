import sys

import numpy as np

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 500
HEIGHT = 500
CLOCK = pygame.time.Clock()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Conway's Game of Life") 
pygame.init

def main() -> None:   
    array: np.ndarray = new_array()
    running = True
    while running:
        handle_events()
        CLOCK.tick(60)
        
def handle_events() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
def draw() -> None:
    WIN.fill(WHITE)
    pygame.display.flip()

def new_array() -> np.ndarray:
    return np.zeros((100, 100))

def process_tile(matrix: np.ndarray, i: int, j: int) -> None:
    pass

def get_neighbours(array: np.ndarray, i: int, j :int) -> list:
    """
    Gets list of the 8 neighbouring values to array[i][j].
    Assumes C-Style (row-major) ndarray.
    
    Does not return any neigbours for edge tiles.
    """
    height_index = array.shape()[0] - 1
    width_index = array.shape()[1] - 1
    
    if (i == 0) or (j == 0):
        return []
    
    if (i == height_index) or (j == width_index):
        return []
    
    return [].append(
        array[i-1][j-1],
        array[i-1][j],
        array[i-1][j+1],
        array[i+1][j+1],
        array[i+1][j],
        array[i+1][j-1],
        array[i, j-1]
    )
    
def seed_matrix(matrix: np.ndarray):
    try:
        matrix[5][5] = 1
        matrix[5][6] = 1
        matrix[6][6] = 1
        matrix[6][5] = 1
        
        matrix[20][20] = 1
        matrix[21][20] = 1
        matrix[22][20] = 1
    finally:
        pass
        
if __name__ == "__main__":
    main()