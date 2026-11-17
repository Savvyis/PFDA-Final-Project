import pygame




class Sketch():

    def __init__(self, x, y, color=(50, 50, 50), size=5, speed=4):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed = speed
        

    def update(self, surf_width, surf_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < surf_width - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < surf_height - self.size:
            self.y += self.speed

        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))


#class Shake():
# shake the canvas to erase the drawings



def main():
    pygame.init()
    display = pygame.display.set_mode((990, 660))
    background = pygame.image.load('eas.jpg')
    x, y = (229.35, 97.35)
    width, height = (529.65, 332)
    surf = pygame.Surface((width, height))
    surf.fill((211, 211, 211))
    clock = pygame.time.Clock()
    pen = Sketch((width // 2), (height // 2), color=(50, 50, 50))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        background.blit(surf, (x, y))
        pen.update(width, height)
        pen.draw(surf)
        pygame.display.flip
        display.blit(background, (0,0))
        clock.tick(60)
        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()
