class Snake():
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.add_block = False
        self.open_head = "no"
        
        #head_closed
        self.snake_head_up = pygame.image.load("Graphics/head_up.png").convert_alpha()
        self.snake_head_down = pygame.image.load("Graphics/head_down.png").convert_alpha()
        self.snake_head_left = pygame.image.load("Graphics/head_left.png").convert_alpha()
        self.snake_head_right = pygame.image.load("Graphics/head_right.png").convert_alpha()
        #head_opened
        self.snake_head_open_up = pygame.transform.scale(pygame.image.load("Graphics/head_open_up.png").convert_alpha(),(39,35))
        self.snake_head_open_down = pygame.transform.scale(pygame.image.load("Graphics/head_open_down.png").convert_alpha(),(39,35))
        self.snake_head_open_left = pygame.transform.scale(pygame.image.load("Graphics/head_open_left.png").convert_alpha(),(35,39))
        self.snake_head_open_right = pygame.transform.scale(pygame.image.load("Graphics/head_open_right.png").convert_alpha(),(35,39))
        #tail
        self.snake_tail_up = pygame.image.load("Graphics/tail_up.png").convert_alpha()
        self.snake_tail_down = pygame.image.load("Graphics/tail_down.png").convert_alpha()
        self.snake_tail_left = pygame.image.load("Graphics/tail_left.png").convert_alpha()
        self.snake_tail_right = pygame.image.load("Graphics/tail_right.png").convert_alpha()
        #body
        self.snake_body_vertical = pygame.image.load("Graphics/body_vertical.png").convert_alpha()
        self.snake_body_horizontal = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()
        
        self.snake_body_tl = pygame.image.load("Graphics/body_tl.png").convert_alpha()
        self.snake_body_tr = pygame.image.load("Graphics/body_tr.png").convert_alpha()
        self.snake_body_bl = pygame.image.load("Graphics/body_bl.png").convert_alpha()
        self.snake_body_br = pygame.image.load("Graphics/body_br.png").convert_alpha()
        
        self.direction_changed = False
        
        
    def draw_snake(self):
        for block in self.body:
            index = self.body.index(block)
            if index == 0:
                snake_head_rect = snake.snake_draw_head().get_rect(topleft = (self.body[0].x*shell_size-3,self.body[0].y*shell_size-3))
                screen.blit(snake.snake_draw_head(),snake_head_rect)
            elif index == len(self.body) -1:
                snake_tail_rect = snake.snake_draw_tail().get_rect(topleft = (self.body[-1].x*shell_size-3,self.body[-1].y*shell_size-3))
                screen.blit(snake.snake_draw_tail(),snake_tail_rect)
            else:
                snake_body = self.snake_body_horizontal
                snake_body_rect = snake_body.get_rect(topleft = (block.x*shell_size-3,block.y*shell_size-3))
                previous_block = self.body[index+1] - block
                next_block = self.body[index-1] - block
                if previous_block.x == next_block.x:
                    snake_body = self.snake_body_vertical
                elif previous_block.y == next_block.y:
                    snake_body = self.snake_body_horizontal
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        snake_body = self.snake_body_tl
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        snake_body = self.snake_body_bl
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        snake_body = self.snake_body_tr
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        snake_body = self.snake_body_br
                screen.blit(snake_body, snake_body_rect)
    def movement_snake(self): 
        
        if self.direction == Vector2(0,0):
            pass
        else:
            if self.add_block == True:
                body_copy = self.body[:]
                body_copy.insert(0,body_copy[0]+self.direction)
                self.body = body_copy[:]
                self.add_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0]+self.direction)
                self.body = body_copy[:]
        self.direction_changed = False
    def snake_collision(self):
        if self.body[0] == fruit.pos:
            self.add_block = True
            crunch.play()
            fruit.randomize()
    def check_fail(self):
        if 0> self.body[0].x or self.body[0].x > shell_number -1:
            snake.game_over()
            
        elif 0> self.body[0].y or self.body[0].y > shell_number - 1:
            snake.game_over()
        for block in self.body[1:]:
            if self.body[0] == block:
                snake.game_over()
    def snake_draw_head(self):
        snake_head = self.snake_head_right
        # if self.direction == Vector2(0,-1):
        #     snake_head = self.snake_head_up  
        # elif self.direction == Vector2(0,1):
        #     snake_head = self.snake_head_down 
        # elif self.direction == Vector2(-1,0):
        #     snake_head = self.snake_head_left
        # elif self.direction == Vector2(1,0):
        #     snake_head = self.snake_head_right
        for head in fruit.surrounding_blocks():
            if self.body[0] == head:
                self.open_head = "yes"
        head_relation = self.body[1] - self.body[0]
        if self.open_head == "no":
            if head_relation == Vector2(1,0):
                snake_head = self.snake_head_left
            elif head_relation == Vector2(-1,0): 
                snake_head = self.snake_head_right
            elif head_relation == Vector2(0,1):
                snake_head = self.snake_head_up 
            elif head_relation == Vector2(0,-1): 
                snake_head = self.snake_head_down
        else:
            if head_relation == Vector2(1,0):
                snake_head = self.snake_head_open_left
            elif head_relation == Vector2(-1,0): 
                snake_head = self.snake_head_open_right
            elif head_relation == Vector2(0,1):
                snake_head = self.snake_head_open_up 
            elif head_relation == Vector2(0,-1): 
                snake_head = self.snake_head_open_down
            self.open_head = "no"
        return snake_head
    def snake_draw_tail(self):
        snake_tail = self.snake_tail_left
        if self.body[-2] - self.body[-1] == Vector2(0,1):
            snake_tail = self.snake_tail_up  
        elif self.body[-2] - self.body[-1] == Vector2(0,-1):
            snake_tail = self.snake_tail_down 
        elif self.body[-2] - self.body[-1] == Vector2(1,0):
            snake_tail = self.snake_tail_left
        elif self.body[-2] - self.body[-1] == Vector2(-1,0):
            snake_tail = self.snake_tail_right
        return snake_tail 

            
    def update_movement(self, new_direction):
        # Only allow a direction change if the snake hasn't already changed direction in this frame
        if not self.direction_changed:
            # Check if the new direction is not the opposite of the current direction
            if (new_direction == Vector2(1, 0) and self.direction != Vector2(-1, 0)) or \
               (new_direction == Vector2(-1, 0) and self.direction != Vector2(1, 0)) or \
               (new_direction == Vector2(0, 1) and self.direction != Vector2(0, -1)) or \
               (new_direction == Vector2(0, -1) and self.direction != Vector2(0, 1)):
                # Update the direction and set flag to true
                self.direction = new_direction
                self.direction_changed = True        
    def update_snake(self):
        snake.draw_snake()
        snake.snake_collision()
        snake.check_fail()
        #snake.keys()
        
    def game_over(self):
        global maingame
        maingame = None
        self.direction == Vector2(0,0)
    # def keys(self):
    #     if maingame:
    #         keys = pygame.key.get_pressed()
    #         if keys[pygame.K_w] :
    #             if keys[pygame.K_a]:
    #                 pass
    #             elif keys[pygame.K_s]:
    #                 pass
    #             elif keys[pygame.K_d]:
    #                 pass
    #             else:
    #                 snake.direction = Vector2(0,-1)
    #         elif keys[pygame.K_a]:
    #             if keys[pygame.K_w]:
    #                 pass
    #             elif keys[pygame.K_s]:
    #                 pass
    #             elif keys[pygame.K_d]:
    #                 pass
    #             else:
    #                 snake.direction = Vector2(-1,0)
    #         elif keys[pygame.K_s]:
    #             if keys[pygame.K_a]:
    #                 pass
    #             elif keys[pygame.K_w]:
    #                 pass
    #             elif keys[pygame.K_d]:
    #                 pass
    #             else:
    #                 snake.direction = Vector2(0,1)
    #         elif keys[pygame.K_d]:
    #             if keys[pygame.K_a]:
    #                 pass
    #             elif keys[pygame.K_s]:
    #                 pass
    #             elif keys[pygame.K_d]:
    #                 pass
    #             else:
    #                 snake.direction = Vector2(1,0)


