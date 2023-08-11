#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def the_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[2]:


test_board=['#','X','O','X','O','X','O','X','O','X']
the_board(test_board)


# In[3]:


def player_input():
    marker =''
    while not(marker =='X' and marker =='O'):
        marker = input('Player 1 Which do you want to be? X or O?  ').upper()
        
        if marker == 'X':
            return('X','O')
        else:
            return('O','X')
    


# In[4]:


player1_marker , player2_marker = player_input()


# In[5]:


player2_marker


# In[6]:


def place_marker(board,marker,position):
       
        board[position]=marker
      

    


# In[7]:


place_marker(test_board,'$',8)
the_board(test_board)


# In[8]:


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    


# In[9]:


the_board(test_board)
win_check(test_board,'X')


# In[10]:


import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[11]:


def space_check(board,position):
    return board[position]==' '


# In[12]:


def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    


# In[13]:


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position 1 - 9'))
        return position


# In[14]:


def replay():
    input('Play again? YES or NO')
    return choice =='Yes'


# In[ ]:


#While loop to keep running the game
print('WELCOME TO TIC TAC TOE')
while True:
    #play the game
    #Set everything up(board,whose first,markers)
    boardd = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first.')
    play_game = input('Ready to play? Y or N')
    if play_game == 'Y':
        game_on =True
    else:
        game_on = False
            
    #Gameplay()
    while game_on:
        if turn =='Player 1':
            the_board(boardd)
            #Choose position
            position = player_choice(boardd)
            
            
            #Place marker on position
            place_marker(boardd,player1_marker,position)
            
            #Check winner
            if win_check(boardd,player1_marker):
                the_board(boardd)
                print('Player 1 has won.')
                game_on =False
            else:
                if full_board(boardd):
                    the_board(boardd)
                    print('Tie game!')
                    game_on =False
                else:
                    turn ='Player 2'
          
            
    
  
        else:
            
            the_board(boardd)
            #Choose position
            position = player_choice(boardd)
            
            
            #Place marker on position
            place_marker(boardd,player2_marker,position)
            
            #Check winner
            if win_check(boardd,player2_marker):
                the_board(boardd)
                print('Player 2 has won.')
                game_on =False
            else:
                if full_board(boardd):
                    the_board(boardd)
                    print('Tie game!')
                    game_on =False
                else:
                    turn ='Player 1'
          
    
    #Player 2 turn
    if not replay():
        break
#Break out of the while loop on the replay function


# In[ ]:





# In[ ]:




