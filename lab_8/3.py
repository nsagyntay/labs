import pygame
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing_mode = 'line' 
    drawing = False 
    current_pos = None 
    
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # определяем, если X был нажат, или использован Ctrl+W или Alt+F4
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # выбор цвета
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                # выбор режима рисования:
                # Rежим линии (L), прямоугольника (Q), круга (C) и ластика (E)
                elif event.key == pygame.K_l:
                    drawing_mode = 'line'
                elif event.key == pygame.K_q:
                    drawing_mode = 'rect'
                elif event.key == pygame.K_c:
                    drawing_mode = 'circle'
                elif event.key == pygame.K_e:
                    drawing_mode = 'eraser'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка мыши (или тачпад)
                    if drawing_mode == 'line':
                        # В режиме линии, как и раньше, левая кнопка увеличивает радиус
                        radius = min(200, radius + 1)
                        # И добавляем начальную точку в список
                        points = points + [event.pos]
                    else:
                        # Для других режимов начинаем рисование и запоминаем стартовую позицию
                        drawing = True
                        start_pos = event.pos
                        current_pos = event.pos
                elif event.button == 3:  # правая кнопка мыши уменьшает радиус
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    # Завершаем рисование для режимов фигур
                    drawing = False
                    start_pos = None
                    current_pos = None
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing_mode == 'line':
                    # в режиме линии добавляем точки в список (как было)
                    points = points + [position]
                    points = points[-256:]
                else:
                    if drawing:
                        current_pos = position
                
        screen.fill((0, 0, 0))
        
        #line
        if drawing_mode == 'line':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1
        
        #rect
        if drawing_mode == 'rect' and drawing and start_pos and current_pos:
            rect_width = current_pos[0] - start_pos[0]
            rect_height = current_pos[1] - start_pos[1]
            pygame.draw.rect(screen, COLORS[mode], (start_pos[0], start_pos[1], rect_width, rect_height), 2)
        
        
        if drawing_mode == 'circle' and drawing and start_pos and current_pos:
            center_x = (start_pos[0] + current_pos[0]) // 2
            center_y = (start_pos[1] + current_pos[1]) // 2
            circle_radius = int(max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1])) // 2)
            pygame.draw.circle(screen, COLORS[mode], (center_x, center_y), circle_radius, 2)
        
        # eraser
        if drawing_mode == 'eraser' and drawing and current_pos:
            pygame.draw.circle(screen, WHITE, current_pos, radius)
        
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

COLORS = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}

main()
