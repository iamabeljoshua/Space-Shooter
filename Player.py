#Author: Joshua Abel
#year: 2014
#twitter: @ferguson_abel

import pygame
import Sprites
'''Defines the player class
'''
class Player(Sprites.Sprite):
    #defines the constructor
    def __init__(self, img, b_img, position, b_speed):
        #initialize or setup the variables
        Sprites.Sprite.__init__(self,img, position)
        self.bullet_img = b_img
        self.bullet_rect = self.bullet_img.get_rect()
        self.bullet_speed = b_speed
        self.bullets = []
        self.score = 0
    #defines the method that allow the player to shoot at enemies
    def shoot(self):
        bullet = self.bullet_img.get_rect()
        bullet.topleft = self.img_rect.center
        self.bullets.append(bullet)
    #defines the method that moves the bullet targeted at enemies
    def move_bullets(self):
        for bullet in self.bullets:
            s = pygame.display.get_surface()
            s.blit(self.bullet_img, bullet)
            bullet.move_ip(0, -self.bullet_speed)
        for bullet in self.bullets:
            if bullet.y < 0:
                self.bullets.remove(bullet)

        
