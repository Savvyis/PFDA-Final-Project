import pygame
from PIL import Image
import turtle



def main():
    pygame.init()

    display = pygame.display.set_mode((990, 660))

    background = pygame.image.load('eas.jpg')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display.blit(background, (0,0))
        pygame.display.update()

    pygame.quit()


#class sketch():
# draw using the arrow keys, including diagonally


#class shake():
# shake the canvas to erase the drawings



if __name__ == "__main__":
    main()