class Fruit():
    def __init__(self):
        self.randomize()
        self.image = pygame.image.load("Graphics/apple.png").convert_alpha()
    def draw_fruit(self):
        for body in snake.body[1:]:
            if self.pos == body:
                self.randomize()
        fruit_rect = self.image.get_rect(topleft = (self.pos.x*shell_size-3,self.pos.y*shell_size-3))
        screen.blit(self.image,fruit_rect)
    def randomize(self):
        self.x = randint(0,shell_number-1)
        self.y = randint(0,shell_number-1)
        self.pos = Vector2(self.x,self.y)
    def update_fruit(self):
        fruit.draw_fruit()
        
    def surrounding_blocks(self):
        block_right = Vector2(self.x+1,self.y)
        block_left = Vector2(self.x-1,self.y)
        block_up = Vector2(self.x,self.y-1)
        block_down = Vector2(self.x,self.y+1)
        block_topright = Vector2(self.x+1,self.y-1)
        block_topleft = Vector2(self.x-1,self.y-1)
        block_bottomright = Vector2(self.x+1,self.y+1)
        block_bottomleft = Vector2(self.x-1,self.y+1)
        radius = [block_right,block_left,block_up,block_down,block_topright,block_topleft,block_bottomright,block_bottomleft]
        return radius
    def score_text(self):
        score = str(len(snake.body) -3)
        score_font = pygame.font.Font("Font/Game_text.ttf",25)
        score_text =  score_font.render(score,True,"black")
        score_text_rect = score_text.get_rect(center = (60,40))
        image_rect =  self.image.get_rect(center = (30,40))
        screen.blit(score_text,score_text_rect)
        screen.blit(self.image,image_rect)
    

