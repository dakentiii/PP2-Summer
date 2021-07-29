import pygame
import random
 # Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 128)
 
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
      #цвет блока и положение
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  #\\прямоугольники
       # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        #рандомные блоки
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        #обновление действии
        # перемещение блока вниз
        self.rect.y += 1
        # сбрасывание позиции и перекидка вверх
        if self.rect.y > 410:
            self.reset_pos()
 
 
class Player(Block):
   def update(self):
        # позиция мыши
        pos = pygame.mouse.get_pos()
        #извлечение х и у для начальной позиции
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
# Initialize Pygame
pygame.init()
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Hungry Lion")

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    #first random red blocks
    block1 = Block(RED, 20, 15)
 
    # random location for the block
    block1.rect.x = random.randrange(screen_width)
    block1.rect.y = random.randrange(screen_height)
    # Добавить блок в список объектов
    block_list.add(block1)
    all_sprites_list.add(block1)
    #second random green blocks
    block2 = Block(GREEN, 20, 15)
 
    #random location for the block
    block2.rect.x = random.randrange(screen_width)
    block2.rect.y = random.randrange(screen_height)
    # Добавить блок в список объектов
    block_list.add(block2)
    all_sprites_list.add(block2)
 
#a red player block
player = Player(BLUE, 20, 15)
all_sprites_list.add(player)
 
#Цикл, пока пользователь не нажмет кнопку закрытия(X)
done = False
#шрифт очков в углу
font = pygame.font.Font(None, 36)
 # скорость обновления экрана
clock = pygame.time.Clock()
score = 0
 
# Основной цикл кода
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # ощищение экрана от блоков
    screen.fill(WHITE)
    all_sprites_list.update()
 
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
  
    # список столкновений (очков)
    for block1 in blocks_hit_list:
        score += 1
        print(score)
        # переспам блоков
        block1.reset_pos()

    all_sprites_list.draw(screen)
    text = font.render("Score: "+str(score), True, BLACK)
    screen.blit(text, [10, 10])
    # только 20 кадров в секунду
    clock.tick(20)
    # повторное обновление 
    pygame.display.flip()
 
pygame.quit()