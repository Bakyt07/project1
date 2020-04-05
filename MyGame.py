import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
сounter = pygame.time.Clock()
score_sur = pygame.Surface((200, 35))
score_shrift = pygame.font.Font(None, 30)
backgroundImage = pygame.image.load("hogwarts1.png")
playerImage = pygame.image.load("hpsmall1.png")
player_x = 200
player_y = 500

enemyImage = pygame.image.load("dmsmall1.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(20, 50)

enemy_dx = 3
enemy_dy = 25

molniyaImage = pygame.image.load("m1.png")
molniya_x = 800
molniya_y = 0
molniya_dy = 5

a = False 
b = False 
c = False 
def player(x, y):
   screen.blit(playerImage, (x, y))

def enemy(x, y):
  screen.blit(enemyImage, (x, y))

def molniya(x, y):
   screen.blit(molniyaImage, (x, y))

def over(enemy_y):
    if enemy_y > 450:
        return True
    return False
score = 0
done = False
while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: 
           done = True
      pressed = pygame.key.get_pressed() 
      if pressed[pygame.K_SPACE] and b is False:   
         molniya_y = 430
         molniya_x = player_x + 35
         b = True
         c = True
       
    if enemy_y <= molniya_y <= enemy_y + 65 and enemy_x <= molniya_x <= enemy_x + 65:  
        molniya_y = 0
        molniya_x = 800
        a = True
        enemy_x, enemy_y = random.randint(0, 534), random.randint(35, 65)
        score += 1
    if molniya_y == 0:
        c = False
        bullet_y = 600
        b = False
    if pressed[pygame.K_LEFT] and player_x >= 2:
         player_x -= 3
    if pressed[pygame.K_RIGHT] and player_x <= 736: 
        player_x += 3
    enemy_x += enemy_dx
    if enemy_x < 0 or enemy_x > 736:
       enemy_dx = -enemy_dx
       enemy_y += enemy_dy

    if c is not False: molniya_y -= molniya_dy

    score_sur.fill((66,66,245))
    score_sur.blit(score_shrift.render("SCORE:"+str(score), 1, (255,255,255)), (0,0))

    if over(enemy_y) != 0:
        screen.fill((167, 230, 60)) and font.render( True, (0, 0, 0))
    screen.blit(backgroundImage, (0, 0))
    player(player_x, player_y)
    molniya(molniya_x, molniya_y)
    enemy(enemy_x, enemy_y)
    screen.blit(score_sur,(0,0))
    pygame.display.flip()
