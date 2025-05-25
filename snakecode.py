import pygame
import random
import time
import os


pygame.init()



class maingame:
    def __init__(self, length):
        
        self.length = length
        self.X = [440] * length
        self.Y = [440] * length
        self.deaths = 0
        self.snakevel = 40
        self.isL = False
        self.isR = False
        self.isU = False
        self.isD = False
        self.moving = False
        self.moving = [self.isL, self.isR, self.isU, self.isD]
        self.block = pygame.image.load("block.jpg")


        pygame.display.set_caption("Interactive window")

    def draw(self, win):
        self.back = pygame.image.load("background.jpg")
        win.blit(self.back,(0,0))
        self.font = pygame.font.SysFont(None, 70)
        self.img = self.font.render(f'{ self.deaths} deaths', True, (255,255,255))
        win.blit(self.img, (760,20))
        for i in range(length):
            win.blit(self.block,(self.X[i],self.Y[i]))   
        



    def move(self):
        keys = pygame.key.get_pressed()

        for i in range (self.length - 1,0, -1):
            self.X[i] = self.X[i - 1]
            self.Y[i] = self.Y[i - 1]




        if(((keys[pygame.K_a] and not self.isR) or self.isL) and (self.X[0] > 0) ):
            self.X[0] -= self.snakevel
            # win.blit(block.block,(block.X, block.Y))    
            self.isL = True
            self.isR = False
            self.isU = False
            self.isD = False

        if(((keys[pygame.K_d] and not self.isL) or self.isR) and (self.X[0] < 960) ):
            self.X[0] += self.snakevel
            # win.blit(block.block,(block.X, block.Y))   
            self.isR = True
            self.isL = False
            self.isU = False
            self.isD = False

        if(((keys[pygame.K_w] and not self.isD) or self.isU) and (self.Y[0] > 0)):
            self.Y[0] -= self.snakevel
            # win.blit(block.block,(block.X, block.Y))    
            self.isU = True
            self.isL = False
            self.isR = False
            self.isD = False

        if(((keys[pygame.K_s] and not self.isU) or self.isD) and (self.Y[0] < 960)):
            self.Y[0] += self.snakevel
            # win.blit(block.block,(block.X, block.Y))   
            self.isD = True
            self.isL = False
            self.isU = False
            self.isR = False

    

        pygame.time.delay(100)






run = True

win = pygame.display.set_mode((1000, 1000))

length = int(input("What length will the snake start at. "))

game = maingame(length)






while run:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
    game.draw(win)
    game.move()

   
    pygame.display.update()
    