class Screens():
    
    def startscreen(self):
        title_the_font = pygame.font.Font("Font/Game_text.ttf",35)
        title_snake_font = pygame.font.Font("Font/Game_text.ttf",200)
        title_space_font = pygame.font.Font("Font/Game_text.ttf",35)
        screen.fill((139, 222, 62))  
        the_text = title_the_font.render("The",True,(31, 79, 17))
        the_text_rect =the_text.get_rect(center = (100,120))
        snake_text = title_snake_font.render("Snake",True,(21, 74, 5))
        snake__text_rect = snake_text.get_rect(center = (350,200))
        snake_whole_body = pygame.transform.scale(pygame.image.load("Graphics/snake_whole_body.png").convert_alpha(),(450,130))
        snake_whole_body_rect = snake_whole_body.get_rect(center = (225,370))
        space_text = title_space_font.render("Press Space To Start!",True,(73, 120, 59))
        space_text_rect =space_text.get_rect(center = (350,500))
        screen.blit( the_text,the_text_rect)
        screen.blit(snake_text,snake__text_rect)
        screen.blit(snake_whole_body,snake_whole_body_rect)
        screen.blit(space_text,space_text_rect)
    def mainscreen(self):
        for row in range(shell_number):
            if row%2 == 0 :
                for col in range(shell_number):
                    if col %2 == 0:
                        grass_rect = pygame.Rect(col*shell_size,row*shell_size,shell_size,shell_size)
                        pygame.draw.rect(screen,(180, 227, 128),grass_rect)
            else:
                for col in range(shell_number):
                    if col %2 != 0:
                        grass_rect = pygame.Rect(col*shell_size,row*shell_size,shell_size,shell_size)
                        pygame.draw.rect(screen,(180, 227, 128),grass_rect)
        
                # screen.fill((246, 233, 107),rect)  
    def endscreen(self):
        screen.fill((180, 227, 128))  
        head = pygame.transform.scale(pygame.image.load("Graphics/head_open_down.png").convert_alpha(),(100,100))
        body = pygame.transform.scale(pygame.image.load("Graphics/body_vertical.png").convert_alpha(),(100,100))
        head_rect = head.get_rect(midtop = (350,100))
        body_rect = body.get_rect(midtop = (350,0))
        
        apple_scale = pygame.transform.scale(fruit.image,(90,90))
        apple_scale_rect = apple_scale.get_rect(center  = (305,310))
        score = str(len(snake.body) -3)
        
        score_font = pygame.font.Font("Font/Game_text.ttf",70)
        score_text =  score_font.render(score,True,"black")
        score_text_rect = score_text.get_rect(center = (385,310))
        
        layer.retry_text()
        layer.exit_text()
        
        screen.blit(head,head_rect)
        screen.blit(body,body_rect)
        screen.blit(apple_scale,apple_scale_rect)
        screen.blit(score_text,score_text_rect)
    def retry_text(self):
        end_screen_font =  pygame.font.Font("Font/Game_text.ttf",50)
        retry__text = end_screen_font.render("Retry",True,"black",(56, 127, 57))
        self.retry_text_rect = retry__text.get_rect(center = (260,450))
        self.mouse_pos = pygame.mouse.get_pos()
        if self.retry_text_rect.collidepoint(self.mouse_pos):
            retry__text = end_screen_font.render("Retry",True,"black",(246, 251, 122))
        screen.blit(retry__text,self.retry_text_rect)
    def exit_text(self):
        end_screen_font =  pygame.font.Font("Font/Game_text.ttf",50)
        exit_text = end_screen_font.render("Exit",True,"black",(56, 127, 57))
        self.exit_text_rect = exit_text.get_rect(center = (430,450))
        self.mouse_pos = pygame.mouse.get_pos()
        if self.exit_text_rect.collidepoint(self.mouse_pos):
            exit_text = end_screen_font.render("Exit",True,"black",(246, 251, 122))
        screen.blit(exit_text,self.exit_text_rect)
    def restart(self):
        global maingame
        snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        snake.direction = Vector2(0,0)
        snake.add_block = False
        fruit.randomize()
        maingame = True
        screen.fill((139, 222, 62)) 
    
