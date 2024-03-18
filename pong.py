import pygame, sys, random

# Initialize pygame and font
pygame.init()
pygame.font.init()  # Initialize font module

# Set up main window
screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Colors and game objects
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Speed settings
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# Score variables
player_score = 0
opponent_score = 0

# Font for displaying scores
font = pygame.font.Font(None, 74)  # Default font, size 74

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        if ball.left <= 0:
            player_score += 1  # Player scores
        else:
            opponent_score += 1  # Opponent scores
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

def draw_score():
    player_score_text = font.render(str(player_score), True, light_grey)
    opponent_score_text = font.render(str(opponent_score), True, light_grey)
    screen.blit(player_score_text, (screen_width / 2 + 20, 20))
    screen.blit(opponent_score_text, (screen_width / 2 - 45, 20))

clock = pygame.time.Clock()

while True:
    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    draw_score()  # Draw scores on the screen

    pygame.display.flip()
    clock.tick(60)
