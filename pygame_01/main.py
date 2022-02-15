import pygame

#Initialize the game
pygame.init()

#Start the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("YEEEEET!")
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)

#Close button
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    pygame.display.update()