#Author: Joshua Abel
#year: 2014
#twitter: @ferguson_abel

from Player import *
from Enemy import *
from Modules import *
import pygame

pygame.mixer.init()
#setup the method to output text to screen
def createText(text, fontSize, fontColor,x, y,BgColor = None):
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    fontObj = font.render(text, True, fontColor, BgColor)
    fontObjRect = fontObj.get_rect()
    fontObjRect.topleft = x, y
    surface = pygame.display.get_surface()
    surface.blit(fontObj, fontObjRect)

#the main part of the program. it loads, initialize and display the game's layout.
def main():
    #setup or define variables and initialize them
    pygame.init()
    Text_color = (0,0,200)
    score = 0
    sound = pygame.mixer.music.load("data/main.ogg")
    frame = pygame.time.Clock()
    screen = Display().createWindow(640, 640)
    player_shoot = True
    enemy_shoot = True
    display_enemy = True
    screen.fill((0,0,234))
    size = pygame.display.get_surface().get_rect().size
    P_pos = [size[0]/2, size[1]-100]
    bullet_speed = 6 #bullet speed for player
    P_image = load_image("player.png", True)
    E_image = load_image("enemy.png", False)
    E_shot = load_image("Enemyshot.png", False)
    P_shot = load_image("Playershot.png", False)
    back = load_image("background.png", True)
    back = pygame.transform.scale(back,(650, 650))
    back_rect = back.get_rect()
    back_rect.topleft = 0, -10
    player = Player(P_image, P_shot, P_pos, bullet_speed)
    player.set_speed(50)
    EnemyList = []
    displayPlayer = True
    EnemyAddCounter = 120
    EnemyOneCounter = 60
    pygame.mouse.set_visible(True)
    bullets = [] #EnemyBullets list
    shot_speed = 8 #bullet speed for enemy
    Display().setTitle("Space Shooter")
    life = 5
    #open the score flat-file
    file = open("data/score.pck", "r")
    f = file.read()
    p_score = int(f)
    file.close()
    if(p_score == 0 or p_score < 20):
        file = open("data/score.pck", "w")
        file.write(str(20))
        p_score = 20
        file.close()
    pygame.mixer.music.play(-1, 0.0)
    while True:
        #the game-loop:
        screen.fill((0,0,234))
        EnemyAddCounter -= 1
        EnemyOneCounter -= 1
        if(EnemyAddCounter == 0):
            EnemyAddCounter = 120
            enemy = Enemy(E_image, E_shot, (random.randint(0, 315), -10), shot_speed)
            enemy.set_speed(5)
            EnemyList.append(enemy)
        
        if(EnemyOneCounter ==0):
            EnemyOneCounter = 60
            enemy = Enemy(E_image, E_shot, (random.randint(320, 575), -10),shot_speed)
            enemy.set_speed(5)
            EnemyList.append(enemy)
        
        screen.blit(back, back_rect)
        createText("Score: " +str(score), 12, Text_color,10, 10,None )
        createText("Top Score: "+str(p_score), 12, Text_color ,10, 30, None)
        createText("Life: "+str(life), 12, Text_color ,10, 50, None)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT and (player.img_rect.left - 50) >= 0:
                    player.move("left")
                if event.key == K_RIGHT and (player.img_rect.right + 50) <= 670:
                    player.move("right")
                if event.key == K_UP and (player.img_rect.top - 30) >=0:
                    player.move("up")
                if event.key == K_DOWN and (player.img_rect.bottom + 50) <= 640:
                    player.move("down")
                if event.key == K_SPACE and player_shoot:
                    player.shoot()
        for enemy in EnemyList:
            if(random.randint(0, 50) == 2) and enemy_shoot == True:
                enemy.shoot()
            if display_enemy:
                enemy.move_bullets()
                enemy.move()
                enemy.update()
        for enemy in EnemyList:
            if enemy.img_rect.y > 640:
                EnemyList.remove(enemy)
            else:
                for bull in player.bullets:
                    if bull.colliderect(enemy.img_rect):
                        bullets = enemy.bullets
                        EnemyList.remove(enemy)
                        score+= 1
                        player.bullets.remove(bull)
                for bull in enemy.bullets:
                    if(bull.colliderect(player.img_rect)):
                       enemy.bullets.remove(bull)
                       life -= 1
                              
        for rect in bullets:
            if(rect.colliderect(player.img_rect)):
                bullets.remove(rect)
                life -= 1
            if(rect.y > 640):
                bullets.remove(rect)
            else:
                rect.move_ip(0, 8)
                screen.blit(E_shot, rect)
                        
        if(life < 1):
            for bullet in player.bullets:
               player.bullets.remove(bullet)
            for bullet in bullets:
               bullets.remove(bullet)
            for bullet in enemy.bullets:
               enemy.bullets.remove(bullet)
            EnemyList = []
            displayPlayer = False
            player_shoot = False
            enemy_shoot = False
            display_enemy = False
            screen.blit(back, back_rect)
            if(p_score < score):
                file = open("data/score.pck", "w")
                file.write(str(score))
                file.close()
                createText("CONGRATULATION, YOU MADE A NEW HIGH SCORE OF ",20, Text_color,50, 310, None)
                p_score = score
            else:
                createText("GAME OVER, YOU FAILED TO MAKE A NEW HIGH SCORE ", 20, Text_color,50, 310, None)
                createText("PRESS Q TO PLAY AGAIN!!!" , 20, Text_color ,50, 330, None)
                pygame.display.update()

                wait_forkey()
                score = 0
                life = 5
                displayPlayer=True
                display_enemy = True
                enemy_shoot = True
                player_shoot = True
            
        
            
        player.move_bullets()
        if(displayPlayer == True):
            player.update()
        pygame.display.update()
        frame.tick(60)
if __name__== "__main__":
    main()

