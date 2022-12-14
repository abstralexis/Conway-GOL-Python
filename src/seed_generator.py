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
    array: np.ndarray = new_array()
    running = True
    while running:
        handle_events(array)
        draw(array) 
        CLOCK.tick(60)
        
def handle_events(matrix: np.ndarray) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                i = y // 5
                j = x // 5
                matrix[i][j] = 1
            elif event.button == 3:
                x, y = pygame.mouse.get_pos()
                i = y // 5
                j = x // 5
                matrix[i][j] = 0
    
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
        
if __name__ == "__main__":
    main()