import pygame
import random
from pygame.math import *
import sys

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake,self).__init__()
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    def draw_snake(self):
        for block in self.body:
            pygame.draw.rect(screen,BLUE,(block.x*cell_size,block.y*cell_size,cell_size,cell_size))
            
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class Snack:
    def __init__(self):
        self.randomize()


    def draw_snack(self):
        snack_rect = pygame.Rect(self.pos[0]*cell_size,self.pos[1]*cell_size,cell_size,cell_size)
        screen.blit(grusha,snack_rect)

    def randomize(self):
        self.x = random.randint(0,cell_num-1)
        self.y = random.randint(0,cell_num-1)
        self.pos = [self.x,self.y]


    def draw_wall(self):
        self.screen.blit(Wall,(0,0))

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super(Wall,self).__init__()

    def draw_wall(self):
        image_wall = pygame.image.load('C:\\Users\\user\\Desktop\\snake\\image\\wall.png')
        wall_rect = image_wall.get_rect()
        screen.blit(image_wall,(0,0))

class Main:
    def __init__(self):
        self.snake = Snake()
        self.snack = Snack()
        self.wall = Wall()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.grass()
        self.wall.draw_wall()
        self.snack.draw_snack()
        self.snake.draw_snake()
        self.score()


    def check_collision(self):
        if self.snack.pos == self.snake.body[0]:
            self.snack.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.snack.pos:
                self.snack.randomize()


    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_num or not 0 <= self.snake.body[0].y < cell_num :
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(slef):
        sys.exit()



    def grass(self):
        for row in range(cell_num):
            if row % 2 == 0:
                for col in range(cell_num):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,(120,255,0),grass_rect)
            else:
                for col in range(cell_num):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(row*cell_size,col * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,(120,255,0),grass_rect)


    def score(self):
        text = 'Your Score: '+str(len(self.snake.body)-3)
        surface = font_small.render(text,True,(WHITE))
        score_x = int(cell_size*cell_num-100)
        score_y = int(cell_size*cell_num-40)
        score_rect = surface.get_rect(center = (score_x,score_y))
        screen.blit(surface,score_rect)


pygame.init()

cell_size = 30
cell_num = 20

SIZE = (WIDTH, HEIGHT) = (600,600)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GREEN = (51,255,51)
YELLOW = (255,255,0)
BLUE = (102,178,255)
TEXT = (106,125,199)

screen = pygame.display.set_mode((SIZE))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()
image = pygame.image.load('C:\\Users\\user\\Desktop\\snake\\image\\grusha.png')
grusha = pygame.transform.scale(image,(20,30))
font = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)
#wall = pygame.image.load("C:\pythonn\TSIS9\wall.png")
      #Шрифты для записи




main = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

def game(speed = 1):
 while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == SCREEN_UPDATE:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main.snake.direction = Vector2(0,-(speed))
            if event.key == pygame.K_DOWN:
                main.snake.direction = Vector2(0,(speed))
            if event.key == pygame.K_RIGHT:
                main.snake.direction = Vector2((speed),0)
            if event.key == pygame.K_LEFT:
                main.snake.direction = Vector2(-(speed),0)
        
    screen.fill(GREEN)
    main.draw_elements()
    pygame.display.update()

def choosing():
    menu_background = pygame.image.load("C:\\Users\\user\\Desktop\\snake\\image\\menu.png")
    easy_text = font.render('1 - easy', True,(TEXT))
    medium_text = font.render("2 - medium",True,TEXT)
    hard_text = font.render("3 - hard",True,TEXT)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game(speed = 1)

                if event.key == pygame.K_2:
                    game(speed = 2)

                if event.key == pygame.K_3:
                    game(speed = 5)

        screen.blit(menu_background,(0,0))
        screen.blit(easy_text,(150,220))
        screen.blit(medium_text,(150,270))
        screen.blit(hard_text,(150,320))
        pygame.display.update()


def menu():
    menu_background = pygame.image.load("C:\\Users\\user\\Desktop\\snake\\image\\menu.png")
    play_text = font.render('press F to start', True,(TEXT))
    quit_text = font.render("press Q to quit",True,TEXT)
    save_text = font.render("press S to save",True,TEXT)

    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    choosing()
                    #game()
                if event.key == pygame.K_q:
                    sys.exit()

        screen.blit(menu_background,(0,0))
        screen.blit(play_text,(150,220))
        screen.blit(save_text,(150,270))
        screen.blit(quit_text,(150,320))
        pygame.display.update()

menu()