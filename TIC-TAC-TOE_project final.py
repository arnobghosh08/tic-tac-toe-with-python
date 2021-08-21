# TEAM-2_CHALLENGE-2

# IMPORT

from turtle import color
import pygame, sys
import numpy as np

#INITIALIZE PYGAME
pygame.init()

#CONSTANTS

WIDTH = 800
HEIGHT= WIDTH
LINE_WIDTH= 10
BOARD_ROWS=3
BOARD_COLUMNS=3
SQUARE_SIZE=WIDTH//BOARD_COLUMNS
CIRCLE_RADIUS= WIDTH//10
CIRCLE_WIDTH=15
CROSS_WIDTH= 25

#COLORS

BG_COLOR= (28,170,156)
LINE_COLOR=(23,145,135)
CIRCLE_COLOR=(239, 231, 200)
TEXT_COLOR= (236, 42,23)
CROSS_COLOR= (66,66,66)
SPACE= SQUARE_SIZE//4

# GAME SCREEN

screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption('TIC-TAC-TOE')
screen.fill (BG_COLOR)

#CONSOLE

board = np.zeros( (BOARD_ROWS, BOARD_COLUMNS) )
print(board)

# LINES

def draw_lines():
    
    # 2 HORIZONTAL LINES
    pygame.draw.line( screen, LINE_COLOR, (0,SQUARE_SIZE), (WIDTH,SQUARE_SIZE), LINE_WIDTH )
    pygame.draw.line( screen, LINE_COLOR, (0,2*SQUARE_SIZE), (WIDTH,2*SQUARE_SIZE), LINE_WIDTH )
    # 2 VERTICAL LINES
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE,0), (SQUARE_SIZE,HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2*SQUARE_SIZE,0), (2*SQUARE_SIZE,HEIGHT), LINE_WIDTH)

# FIGURES (X AND O)

def draw_figures():
   
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            if board[row][column]== 1:
                pygame.draw.circle( screen, CIRCLE_COLOR , (int(column* SQUARE_SIZE + SQUARE_SIZE//2 ), int( row*  SQUARE_SIZE+SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][column]== 2:
                pygame.draw.line( screen, CROSS_COLOR, (column* SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE- SPACE), (column * SQUARE_SIZE + SQUARE_SIZE//2 + SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOR, (column* SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (column * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE- SPACE), CROSS_WIDTH )

# MARK SQUARES (THESE ARE USED TO MARK THE SQUARES SELECTED BY PLAYERS )
                
def mark_square(row, column, player):
    board[row][column]= player

# AVAILABLE SQUARES (USED TO CHECK IF A SQUARE IS AVAILABLE )

def available_square(row, column):
    return board[row][column]== 0


#To find out if a square is available(suppose, the middle one), type-   print( available_square(1,1) )

def board_is_full():
    # FIRST LOOP THROUGH ALL THE ROWS. SECOND LOOP THROUGH ALL THE COLUMNS
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            if board[row][column] ==0:
                return False
    return True
   
                   
                 
# CHECK WINNING CONDITIONS

def check_win (player):
    
    # VERTICAL WIN CHECK
    for column in range(BOARD_COLUMNS):
        if board[0][column]==player and board[1][column]==player and board[2][column]==player:
            draw_vertical_winning_line (column, player)
            return True
    # HORIZONTAL WIN CHECK
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
          draw_horizontal_winning_line(row, player)
          return True
    # ASCENDING DIAGONAL WIN CHECK
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
       draw_asc_diagonal(player)
       return True
    # DESCENDING DIAGONAL WIN CHECK
    if board[0][0]==player and board[1][1]== player and board[2][2]==player:
       draw_desc_diagonal(player)
       return True
    
    return False

# WINNING LINES

def draw_vertical_winning_line (column, player):
    posX=column * SQUARE_SIZE + SQUARE_SIZE//2
    # CO-ORDINATES OF VERTICAL WINNING LINE
    if player==1:
        color = CIRCLE_COLOR
    elif player==2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX,15), (posX, HEIGHT-15), LINE_WIDTH)

def draw_horizontal_winning_line (row, player):
    posY=row * SQUARE_SIZE + SQUARE_SIZE//2

    if player==1:
        color = CIRCLE_COLOR
    elif player==2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH-15,posY), LINE_WIDTH)

def draw_asc_diagonal(player):
    
    if player==1:
        color = CIRCLE_COLOR
    elif player==2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH-15, 15), LINE_WIDTH)

def draw_desc_diagonal(player):
    
    if player==1:
        color = CIRCLE_COLOR
    elif player==2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15,15), (WIDTH-15,HEIGHT-15), LINE_WIDTH)

# RESTART FUNCTION (TO RESTART THE GAME)    
    
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            board[row][column]=0


# QUIT FUNCTION (TO QUIT THE GAME)            
def quit():
    event.type==pygame.QUIT
    pygame.quit()
    sys.quit()

            

draw_lines()

player = 1
game_over= False

# MAIN LOOP

while True:
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
           sys.exit()
              
        
              
         
        if event.type== pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_row = int(mouseY // SQUARE_SIZE) 
            clicked_column = int(mouseX // SQUARE_SIZE)

            if available_square ( clicked_row, clicked_column ):
               
                if player==1:
                    mark_square( clicked_row, clicked_column, 1 )
                    if check_win ( player ):
                        game_over=True
                        font = pygame.font.SysFont(None, 40)
                        img = font.render('CIRCLE WON. Press q to quit and r to restart', True, TEXT_COLOR)
                        screen.blit(img, (WIDTH//6, 20))
                        
                        

                    player = 2

                            
                 # NOW, WE ARE SWITCHING TO PLAYER-2 
                
                elif player==2:
                    mark_square( clicked_row, clicked_column, 2 )     
                    if check_win( player ):
                       game_over=True
                       font = pygame.font.SysFont(None, 40)
                       img = font.render('CROSS WON. Press q to quit and r to restart', True, TEXT_COLOR)
                       screen.blit(img, (WIDTH//6, 20))
                      
                    
                    player = 1
                     # NOW, WE ARE SWITCHING BACK TO PLAYER-1. IN THIS WAY, WE CAN KEEP SWITCHING BETWEEN THE PLAYERS AFTER A MOVE.
                
                               # WHAT HAPPENS IF THE BOARD IS FULL? 3 POSSIBILITIES-
                if  board_is_full(): 
                   game_over= True
                   font=pygame.font.SysFont(None,40)
                   if check_win(1): img=font.render('CIRCLE WON. Press q to quit and r to restart', True, TEXT_COLOR)
                   elif check_win(2):img=font.render('CROSS WON. Press q to quit and r to restart', True, TEXT_COLOR)
                   else: img=font.render('DRAW. Press q to quit and r to restart', True, TEXT_COLOR)
                   screen.blit(img,(WIDTH//6,20))
                
                draw_figures()

        # ASSIGNING KEYS FOR RESTARTING AND QUITTING THE GAME         
               
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart() 
                player=1
                game_over=False

           # NOW, IF WE PRESS 'r', THE GAME WILL RESTART FROM PLAYER-1 (AS ASSIGNED) AND THE GAME IS NOT OVER; IT'S JUST BEGINNING           


            if event.key==pygame.K_q:
                quit()
        
        # NOW, IF WE PRESS 'q', WE CAN QUIT THE GAME.
        
    pygame.display.update()




               

