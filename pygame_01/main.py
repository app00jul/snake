import pygame
from pygame.locals import *
from game_elem import Snake
from game_elem import Fruit

class App:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((1080,700),flags)
        App.name = pygame.display.set_caption("Snake")
        App.fps = pygame.time.Clock()
        App.running = True

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
        pygame.quit()

if __name__ == "__main__":
    App().run()

