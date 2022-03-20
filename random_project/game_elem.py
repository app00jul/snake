import pygame
from pygame.locals import *

class App:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((1080,700),flags)
        App.running = True

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
            App.screen.fill(Color('gray'))
            pygame.display.update()
        pygame.quit()