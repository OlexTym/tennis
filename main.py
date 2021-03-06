
from icecream.icecream import colorizedStderrPrint
import pygame
from datetime import datetime
from icecream import ic

from colors import Colors
from player import Player
from ball import Ball


# Icecream
def time_format():
    return f'{datetime.now()}|> '


ic.configureOutput(prefix=time_format)

pygame.init()

# Screen
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 820
screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
# Windows title
pygame.display.set_caption("Tennis v1")

# Play will be active if playactive = true
play_active = True

# Update window
fps = 60
clock = pygame.time.Clock()

# Define pleyer 1
player_one_x = 20
player_one_y = 20
player_one = Player(screen, Colors.WHITE, player_one_x, player_one_y)
player_one_up = False
player_one_down = False

# Define pleyer 2
player_two_x = screen.get_width() - 40
player_two_y = 20
player_two = Player(screen, Colors.WHITE, player_two_x, player_two_y)
player_two_up = False
player_two_down = False

ball = Ball(screen, Colors.WHITE)
# Main cycle
while(play_active):

    # Check event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_active = False
        # Key pressed
        elif event.type == pygame.KEYDOWN:

            # Player one
            if event.key == pygame.K_w:
                ic("Player one")
                player_one_up = True
            elif event.key == pygame.K_s:
                ic("Player one")
                player_one_down = True
            # Player two
            elif event.key == pygame.K_UP:
                ic("Player two")
                player_two_up = True
            elif event.key == pygame.K_DOWN:
                ic("Player two")
                player_two_down = True

        # Key reliase
        elif event.type == pygame.KEYUP:
            # Player one
            if event.key == pygame.K_w:
                ic("Player one")
                player_one_up = False
            elif event.key == pygame.K_s:
                ic("Player one")
                player_one_down = False
            elif event.key == pygame.K_UP:
                ic("Player two")
                player_two_up = False
            elif event.key == pygame.K_DOWN:
                ic("Player two")
                player_two_down = False

    # Refresh play window (delete all)
    screen.fill(Colors.BLACK)

    # Ball
    ball.draw_ball()
    ball.move_ball()

    # Player
    player_one.draw_racket()
    player_two.draw_racket()

    if player_one_up:
        player_one.move_up()
    if player_one_down:
        player_one.move_down()

    if player_two_up:
        player_two.move_up()
    if player_two_down:
        player_two.move_down()

    if player_one.racket.colliderect(ball.ball):
        ic("Shoot one")
        ball.racket_shoot()

    if player_two.racket.colliderect(ball.ball):
        ic("Shoot two")
        ball.racket_shoot()
    # Update window
    pygame.display.flip()

    # Update-time
    clock.tick(fps)

pygame.quit()
