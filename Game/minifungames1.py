#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 16:36:49 2022

@author: samyashah21
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:56:02 2022

@author: samyashah21
"""


def games1():
    import pygame
    import random
    import os

    #Initialization
    pygame.mixer.init()
    pygame.init()


    #Colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    snakegreen = (35, 45, 40)

    #Game Backgrounds
    bg1 = pygame.image.load("bg.jpg")
    bg2 = pygame.image.load("bg2new.png")
    intro = pygame.image.load("intronew.jpg")
    outro = pygame.image.load("outronew1.png")

    #Creating The window
    screen_width = 900
    screen_height = 600
    gameWindow = pygame.display.set_mode((screen_width, screen_height))

    #Game Title
    pygame.display.set_caption("Snake Game")
    pygame.display.update()

    #Variables For The Game
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Harrington', 35)

    def text_screen(text, color, x, y):
       screen_text = font.render(text, True, color)
       gameWindow.blit(screen_text, [x,y])

    def plot_snake(gameWindow, color, snk_list, snake_size):
       for x,y in snk_list:
           pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


    #Welcome Screen

    def welcome():
        exit_game = False
        while not exit_game:
            gameWindow.blit(intro, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
            pygame.display.update()
            clock.tick(60)

    # Game Loop
    def gameloop():

    # Game specific variables
       exit_game = False
       game_over = False
       snake_x = 45
       snake_y = 55
       velocity_x = 0
       velocity_y = 0
       snk_list = []
       snk_length = 1

    #Highscore Build
       if(not os.path.exists("highscore.txt")):
           with open("highscore.txt", "w") as f:
               f.write("0")
       with open("highscore.txt", "r") as f:
                highscore = f.read()

    #Food
       food_x = random.randint(20, screen_width / 2)
       food_y = random.randint(20, screen_height / 2)

    #Game Variables
       score = 0
       init_velocity = 5
       snake_size = 30
       fps = 60
       while not exit_game:
           if game_over:
               with open("highscore.txt", "w") as f:
                   f.write(str(highscore))

    #GameOverScreen

               gameWindow.blit(outro, (0, 0))
               text_screen("Score: " + str(score ), white, 365, 300)
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       exit_game = True
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_RETURN:
                           welcome()
           else:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       exit_game = True
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_RIGHT:
                           velocity_x = init_velocity
                           velocity_y = 0
                       if event.key == pygame.K_LEFT:
                           velocity_x = - init_velocity
                           velocity_y = 0
                       if event.key == pygame.K_UP:
                           velocity_y = - init_velocity
                           velocity_x = 0
                       if event.key == pygame.K_DOWN:
                           velocity_y = init_velocity
                           velocity_x = 0
                       if event.key == pygame.K_q:
                            score +=10
               snake_x = snake_x + velocity_x
               snake_y = snake_y + velocity_y
               if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                   score +=10
                   food_x = random.randint(20, screen_width / 2)
                   food_y = random.randint(20, screen_height / 2)
                   snk_length +=5
                   if score>int(highscore):
                       highscore = score
               gameWindow.blit(bg2, (0, 0))
               text_screen("Score: " + str(score) + "  Highscore: "+str(highscore),  snakegreen, 5, 5)
               pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
               head = []
               head.append(snake_x)
               head.append(snake_y)
               snk_list.append(head)


               if len(snk_list)>snk_length:
                   del snk_list[0]
               if head in snk_list[:-1]:
                   game_over = True
               if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                   game_over = True
               plot_snake(gameWindow, black, snk_list, snake_size)
           pygame.display.update()
           clock.tick(fps)
       
       pygame.quit()
       quit()
       
    welcome()
def games2():
    import rpsMain


def games():
    class Tictactoe():   
        ''' 
        This is simple TicTacToe game
        '''

        def __init__(self):
            '''
            to save the position value,
            made a dicitonary with position as keys and O/X as values
            '''
            self.positions = {"t1" : " ",
                            "t2" : " ",
                            "t3" : " ",
                            "m1" : " ",
                            "m2" : " ",
                            "m3" : " ",
                            "b1" : " ",
                            "b2" : " ",
                            "b3" : " "} 
            
            '''
            for find winner set initial position_value all 0 
            '''                      
            self.positions_value = {"t1" : 0,
                            "t2" : 0,
                            "t3" : 0,
                            "m1" : 0,
                            "m2" : 0,
                            "m3" : 0,
                            "b1" : 0,
                            "b2" : 0,
                            "b3" : 0}  
        
        def basic(self):
            """
            basic grid of tictactoe game
            """ 
            self.status = self.positions.values()   
            print("\t %s | %s | %s \n\t---+---+---\n\t %s | %s | %s \n\t---+---+---\n\t %s | %s | %s "  
        % tuple(self.status))
        
        def ready(self):
            '''
            ready for game with game position info
            '''
            print("**** Welcome to TICTACTOE Game! ****")
            self.status = ("T1", "T2", "T3", "M1", "M2", "M3", "B1", "B2", "B3")
            print("\t%s |%s |%s \n\t---+---+---\n\t%s |%s |%s \n\t---+---+---\n\t%s |%s |%s "  
        % self.status)
            
            

        def player1(self):
            '''
            if player1 put right position(no duplicate, only accept empty position),
            position will be filled with "O" and positions_value has value 1
            '''
            while True:
                player1 = input("player1>>>>> ").lower()
                if player1 in self.positions_value.keys():
                    if self.positions[str(player1)] == " ":
                        self.positions[str(player1)]="O"
                        self.basic()
                        self.positions_value[str(player1)] = 1
                        break
                    else:
                        print("This position is filled.\nPlease put another position.")
                        continue
                else:
                    print("you put the wrong position.")    
                    continue

        def player2(self):
            '''
            if player2 put right position(no duplicate, only accept empty position),
            position will be filled with "X" and positions_value has value 4
            '''
            while True:
                player2 = input("player2>>>>> ").lower()
                if player2 in self.positions.keys():
                    if self.positions[str(player2)] == " ":
                        self.positions[str(player2)]="X"
                        self.basic()
                        self.positions_value[str(player2)] = 4
                        break
                    else:
                        print("This position is filled.\nPlease put another position.")
                        continue
                else:    
                    print("You put the wrong position.")    
                    continue

        def play(self):
            print("\nLet's start the game!")
            print("Player1 : O     Player2 : X")
            print("write a position!\n")
            for i in range(1,10):
                win = self.win()
                if 3 in win: # player1's each position has value 1
                    print("Player1 WIN!")
                    break
                elif 12 in win: # player2'x each position has value 4
                    print("Player2 WIN!")
                    break
                elif i == 9:
                    if i % 2 == 0:
                        self.player2()
                    else:
                        self.player1()
                    print("The game ended in a tie.")
                else:
                    if i % 2 == 0:
                        self.player2()
                    else:
                        self.player1()

            
        def win(self):
            self.p = list(self.positions_value.values()) # for convenience made p 
            
            # row match case
            self.r_match = [self.p[i]+self.p[i+1]+self.p[i+2] for i in [0,3,6]]

            # column match case
            self.c_match = [self.p[i]+self.p[i+3]+self.p[i+6] for i in [0,1,2]]

            # diagonal match case
            self.d_match = [self.p[0]+self.p[4]+self.p[8], self.p[2]==self.p[4]==self.p[6]]

            self.result = self.r_match + self.c_match+ self.d_match
            return self.result

    a = Tictactoe()
    while True:

        a.ready()
        answer = input("Do you wanna play? y/n >> ").lower()
        if answer == "y":    
            a.play()
        else:
            print("Bye!")
            break


def selection():
    print("Which game would you like to play :\n1) select 1 for snake game\n2) Select 2 for Stone Paper Scissor")
    s=int(input())
    if(s==1):
        games1()
    if(s==2):
        games2()
    
      
print("Select 1 for single player\nSelect 2 for multiplayer ")
m=int(input())
if(m==1):
    
    def signup():
        userID = input("Enter your user ID: ")
        duplicate = False
        try:
            f = open("savedata.txt", "r")
        except FileNotFoundError:
            f = open("savedata.txt", "x")
            f.close()
        f = open("savedata.txt", "r")
        readLines = f.readlines()
        for i in readLines:
            line = i.split()
            if line[0] == userID:
                duplicate = True
                break
            else:
                pass
        if duplicate == True:
            print("Username already exists")
        else :   
            passwd = input("Enter your password: ")
            f.close()
            f = open("savedata.txt", "a")
            f.write(f"{userID} {passwd}\n")
            f.close()
    
    def login():
        userID = input("Enter your user ID: ")
        passwd = input("Enter your password: ")
        matched = False
        
        try:
            f = open("savedata.txt", "r")
        except FileNotFoundError:
            f = open("savedata.txt", "x")
            f.close()
        f = open("savedata.txt", "r")
        
        readLines = f.readlines()
        for i in readLines:
            line = i.split()
            if line[0] == userID and line[1] == passwd:
                matched = True
                break
            else:
                pass
        if matched == True:
            print("Logged in.")
            selection()
        else:
            print("Invalid user ID or password.")
        f.close()
    
    
    print("1) Existing user login \n2) New user please signup")
    n=int(input())
    if(n==1):
        login()
    if(n==2):
        signup()
if(m==2):
    print("1) Existing user login\n2) New user please signup")
    n=int(input())
    
    def signup():
        z=-1
        userID = input("Enter your user ID: ")
        duplicate = False
        try:
            f = open("savedata.txt", "r")
        except FileNotFoundError:
            f = open("savedata.txt", "x")
            f.close()
        f = open("savedata.txt", "r")
        readLines = f.readlines()
        for i in readLines:
            line = i.split()
            if line[0] == userID:
                duplicate = True
                break
            else:
                pass
        if duplicate == True:
            print("Username already exists")
            z=0
            
        else :   
            passwd = input("Enter your password: ")
            f.close()
            f = open("savedata.txt", "a")
            f.write(f"{userID} {passwd}\n")
            f.close()
        return z
    def multilogin():
        user1ID = input("User 1 enter your user ID: ")
        passwd1= input("User 1 enter your password: ")
        user2ID = input("User 2 your user ID: ")
        passwd2= input("User 2 your password: ")
        matched1 = False
        matched2 = False
        try:
            f = open("savedata.txt", "r")
        except FileNotFoundError:
            f = open("savedata.txt", "x")
            f.close()
        f = open("savedata.txt", "r")
        readLines = f.readlines()
        for i in readLines:
            line = i.split()
            if line[0] == user1ID and line[1] == passwd1:
                matched1= True
                break
            else:
                pass
        for i in readLines:
            line = i.split()
            if line[0] == user2ID and line[1] == passwd2:
                matched2= True
                break
            else:
                pass
        if (matched1== True and matched2==True):
            print("Both users Logged in.")
            games()
        elif (matched1 == True and matched2 != True):
            print("2 user invalid username or password")
        elif (matched1 != True and matched2 == True):
            print("1 user invalid username or password")
        else:
            print("Invalid user ID or password.")
        f.close()
    def multisignup():
        print("Which user would like to sign up firsr\n1)For user 1\n2)For user 2")
        x=int(input())
        if(x==1):
            z=signup()
            if(z==0):
                print("As username is invalid please start again")
                return(-1)
            print("User 1 signed up")
            print("Second user please make your inputs")
            signup()
            if(z==0):
                print("As username is invalid please start again")
                return(-1)
            print("User 2 signed up")
        if(x==2):
            z=signup()
            if(z==0):
                print("As username is invalid please start again")
                return(-1)
            print("User 2 signed up")
            print("First user please make your inputs")
            signup()
            if(z==0):
                print("As username is invalid please start again")
                return(-1)
            print("User 2 signed up")
            print("As you have signed up please login and start playing")
    if(n==1):       
        multilogin()
    if(n==2):
        multisignup()
