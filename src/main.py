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
    seed_matrix(array)
    running = True
    while running:
        handle_events()
        array = process_matrix(array)
        draw(array)
        CLOCK.tick(1)
        
def handle_events() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
def draw(matrix: np.ndarray) -> None:
    WIN.fill(WHITE)
    i = 0
    j = 0
    for i, row in enumerate(matrix):
        y = i * 5
        for j, col in enumerate(row):
            x = j * 5
            if col == 1:
                rect = pygame.rect.Rect(x, y, 5, 5)
                pygame.draw.rect(WIN, BLACK, rect)

    pygame.display.flip()
    
def new_array() -> np.ndarray:
    return np.zeros((100, 100))

def process_tile(matrix: np.ndarray, i: int, j: int) -> None:
    """
    Modifies a tile in a matrix of of 0s and 1s with the rules:

    If alive,
        if number of neigbours == 2 or 3
            stay alive
        else
            die
    if dead:
        if num neigbours == 3
            live
    """
    neighbours = get_neighbours(matrix, i, j)
    neighbours = neighbours.count(1)
    if matrix[i][j] == 1:
        if neighbours == 2 or neighbours == 3:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0
    else:
        if neighbours == 3:
            matrix[i][j] = 1

def process_matrix(matrix: np.ndarray) -> np.ndarray:
    print(get_neighbours(matrix, 20, 20).count(1))
    print(get_neighbours(matrix, 21, 20).count(1))
    print(get_neighbours(matrix, 22, 20).count(1))
    print(get_neighbours(matrix, 20, 20))
    print(get_neighbours(matrix, 21, 20))
    print(get_neighbours(matrix, 22, 20))

    new = matrix.copy()

    for i, row in enumerate(new):
        for j, _ in enumerate(row):
            neighbours = get_neighbours(matrix, i, j)
            neighbours = neighbours.count(1)
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
    
    Does not return any neigbours for edge tiles.
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