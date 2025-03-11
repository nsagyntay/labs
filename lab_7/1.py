import pygame
import time
import math
from datetime import datetime

pygame.init()
w = 600
h = 600
c = (w // 2, h// 2)
back_color = (255 ,255 ,255)

screen = pygame.display.set_mode((w , h ))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

back = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_7\mickeyclock.png")
r_hand = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_7\left_hand.png")
l_hand = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_7\right_hand.png")


back = pygame.transform.scale(back,(w,h))
r_hand = pygame.transform.scale(r_hand, (255,100))
l_hand = pygame.transform.scale(l_hand, (255, 100))


r_hand_offset = (0,0)
l_hand_offset = (0,0)

def rot_center(image, angle, offset):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=(c[0] + offset[0], c[1] + offset[1]))
    screen.blit(rotated_image, rect.topleft)

running = True
while running:
    screen.fill(back_color)
    screen.blit(back, (0, 0))

    now = datetime.now()
    min = now.minute
    sec = now.second
    
    min_angle = -(min % 60) * 6 
    sec_angle = -(sec % 60) * 6

    rot_center(r_hand,min_angle, r_hand_offset)
    rot_center( l_hand, sec_angle, l_hand_offset)        

    pygame.display.flip()
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
