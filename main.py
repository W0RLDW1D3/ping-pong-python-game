import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

# Set up game objects
paddle_width = 10
paddle_height = 60
paddle_speed = 5
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3

paddle_a_x = 50
paddle_a_y = height // 2 - paddle_height // 2
paddle_b_x = width - 50 - paddle_width
paddle_b_y = height // 2 - paddle_height // 2

ball_x = width // 2
ball_y = height // 2
ball_dx = random.choice([-1, 1]) * ball_speed_x
ball_dy = random.choice([-1, 1]) * ball_speed_y

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a_y > 0:
        paddle_a_y -= paddle_speed
    if keys[pygame.K_s] and paddle_a_y < height - paddle_height:
        paddle_a_y += paddle_speed
    if keys[pygame.K_UP] and paddle_b_y > 0:
        paddle_b_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_b_y < height - paddle_height:
        paddle_b_y += paddle_speed

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with paddles
    if (
        ball_x <= paddle_a_x + paddle_width
        and paddle_a_y <= ball_y <= paddle_a_y + paddle_height
    ) or (
        ball_x >= paddle_b_x - ball_radius
        and paddle_b_y <= ball_y <= paddle_b_y + paddle_height
    ):
        ball_dx *= -1

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_dy *= -1

    # Ball out of bounds
    if ball_x <= 0 or ball_x >= width - ball_radius:
        ball_x = width // 2
        ball_y = height // 2
        ball_dx = random.choice([-1, 1]) * ball_speed_x
        ball_dy = random.choice([-1, 1]) * ball_speed_y

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, (255, 255, 255), (paddle_a_x, paddle_a_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_b_x, paddle_b_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
