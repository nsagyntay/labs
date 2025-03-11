import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Mickey Clock")

back = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_7\mickeyclock.png")
back = pygame.transform.scale(back, (800, 700))
l_hand = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_7\right_hand.png")  
r_hand = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_7\left_hand.png")

def draw_hand(image, angle, x, y):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=(400, 350))
    screen.blit(rotated, rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(back, (0, 0))

    cur_t = time.localtime()
    min = cur_t.tm_min
    sec = cur_t.tm_sec

    sec_a = -sec * 6
    min_a = -min * 6

    draw_hand(l_hand, sec_a, 400, 350)
    draw_hand(r_hand, min_a, 400, 350)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.time.delay(1000)

pygame.quit()
