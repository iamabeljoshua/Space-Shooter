#Author: Joshua Abel
#year: 2014
#twitter: @ferguson_abel

from Player import *
import random
#create the Enemy class and inherit the Player class
class Enemy(Player):
    #setup the constructor
    def __init__(self, img, b_img, position,b_speed):
        Player.__init__(self, img,b_img, position, b_speed)
    #the method that controls enemies movement
    def move(self):
        x =0
        y = self.speed
        self.img_rect.move_ip(x,y)
    #the method that moves enemies bullets targeted at player
    def move_bullets(self):
        for bullet in self.bullets:
            s = pygame.display.get_surface()
            s.blit(self.bullet_img, bullet)
            bullet.move_ip(0, self.bullet_speed)
        for bullet in self.bullets:
            if bullet.y > 640:
                self.bullets.remove(bullet)
    
    
        
    
