import pygame
import random
pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Sprite Color Change Event")

white = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 200, 50, 50)
color1 = random.choice(colors)
color2 = random.choice(colors)
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR:
            color1 = random.choice(colors)
            color2 = random.choice(colors)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect1.x -= 1
    if keys[pygame.K_RIGHT]:
        rect1.x += 1
    if keys[pygame.K_UP]:
        rect1.y -= 1
    if keys[pygame.K_DOWN]:
        rect1.y += 1

    screen.fill(white)

    pygame.draw.rect(screen, color1, rect1)
    pygame.draw.rect(screen, color2, rect2)
    pygame.display.flip()
pygame.quit()
