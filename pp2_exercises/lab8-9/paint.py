import pygame

pygame.init()
screen=pygame.display.set_mode([900,700])
white=(255,255,255)
screen.fill(white)
pygame.display.set_caption("GFG Paint")
keep_going=True


WHITE=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)
GREEN=(102,204,0)
BLUE=(51,51,255)
BLACK=(0,0,0)
PINK=(255,0,255)

pygame.draw.rect(screen,RED,(0,0,50,50))
pygame.draw.rect(screen,YELLOW,(0,50,50,50))
pygame.draw.rect(screen,GREEN,(0,100,50,50))
pygame.draw.rect(screen,BLUE,(0,150,50,50))
pygame.draw.rect(screen,BLACK,(0,200,50,50))
pygame.draw.rect(screen,PINK,(0,250,50,50))
pygame.draw.rect(screen, BLACK,(0,310,50,25),2)
pygame.draw.circle(screen, BLACK,(25,370),25,2)
erasor = pygame.transform.scale(pygame.image.load("images/erasor.jpg"), (50, 50))
screen.blit(erasor, [0,395])
mousedn=False
color=BLACK
radius=5

while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousedn=True
            spot = pygame.mouse.get_pos()
            if spot[0] < 50 and spot[1] < 50:
                color= RED
            elif spot[0] < 50 and spot[1] < 100 and spot[1] > 50:
                color= YELLOW
            elif spot[0] < 50 and spot[1] < 150 and spot[1] > 100:
                color= GREEN
            elif spot[0] < 50  and spot[1] < 200 and spot[1] > 150:
                color= BLUE
            elif spot[0] < 50 and spot[1] < 250 and spot[1] > 200:
                color= BLACK
            elif spot[0] < 50 and spot[1] < 300 and spot[1] > 250:
                color= PINK
            elif spot[0] < 50 and spot[1] < 445 and spot[1] > 395:
                color = WHITE
            
        if event.type==pygame.MOUSEBUTTONUP:
            mousedn=False
        if mousedn:
            spot = pygame.mouse.get_pos()
            if spot[0]>50:
                pygame.draw.circle(screen,color,spot,radius)
        pygame.display.update()
pygame.quit()