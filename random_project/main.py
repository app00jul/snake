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
        pygame.quit()

if __name__ == "__main__":
    App().run()

class Text:
    def __init__(self,text,post):
        self.text = text
        self.post = post

        self.font_name = None
        self.font_size = 72
        self.font_color = Color("white")
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.font_name,self.font_size)

    def render(self):
        self.img = self.font.render(self.text,True,self.font_color)
        self.rect = self.img.get_rect()
        self.rect.midright = self.pos

    def draw(self):
        App.screen.blit(self.img,self.rect)