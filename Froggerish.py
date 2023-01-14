import pygame
import random as r
pygame.init()
SCREEN=pygame.display.set_mode((840,650))
BG=pygame.image.load('road.png')
COORDS=[190,310,430,570,]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CLOCK = pygame.time.Clock()
FONT = pygame.font.Font(None, 72)
start=False
starttime=pygame.time.get_ticks()


def redraw(time):
    SCREEN.blit(BG,(0,0))
    text = FONT.render("Time= " + str(time), 1, BLACK)
    if start:        
        SCREEN.blit(text,(0,0))
    c1.draw()
    c2.draw()
    player.draw()
    pygame.display.update()



class car(object):
    def __init__(self,skin,velocity,x):
        self.skin=skin
        self.velocity=velocity
        self.x=x
        self.y=0
    def draw(self):
        SCREEN.blit(self.skin,(self.x,self.y))
        self.y+=self.velocity
        
        
class man(object):
    def __init__(self):
        self.x=70
        self.y=575
        self.skin=pygame.image.load('player.png')
    def draw(self):
        SCREEN.blit(self.skin,(self.x,self.y))
        

        
x=9
c1=car(pygame.image.load('car.jpg'),r.randint(9,x),COORDS[r.randint(0,1)])        
c2=car(pygame.image.load('car.jpg'),r.randint(9,x),COORDS[r.randint(2,3)])        
player=man()        

game=True
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] or keys[pygame.K_2] or keys[pygame.K_3] or keys[pygame.K_4]:
            if not start:
                starttime=pygame.time.get_ticks()
                start=True
        if keys[pygame.K_1]:
            player.x=190
        elif keys[pygame.K_2]:
            player.x=310
        elif keys[pygame.K_3]:
            player.x=430
        elif keys[pygame.K_4]:
            player.x=570    
        if c1.y>=650:
            x=x+1
            c1=car(pygame.image.load('car.jpg'),r.randint(9,x),COORDS[r.randint(0,1)])
        if c2.y>=650:
            x=x+1
            c2=car(pygame.image.load('car.jpg'),r.randint(9,x),COORDS[r.randint(2,3)])
        if (c1.y+160>=player.y and c1.y<player.y and c1.x==player.x) or (c2.y+160>=player.y and c2.y<player.y and c2.x==player.x):
            game=False
        time=pygame.time.get_ticks()-starttime
        time=time/1000
        redraw(time)
    else:
        SCREEN.blit(BG,(0,0))
        text = FONT.render("Game Over, You lasted", 1, BLACK)
        text2= FONT.render(str(time)+ "seconds", 1, BLACK)
        SCREEN.blit(text,(170,149))
        SCREEN.blit(text2,(170,199))
        SCREEN.blit(c1.skin,(c1.x,c1.y))
        SCREEN.blit(c2.skin,(c2.x,c2.y))
        SCREEN.blit(player.skin,(player.x,player.y))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game=True
            x=9
            c1=car(pygame.image.load('car.jpg'),r.randint(9,x),COORDS[r.randint(0,1)])        
            c2=car(pygame.image.load('car.jpg'),r.randint(9,x),COORDS[r.randint(2,3)])        
            player=man()        

       
                    
pygame.quit()