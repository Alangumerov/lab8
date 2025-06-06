import pygame
import random

pygame.init()
#дисплей
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гонщик")
#скорость игрока и врагов
player_speed = 4
enemy_speed = 3
#фон
bg_image = pygame.image.load('images/AnimatedStreet.png')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
#картинки 
player = pygame.image.load('images/Player.png')
enemy = pygame.image.load('images/Enemy.png')
coin=pygame.image.load('images/images.png')
coin=pygame.transform.scale(coin, (30,30))
#начальные координаты игрока
player_x = 190
player_y = 400
#появление врагов
enemy_x = random.randint(50, WIDTH - 50)
enemy_y = -100

moving_left = False
moving_right = False
#шрифт 
font = pygame.font.Font(None, 50)
game_over_text = font.render("GAME OVER", True, (255, 255, 255))

game_over_flag = False
score=0
score_font=pygame.font.Font(None, 50)
coin_x=random.randint(50,WIDTH-50)
coin_y=-100
coin_speed=2
coin_score=0
coin_score_font=pygame.font.Font(None,50)
running = True
while running:
    #управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    if not game_over_flag:
        if moving_left and player_x > 0:
            player_x -= player_speed
        if moving_right and player_x < WIDTH - player.get_width():
            player_x += player_speed
        #появвление врагов и счет очков
        enemy_y += enemy_speed
        if enemy_y > HEIGHT:
            enemy_x = random.randint(50, WIDTH - 50)
            enemy_y = -100
            score+=1
        coin_y+=coin_speed
        if coin_y>HEIGHT:

            coin_x=random.randint(50,WIDTH-50)
            coin_y=-100

        player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy.get_width(), enemy.get_height())
        coin_rect=pygame.Rect(coin_x,coin_y, coin.get_width(), coin.get_height())
         #столкновение
        if player_rect.colliderect(enemy_rect):
            game_over_flag = True

        if player_rect.colliderect(coin_rect):
           coin_score += 1
           coin_x=random.randint(50, WIDTH-50)
           coin_y=-100

    score_text = score_font.render(str(score), True, (0, 0, 1))
    coin_score_text=coin_score_font.render(str(coin_score), True, (0,0,1))
    screen.blit(bg_image, (0, 0))
    screen.blit(enemy, (enemy_x, enemy_y))
    screen.blit(player, (player_x, player_y))
    screen.blit(score_text,(20,10))
    screen.blit(coin,(coin_x,coin_y))
    screen.blit(coin_score_text,(300,10))

  
    if game_over_flag:
        screen.fill((255, 0, 0))
        screen.blit(game_over_text, (100, 250))

    pygame.display.update()

pygame.quit()
