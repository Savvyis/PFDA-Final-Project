import pygame
import sys



def main():
    pygame.init()
    display = pygame.display.set_mode((990, 660))
    background = pygame.image.load('eas.jpg')
    x, y = (229.35, 97.35)
    width, height = (529.65, 332)
    surf = pygame.Surface((width, height))
    surf.fill((211, 211, 211))
    background.blit(surf, (x, y))
    #drawing = Sketch()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display.blit(background, (0,0))
        pygame.display.update()

    pygame.quit()


#class Sketch():

    #def __init__(self):
        

# draw using the arrow keys, including diagonally


#class Shake():
# shake the canvas to erase the drawings



if __name__ == "__main__":
    main()
