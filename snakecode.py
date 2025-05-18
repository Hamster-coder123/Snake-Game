import pygame
import random
import time
import os


pygame.init()



class maingame:
    def __init__(self):
        self.X = 440
        self.Y = 440
        self.deaths = 0
        self.snakevel = 40
        self.isL = False
        self.isR = False
        self.isU = False
        self.isD = False
        self.moving = False
        self.moving = [self.isL, self.isR, self.isU, self.isD]



        pygame.display.set_caption("Interactive window")

    def draw(self, win, block):
        self.back = pygame.image.load("background.jpg")
        win.blit(self.back,(0,0))
        self.font = pygame.font.SysFont(None, 70)
        self.img = self.font.render(f'{ self.deaths} deaths', True, (255,255,255))
        win.blit(self.img, (760,20))
        block.draw()

    def move(self, block, block2, block3):
        keys = pygame.key.get_pressed()

        if(((keys[pygame.K_a] and not self.isR) or self.isL) and (block.X > 0) ):
            blockold = block.X
            block2old = block2.X
            block2.X = blockold
            block3.X = block2old
            block.X = block.X - self.snakevel
            # win.blit(block.block,(block.X, block.Y))    
            self.isL = True
            self.isR = False
            self.isU = False
            self.isD = False

        if(((keys[pygame.K_d] and not self.isL) or self.isR) and (block.X < 960) ):
            blockold = block.X
            block2old = block2.X
            block2.X = blockold
            block3.X = block2old
            block.X = block.X + self.snakevel
            # win.blit(block.block,(block.X, block.Y))   
            self.isR = True
            self.isL = False
            self.isU = False
            self.isD = False

        if(((keys[pygame.K_w] and not self.isD) or self.isU) and (block.Y > 0)):
            blockold = block.Y
            block2old = block2.Y
            block2.Y = blockold
            block3.Y = block2old
            block.Y = block.Y - self.snakevel
            # win.blit(block.block,(block.X, block.Y))    
            self.isU = True
            self.isL = False
            self.isR = False
            self.isD = False

        if(((keys[pygame.K_s] and not self.isU) or self.isD) and (block.Y < 960)):
            blockold = block.Y
            block2old = block2.Y
            block2.Y = blockold
            block3.Y = block2old
            block.Y = block.Y + self.snakevel
            # win.blit(block.block,(block.X, block.Y))   
            self.isD = True
            self.isL = False
            self.isU = False
            self.isR = False

    

        pygame.time.delay(100)


class blocks:
    def __init__(self, X, Y ):
        self.X = X
        self.Y = Y
        self.block = pygame.image.load("block.jpg")
        

    def draw(self):
        win.blit(self.block,( self.X, self.Y))   
        print(self.X, self.Y)




run = True

win = pygame.display.set_mode((1000, 1000))



game = maingame()

block = blocks(game.X, game.Y)

block2 = blocks(game.X + 40, game.Y )

block3 = blocks(game.X + 80, game.Y )


blocklist = []

while run:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
    game.draw(win, block)
    game.move(block, block2, block3)
    block2.draw()
    block3.draw()
   
    pygame.display.update()
    