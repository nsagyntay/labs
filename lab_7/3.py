#Draw circle - a red ball of size 50 x 50
#  (radius = 25) on white background. When
#  user presses Up, Down, Left, Right arrow
#  keys on keyboard, the ball should move by
#  20 pixels in the direction of pressed key.
#  The ball should not leave the screen, i.e.
#  user input that leads the ball to leave of 
# the screen should be ignored
import pygame

pygame.init()

w=500
h = 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption(" Red Ball")

r = 25
x= w // 2
y =h // 2
speed = 20

running = True
while running:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x - r - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x+ r + speed <= w:
        x += speed
    if keys[pygame.K_UP] and y - r - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + r + speed <= h:
        y += speed
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)
    pygame.display.update()
    
pygame.quit()