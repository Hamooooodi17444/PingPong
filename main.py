import pygame
import sys

svart = (0, 0, 0)
röd = (255, 0, 0)

pygame.init()

storlek = (800, 600)
screen = pygame.display.set_mode(storlek)
rectx = 400
recty = 580

bollx = 50
bolly = 50

boll_justering_x = 0
boll_justering_y = 0

score = 0


def drawrect(skärm, x, y):
    if x <= 0:
        x = 0
    if x >= 700:
        x = 700
    pygame.draw.rect(skärm, röd, (x, y, 100, 20))


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Uppdatera spellogik här

    screen.fill(svart)
    drawrect(screen, rectx, recty)

    pygame.display.flip()
    clock.tick(60)