import pygame
import time
import random
from pygame.locals import *

class Game:
    def __init__(self):
        self.snake_position = [540, 350]
        self.snake_body_position = [[540, 350],
                              [530, 350],
                              [520, 350],
                              [510, 350]
                              ]
        self.fruit_position = [random.randrange(1,1080),random.randrange(1,700)]
        self.fruit_spawn = True
        self.direction = "RIGHT"
        self.change_direction_to = self.direction
        self.score = 0

    def score_displace(self,choice,color,font,size):
        score_font = pygame.font.SysFont(font,size)
        score_surface = score_font.render(f"Score: {self.score}",True,color)
        score_board = score_surface.get_rect()

        #display the text
        App.screen.blit(score_surface,score_board)

    def game_over_screen(self):
        my_font = pygame.font.SysFont("times new roman", 50)

        game_over_surface = my_font.render(f"Your Score is: {self.score}", True,pygame.color(255,0,0))
        game_over_board = game_over_surface.get_rect()
        game_over_board.midtop = (520,175)

        App.screen.blit(game_over_surface,game_over_board)
        pygame.display.flip()

        time.sleep(3)
        pygame.quit()

        quit()


class App:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((1080, 700), flags)
        App.running = True
        self.window_x = 1080
        self.window_y = 700
        self.fps = pygame.time.Clock()

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        Game.change_direction_to = 'UP'
                    if event.key == pygame.K_s:
                        Game.change_direction_to = 'DOWN'
                    if event.key == pygame.K_a:
                        Game.change_direction_to = 'LEFT'
                    if event.key == pygame.K_d:
                        Game.change_direction_to = 'RIGHT'

            # If two keys pressed simultaneously
            # we don't want snake to move into two
            # directions simultaneously
            if Game.change_direction_to == 'UP' and Game.direction != 'DOWN':
                Game.direction = 'UP'
            if Game.change_direction_to == 'DOWN' and Game.direction != 'UP':
                Game.direction = 'DOWN'
            if Game.change_direction_to == 'LEFT' and Game.direction != 'RIGHT':
                Game.direction = 'LEFT'
            if Game.change_direction_to == 'RIGHT' and Game.direction != 'LEFT':
                Game.direction = 'RIGHT'

                # Moving the snake
            if Game.direction == 'UP':
                Game.snake_position[1] -= 10
            if Game.direction == 'DOWN':
                Game.snake_position[1] += 10
            if Game.direction == 'LEFT':
                Game.snake_position[0] -= 10
            if Game.direction == 'RIGHT':
                Game.snake_position[0] += 10

                # Snake body growing mechanism
                # if fruits and snakes collide then scores
                # will be incremented by 10
            Game.snake_body_position.insert(0, list(Game.snake_position))
            if Game.snake_position[0] == fruit_position[0] and Game.snake_position[1] == fruit_position[1]:
                Game.score += 10
                fruit_spawn = False
            else:
                Game.snake_body_position.pop()

            if not fruit_spawn:
                fruit_position = [random.randrange(1, (self.window_x // 10)) * 10,
                                  random.randrange(1, (self.window_y // 10)) * 10]

            fruit_spawn = True
            App.screen.fill(pygame.color(255,255,255))

            for pos in Game.snake_body_position:
                pygame.draw.rect(App.screen, pygame.color(0,255,0),
                                 pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(App.screen, pygame.color(0,0,0), pygame.Rect(
                fruit_position[0], fruit_position[1], 10, 10))

            # Game Over conditions
            if Game.snake_position[0] < 0 or Game.snake_position[0] > self.window_x - 10:
                Game.game_over()
            if Game.snake_position[1] < 0 or Game.snake_position[1] > self.window_y - 10:
                Game.game_over()

                # Touching the snake body
                for block in Game.snake_body_position[1:]:
                    if Game.snake_position[0] == block[0] and Game.snake_position[1] == block[1]:
                        Game.game_over()

                # displaying score countinuously
                Game.show_score(1, pygame.color(0,0,0), 'times new roman', 20)

                # Refresh game screen
                pygame.display.update()

                # Frame Per Second /Refresh Rate
                self.fps.tick(15)

        pygame.quit()