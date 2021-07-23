import pygame, sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

#Parameters for food
#food_pos = [0,0]
food_pos = [random.randrange(1,(frame_size_x//10))*10, random.randrange(1,(frame_size_y//10))*10]
food_spawn = False

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))



# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()




def check_for_events():
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    global change_to
    global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if change_to == 'UP' and  direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'














def update_snake():
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction
    







    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    





    # End the game if the snake collides with the wall or with itself. 
    global score
    global food_spawn
    global snake_pos
     
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
  
    if snake_pos[1]== food_pos[1] and snake_pos[0] == food_pos[0]:
        score +=1
        food_spawn = False
        

    else:
        snake_body.pop()

     #Game over
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x -10:
        game_over()
    
    if snake_pos[0] < 0 or snake_pos[1] > frame_size_y -10:
        game_over()

    #touching own body

    for piece in snake_body[1:]:
        if snake_pos[0] == piece[0] and snake_pos[1] == piece[1]:
            game_over()






def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    global food_pos
    global food_spawn
    if food_spawn==False:
         
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True
    




def show_score(pos, color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score :' +  str(score), True, color)

    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
  






def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    global food_pos
    
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    







def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    gameover_img = pygame.font.SysFont('times new roman', 54).render('YOU DIED', True, red)
    score_img = pygame.font.SysFont('times new roman', 23).render('Score :'+str(score), True, red)
    gameover_rect = gameover_img.get_rect()
    score_rect = score_img.get_rect()
    gameover_rect.midtop = (frame_size_x/2, frame_size_y/4)
    
    score_rect.midtop = (frame_size_x/2, frame_size_y*0.75)
    game_window.blit(score_img, score_rect)

    
    game_window.blit(gameover_img, gameover_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()







# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    update_snake()
    check_for_events()
    create_food()
    
    update_screen()           
                                                         



    

    # To set the speed of the screen
    fps_controller.tick(25)