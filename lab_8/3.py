import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
COLORS = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}

# Экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing App")
clock = pygame.time.Clock()

radius = 15
mode = 'blue'
drawing_mode = 'line'
points = []
start_pos = None
drawing = False
position = (0, 0)

def drawLineBetween(screen, index, start, end, width, color):
    pygame.draw.line(screen, color, start, end, width)

def main():
    global mode, drawing_mode, radius, start_pos, drawing ,points

    running = True
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                elif event.key == pygame.K_e:
                    drawing_mode = 'eraser'
                elif event.key == pygame.K_l:
                    drawing_mode = 'line'
                elif event.key == pygame.K_c:
                    drawing_mode = 'circle'
                elif event.key == pygame.K_t:
                    drawing_mode = 'rect'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                    drawing = True
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #Stop draw
                    drawing = False
                    start_pos = None
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                 if drawing:
                    position = event.pos
                    if drawing_mode == 'line':
                        points.append(position)
                        points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        # rectangle
        if drawing and drawing_mode == 'rect' and start_pos:
            pygame.draw.rect(screen, COLORS[mode], (*start_pos, position[0] - start_pos[0], position[1] - start_pos[1]), 2)

        # circle
        if drawing and drawing_mode == 'circle' and start_pos:
            center_x = (start_pos[0] + position[0]) // 2
            center_y = (start_pos[1] + position[1]) // 2
            radius = max(abs(start_pos[0] - position[0]), abs(start_pos[1] - position[1])) // 2
            pygame.draw.circle(screen, COLORS[mode], (center_x, center_y), radius, 2)
        if event.type == pygame.MOUSEMOTION and drawing:
            position = event.pos
            if drawing_mode == 'eraser':
                pygame.draw.circle(screen, WHITE, position, radius)
            elif drawing_mode == 'line':
                points.append(position)
                points = points[-256:]
        # eraser
        if drawing and drawing_mode == 'eraser':
            pygame.draw.circle(screen, WHITE, position, radius)
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()