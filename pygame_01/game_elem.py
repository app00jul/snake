import random

class Snake:
    def __init__(self):
        Snake.snake_position = [540,350]
        Snake.snake_body = [[540,350],
                            [530,350],
                            [520,350],
                            [510,350]
                            ]

class Fruit:
    def __init__(self):
        Fruit.position = [random.randrange(1, 1080),
                          random.randrange(1,700)]
        Fruit_spawn = True

