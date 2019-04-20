### bfd soondays day 12 2018.04.08 ###
### Section 9: Project - Lecture 61 (https://www.udemy.com/the-python-bible) ###

                      ### Project 8: Tic Tac Toe ###

board = [' ' for i in range(9)]

def board_func():
  row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
  row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
  row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

  print ('')
  print (row1)
  print (row2)
  print (row3)
  print ('')

def p_move (p_value):
    if p_value == 'x':
        number = 1
    elif p_value == 'o':
        number = 2

    print ('Your turn Player {}!'.format(number))
    choice = int(input('Choose a position (1-9): '))

    while board[choice - 1] == 'x' or board[choice - 1] == 'o':
        print ('\nSpace is taken.')
        board_func()
        print ('Your turn Player {}!'.format(number))
        choice = int(input('Choose a position (1-9): '))

    if board[choice - 1] == ' ':
        board[choice - 1] = '{}'.format(p_value)


def is_win (p_value):
    if(board[0] == p_value and board[1] == p_value and board[2] == p_value) or \
      (board[3] == p_value and board[4] == p_value and board[5] == p_value) or \
      (board[6] == p_value and board[7] == p_value and board[8] == p_value) or \
      (board[0] == p_value and board[3] == p_value and board[6] == p_value) or \
      (board[0] == p_value and board[4] == p_value and board[8] == p_value) or \
      (board[2] == p_value and board[4] == p_value and board[6] == p_value):
      ## ' \ ' allows you to continue statement on next line
        return True
    else:
        return False

def is_draw():
  if ' ' not in board:
    return True
  else:
    return False


while True:
  board_func()
  p_move('x')
  board_func()
  if is_win('x'):
    print ('Winner, winner chicken dinner! \nPlayer 1 wins!')
    break
  elif is_draw():
    print ('Draw!!')
    break
  p_move('o')
  if is_win('o'):
    board_func()
    print ('Winner, winner chicken dinner! \nPlayer 2 wins!')
    break

