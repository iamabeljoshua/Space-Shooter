#Author: Joshua Abel
#year: 2014
#twitter: @ferguson_abel

import pygame, sys, os
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]
class Display():
    """THIS IS A CLASS FOR ALL SORT OF DISPLAY IN GAMES"""
    def __init__(self):
        pass
    def createWindow(self, width, height):
        return pygame.display.set_mode((width, height))
    def setTitle(self, title):
        pygame.display.set_caption(title)
    def createButton(self, text,fontSize,fontColor,x, y, BgColor = None):
        font = pygame.font.Font('freesansbold.ttf',fontSize)
        if BgColor == None:
            nameObj = font.render(text, True, fontColor)
        else:
            nameObj = font.render(text, True, fontColor, BgColor)
        nameObjRect = nameObj.get_rect()
        nameObjRect.topleft = x, y
        surface = pygame.display.get_surface()
        surface.blit(nameObj, nameObjRect)
        return(nameObjRect)
    def createText(self, text, fontSize, fontColor,x, y,BgColor = None):
        font = pygame.font.Font('freesansbold.ttf', fontSize)
        fontObj = font.render(text, True, fontColor, BgColor)
        fontObjRect = fontObj.get_rect()
        fontObjRect.topleft = x, y
        surface = pygame.display.get_surface()
        surface.blit(fontObj, fontObjRect)
        
class Transfrom(object):
    """ THIS IS A CLASS FOR ALL SORT OF TRANSFORMATION TO GAME OBJECTS AND SPRITES"""
    def __init__(self):
        pass
    @staticmethod
    def scaleImage(self, img, size):
        return pygame.transform.scale(img,(size))
    @staticmethod
    def rotateImage(self, img, angle):
        return pygame.transform.rotate(img, angle)
    

def load_sound(path):
    path = os.path.join(main_dir, "data", path)
    if not pygame.mixer:
        return None
    try:
        data = pygame.mixer.Sound(path)
    except pygame.error:
        print("Sorry, couldn't load image " +(path) + " " + pygame.get_error())
    return data

def load_image(path, transparent):
    path = os.path.join(main_dir, "data", path)
    if not pygame.image:
        return None
    try:
        data = pygame.image.load(path)
    except pygame.error:
        print("Couldn't load image file " + path+ " " + pygame.get_error())
    if transparent:
        corner = data.get_at((0,0))
        data.set_colorkey(corner, RLEACCEL)
    return data.convert()

def pause():
    while True:
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == ord("p"):
                    return
def terminate():
    pygame.quit()
    sys.exit()
def wait_forkey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == ord("q"):
                    return
            

    

            

            
        
