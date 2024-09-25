import pygame
from pygame.locals import *
import time
import random

pygame.init()

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)
yellow = (255, 255, 0)
black = (0, 0, 0)

# Screen dimensions
win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Snake Game')
time.sleep(2)

snake = 10
snake_speed = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 40)
score_font = pygame.font.SysFont('Arial', 40)

def user_score(score):
    number = score_font.render(f"Score: {score}", True, red)
    window.blit(number, [0, 0])

def game_snake(snake, snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window, green, (x[0], x[1], snake, snake))

def message(msg):
    msg = font.render(msg, True, red)
    window.blit(msg, [win_width / 6, win_height / 3])

def game_loop():
    gameover = False
    gameclose = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    while not gameover:

        while gameclose:
            window.fill(black)
            message("You Lost! Press Q-Quit or P-Play Again")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    gameover = True
                    gameclose = True
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        gameover = True
                        gameclose = True
                    if event.key == K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = True
                break
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == K_UP:
                    y1_change = -snake
                    x1_change = 0
                elif event.key == K_DOWN:
                    y1_change = snake
                    x1_change = 0

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            gameclose = True

        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, yellow, [foodx, foody, snake, snake])

        snake_head = [x1, y1]
        snake_length_list.append(snake_head)
        if len(snake_length_list) > snake_length:
            del snake_length_list[0]

        game_snake(snake, snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()

game_loop()
