import pygame
import os
import sys

WIDTH = 800
HEIGHT = 650
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        def load_image(name, colorkey=None):
            if not os.path.isfile(name):
                print(f"Файл с изображением '{name}' не найден")
                sys.exit()
            image = pygame.image.load(name)
            if colorkey is not None:
                image = image.convert()
                if colorkey == -1:
                    colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey)
            else:
                image = image.convert_alpha()
            return image

        self.image = pygame.Surface((50, 50))
        img = load_image('кисточка.webp', -1)
        self.image = img
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self, x, y):
        self.rect.x = x
        self. rect.y = y



pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x = int(event.pos[0])
            y = int(event.pos[1])
            all_sprites.update(x, y)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()