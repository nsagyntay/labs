import pygame
import random

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
CELL_SIZE = 20
WHITE =(255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")


font = pygame.font.SysFont("Arial", 24)

walls = [(x, 0) for x in range(0, SCREEN_WIDTH, CELL_SIZE)] + \
        [(x, SCREEN_HEIGHT - CELL_SIZE) for x in range(0, SCREEN_WIDTH, CELL_SIZE)] + \
        [(0, y) for y in range(0, SCREEN_HEIGHT, CELL_SIZE)] + \
        [(SCREEN_WIDTH - CELL_SIZE, y) for y in range(0, SCREEN_HEIGHT, CELL_SIZE)]

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"
        self.grow = False

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE
        new_head = (x, y)

        if new_head in self.body or new_head in walls:
            return False
        
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        
        return True

    def change_direction(self, new_direction):
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposite[self.direction]:
            self.direction = new_direction


class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        while True:
            x = random.randint(1, (SCREEN_WIDTH // CELL_SIZE) - 2) * CELL_SIZE
            y = random.randint(1, (SCREEN_HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
            if (x, y) not in walls and (x, y) not in snake.body:
                return x, y

    def respawn(self):
        self.position = self.generate_position()


snake = Snake()
food = Food()
running = True
clock = pygame.time.Clock()
score = 0
level = 1
speed = 10  


while running:
    screen.fill(WHITE)  
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    
    if not snake.move():
        running = False  

    
    if snake.body[0] == food.position:
        snake.grow = True
        food.respawn()
        score += 1

    
        if score % 3 == 0:
            level += 1
            speed += 2  
    
    
    for wall in walls:
        pygame.draw.rect(screen, BLACK, (*wall, CELL_SIZE, CELL_SIZE))

    
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, RED, (*food.position, CELL_SIZE, CELL_SIZE))

    
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()  
    clock.tick(speed) 

pygame.quit()
