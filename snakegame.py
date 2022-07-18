# This is a snake game which is just like other snake game it will be improved more in the future.

# So thank you for reading this comment


import random
import pygame

# defining the hight score over here

hightscore = 100

pygame.init() # initializing the pygame module

# defining the variables here which are constant they will never change

window_width = 1000
window_height = 700
fps = 60 # frames per second


# defining the colors over here
white = (255, 255, 255)


# creating the display here
display = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake bite")
icon = pygame.image.load("img/game.jpg")
# pygame.display.set_icon(icon)
pygame.display.set_icon(icon)

# creating the fps over here

clock = pygame.time.Clock();

# creating the gameloop function here

# def homescreen():
    

def gameloop():

    # defining the variable here that need to be set as the game will be restart.

    exit_game = False
    game_over = False
    score = 0
    snake_x = window_width/2-200
    snake_y = window_height/2-200
    size = 20
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(15,window_width-15)
    food_y = random.randint(5,window_height-15)

    snk_list = []
    snk_length = 1

    while not exit_game:

        # creating all the game events here.

        if game_over:
            display.fill("white")
            displaytext(display,"Score :- ","black",score,100,window_width/2-160,window_height/4)
            if score>hightscore:
                displaytext(display,"congratulations High score:- ","black",score,60,window_width/2-250,window_height/2)
            
            # updating the display
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("hey you have pressed the enter")
                        gameloop()

        if not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x=-5
                        velocity_y=0

                    if event.key == pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        velocity_x=0
                        velocity_y=-5

                    if event.key == pygame.K_DOWN:
                        velocity_x=0
                        velocity_y=5
                
            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score+=1
                food_x = random.randint(5,window_width-5)
                food_y = random.randint(5,window_height-5)
                snk_length+=4
                
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
                
            snake_x+=velocity_x
            snake_y+=velocity_y

            # checking whether the game is over or not

            game_over=checkthecollision(snake_x,snake_y,snk_list)

            display.fill(white) # filling the canvas with a white color
            plotsnake(display,snk_list,size,"black")
            pygame.draw.rect(display,"red",[food_x,food_y,size,size])
            displaytext(display,"Score:- ","black",score,50,10,10)
            pygame.display.update() # updating the display


            clock.tick(fps) # setting fps of the game here

    # if the game exits it will exit the game and break the code
    pygame.quit()


# defining all the funcitions over here

def displaytext(display,text,color,score,size,x,y):

     font = pygame.font.SysFont(None,size);
     screen_text = font.render(text+str(score),True,color)
     display.blit(screen_text,[x,y])

def plotsnake(display,snk_list,size,color):
    for x,y in snk_list:
        pygame.draw.rect(display,color,[x,y,size,size])

def checkthecollision(snake_x,snake_y,snk_list):

    over = False

    head_x = snk_list[0][0]
    head_y = snk_list[0][1]

    if snake_x<0 or snake_x>window_width or snake_y<0 or snake_y>window_height:
        print("game over")
        return True    

    for i in range(len(snk_list)):
        if i == 0:
            pass
        else:
            if snk_list[i][0]==head_x and snk_list[i][1]==head_y:
                over = True
                break
            else:
                over = False
        
    return over
            

# runnig the gameloop
gameloop()







