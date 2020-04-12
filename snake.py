import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
lemonImage = pygame.image.load("lemon1.png")

class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5 
        self.dy = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Lemon:
    def _init_(self):
        self.x = random.randint(30, 740)
        self.y = random.randint(30, 740)
    def draw(self):
        screen.blit (lemonImage, (self.x, self.y))
    
def impact():
        if (lemon.x>= snake.elements[0][0]-27 and lemon.x<snake.elements[0][0]+27) and  (lemon.y >= snake.elements[0][1]-27 and lemon.y<snake.elements[0][1] +27):
         snake.is_add = True
         if snake.is_add == True:
            snake.score +=1
            lemon.x = random.randint(10, 750)
            lemon.y = random.randint(10, 550)
    
def Scores():
     font = pygame.font.SysFont(50, 30)
     score = font.render("score " + str(snake.score), True, (0,0,0))
     screen.blit(score, (575, 34))
def limit():
        if snake.elements[0][0]>=760 or snake.elements[0][0]<=30 or snake.elements[0][1]<=30 or snake.elements[0][1]>=575:
            return True
        return False    
def crush():
     for block in snake.elements[1:]:
        if snake.elements[0][0] == block[0] and snake.elements[0][1] == block[1]:
            return True
     return False
def endgame():
     snake.dx=0
     snake.dy=0
     snake.radius=0
snake = Snake()
lemon=Lemon()
running = True
score=0
d = 3

    
snake = Snake()

running = True

d = 5

FPS = 30

clock = pygame.time.Clock()

k1_pressed = False

while running:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = d
            if event.key == pygame.K_1:
                snake.is_add = True
        snake.move()
        screen.fill((0, 0, 0))
        snake.draw()
        lemon.draw()
        lemon.impact()
    
    

        pygame.display.flip()
