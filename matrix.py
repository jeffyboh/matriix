import os
import pygame
from random import choice, randrange


class Symbol:
    def __init__(self, x, y, speed):
        self.x, self.y = x, y
        self.speed = speed
        self.value = choice(green_font)
        self.interval = randrange(5, 30)

    def draw(self, color):
        frames = pygame.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_font if color ==
                                'green' else lightgreen_font)

        self.y = self.y + self.speed if self.y < HEIGHT else - FONT_SIZE
        surface.blit(self.value, (self.x, self.y))


class SymbolColumn:
    def __init__(self, x, y):
        self.column_height = randrange(8, 18)
        self.speed = randrange(2, 6)
        self.symbols = [Symbol(x, i, self.speed) for i in range(
            y, y - FONT_SIZE * self.column_height, - FONT_SIZE)]

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen')
         for i, symbol in enumerate(self.symbols)]


os.environ['SDL_VIDEO_CENTERED'] = '1'
WIDTH = 800
HEIGHT = 600
FONT_SIZE = 30
alpha = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT))
surface.set_alpha(alpha)

clock = pygame.time.Clock()

symbol_font = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pygame.font.SysFont('IPAMincho', FONT_SIZE, bold=True)

green_font = [font.render(char, True, (0, randrange(160, 256), 0))
              for char in symbol_font]

lightgreen_font = [font.render(char, True, pygame.Color('lightgreen'))
                   for char in symbol_font]

symbol_columns = [SymbolColumn(x, randrange(-HEIGHT, 0))
                  for x in range(0, WIDTH, FONT_SIZE)]

while True:
    screen.blit(surface, (0, 0))
    surface.fill(pygame.Color('black'))

    for symbol_column in symbol_columns:
        symbol_column.draw()

    if not pygame.time.get_ticks() % 20 and alpha < 170:
        alpha += 3
        surface.set_alpha(alpha)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(60)
