import pygame
import time 
import os

pygame.init()




WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Game made by Alp")
velocity = 3
bulletvelocity = 7
fps = 60
RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2
font = pygame.font.SysFont("Arial", 40)
yellowwin = font.render("Yellow Hit!", 1, "yellow")
redwin = font.render("Red Hit!", 1, "red")
yscore = 0
rscore = 0
yellowscore = font.render("Yellow Score: ",  1, "yellow"  )
redscore = font.render("Red Score: ",  1, "red")
yellowscore1 = font.render(str(yscore), 1, "yellow")
redscore1 = font.render(str(rscore), 1, "red")
pygame.display.update()



background = pygame.transform.scale(pygame.image.load(os.path.join("space invaders/background.png")), (WIDTH, HEIGHT))
ship1 = pygame.image.load(os.path.join("space invaders/yellowship.png"))
yellowship = pygame.transform.rotate(pygame.transform.scale(ship1, (60, 40)), 90)
ship2 = pygame.image.load(os.path.join("space invaders/redship.png"))
redship = pygame.transform.rotate(pygame.transform.scale(ship2, (60, 40)), 270)

def draw_window(red,yellow,redbullet,yellowbullet):
    screen.blit(background, (0,0))
    screen.blit(yellowship, (yellow.x,yellow.y))
    screen.blit(redship, (red.x,red.y))
    screen.blit(yellowscore, (300, 500))
    screen.blit(redscore, (700,500))
    
    for i in redbullet:
        pygame.draw.rect(screen, "red", i)
    for i in yellowbullet:
        pygame.draw.rect(screen, "yellow", i)
    pygame.display.update()


def yellowshipmovement(keypress, yellow):
    if keypress[pygame.K_a]:
        yellow.x -= velocity
    if keypress[pygame.K_d]:
        yellow.x += velocity
    if keypress[pygame.K_s]:
        yellow.y += velocity
    if keypress[pygame.K_w]:
        yellow.y -= velocity
    
def redshipmovement(keypress, red):
    if keypress[pygame.K_LEFT]:
        red.x -= velocity
    if keypress[pygame.K_RIGHT]:
        red.x += velocity
    if keypress[pygame.K_DOWN]:
        red.y += velocity
    if keypress[pygame.K_UP]:
        red.y -= velocity

def handlebullets(yellowbullet, redbullet, yellow, red):
    global rscore, yscore
    for i in yellowbullet:
        i.x += bulletvelocity
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(RED_HIT))
            screen.blit(yellowwin, (300,300))
            yscore = yscore + 1
            pygame.display.update()
            time.sleep(0.01)
            
            
    for i in redbullet:
        i.x -= bulletvelocity
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            screen.blit(redwin, (300,300))
            rscore = rscore + 1
            pygame.display.update()
            time.sleep(0.01)
            
            
def main():
    red = pygame.Rect(700,300,60,40)
    yellow = pygame.Rect(100,300,60,40)
    redbullet = []
    yellowbullet = []

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LSHIFT:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellowbullet.append(bullet)

                if i.key == pygame.K_RSHIFT:
                    bullet = pygame.Rect(red.x + red.width,red.y + red.height // 2 - 2, 10, 5)
                    redbullet.append(bullet)
        keypress = pygame.key.get_pressed()
        yellowshipmovement(keypress, yellow)
        redshipmovement(keypress, red)
        handlebullets(yellowbullet, redbullet, yellow, red)
        draw_window(red, yellow, redbullet, yellowbullet)

if __name__ == "__main__":
    main()
