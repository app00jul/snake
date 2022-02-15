import pygame

#Initialize the game
pygame.init()

#Start the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("YEEEEET!")

#Close button
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