import pygame,sys,os
from pygame.math import Vector2
os.chdir(os.path.dirname(sys.argv[0]))
from random import randint
pygame.init()
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(pygame.image.load("Graphics/icon.ico"))

shell_size = 35
shell_number = 20
screen = pygame.display.set_mode((shell_size*shell_number,shell_size*shell_number))
clock = pygame.time.Clock()
time = 150
maingame = False

fruit = Fruit()
snake = Snake()
layer = Screens()

#sounds
bg_music = pygame.mixer.Sound("Sound/BG_music.mp3")
crunch = pygame.mixer.Sound("Sound/crunch.wav")
movement = pygame.mixer.Sound("Sound/movement.wav")
transition = pygame.mixer.Sound("Sound/transition.wav")

bg_music.set_volume(0.5)
movement.set_volume(0.3)
bg_music.play(-1)
#timers
update_timer = pygame.USEREVENT + 1
pygame.time.set_timer(update_timer,time)
difficulty_timer = pygame.USEREVENT + 2
pygame.time.set_timer(difficulty_timer,10000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if maingame == False :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    transition.play()
                    maingame = True
        if maingame:
            if event.type == update_timer:
                snake.movement_snake()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if snake.direction != Vector2(0,1):
                        snake.update_movement(Vector2(0,-1))
                        movement.play()
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if snake.direction != Vector2(0,-1):
                        snake.update_movement(Vector2(0,1))
                        
                        movement.play()
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if snake.direction != Vector2(1,0):  
                        snake.update_movement(Vector2(-1,0))
                        
                        movement.play()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if snake.direction != Vector2(-1,0):
                        snake.update_movement(Vector2(1,0))
                        
                        movement.play()
        if maingame == None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if layer.retry_text_rect.collidepoint(layer.mouse_pos):
                    transition.play()
                    layer.restart()
                    
                if layer.exit_text_rect.collidepoint(layer.mouse_pos):
                    pygame.quit()
                    sys.exit()
    if maingame:
        screen.fill((136, 214, 108))
        layer.mainscreen()
        fruit.update_fruit()  
        snake.update_snake()
        fruit.score_text()
    elif maingame == False:
        layer.startscreen()
    else:
        layer.endscreen()
    pygame.display.update()
    clock.tick(60)