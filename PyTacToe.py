#!/usr/bin/python -tt

import random

def displayInstructions():
  print '\n\n--------'
  print 'PyTacToe'
  print '--------\n\n'
  print 'Enter your move using the following board positions.\n\n'
  print ' 1 | 2 | 3'
  print '-----------'
  print ' 4 | 5 | 6'
  print '-----------'
  print ' 7 | 8 | 9\n\n'

def displayBoard(board):
  print '\n\n'
  print ' ' + board[0] + ' | ' + board[1] + ' | ' + board[2]
  print '-----------'
  print ' ' + board[3] + ' | ' + board[4] + ' | ' + board[5]
  print '-----------'
  print ' ' + board[6] + ' | ' + board[7] + ' | ' + board[8]
  print '\n\n'

def isValidMove(board, space):
  valid = 1
  if (board[space] == ' '):
    valid = 0
  return valid

def isBoardFull(board):
  full = False
  boardcount = 0
  for i in range(0, 9):
    boardcount = boardcount + isValidMove(board, i)
  if (boardcount == 9):
    full = True
  return full

def isWinner(board, letter):
  return ((board[6] == letter and board[7] == letter and board[8] == letter) or
  (board[3] == letter and board[4] == letter and board[5] == letter) or
  (board[0] == letter and board[1] == letter and board[2] == letter) or
  (board[6] == letter and board[3] == letter and board[0] == letter) or
  (board[7] == letter and board[4] == letter and board[1] == letter) or
  (board[8] == letter and board[5] == letter and board[2] == letter) or
  (board[6] == letter and board[4] == letter and board[2] == letter) or
  (board[8] == letter and board[4] == letter and board[0] == letter))

def commitPlay(board, letter, move):
    board[move] = letter

def getComputerRandomInt():
  return (random.randrange(1, 10, 1)) - 1

def getUserInt():
  print 'Enter a move (1-9): '
  move = raw_input()
  while not (move == '1' or move == '2' or move == '3' or move == '4' or move == '5' or move == '6' or move == '7' or move == '8' or move == '9'):
    print 'Invalid move\nEnter a move (1-9)'
    move = raw_input()
  return int(move) - 1

def firstMove():
  if random.randint(0, 1) == 0:
    print '\nThe Computer Goes First'
    return 'Computer'
  else:
    print '\nYou Go First'
    return 'Human'

def scoreboard(comp, hum, ties, message):
  print '\n\n----------------------'
  print message
  print '----------------------'
  print ' Computer:  ' + str(comp) + ' Win(s)'
  print ' Human:     ' + str(hum) + ' Win(s)'
  print ' Tie Games: ' + str(ties)
  print '----------------------'
  return

def main():
  displayInstructions()
  play=True
  humanWins = 0
  computerWins = 0
  tieGames = 0
  while (play==True):

    grid_list = [' ', ' ', ' ' ,' ' ,' ' ,' ' ,' ' ,' ', ' ']
    endOfGame = False
    turn = firstMove()

    while (endOfGame == False):
      while (turn == 'Human' and endOfGame == False):
        displayBoard(grid_list)
        move = getUserInt()
        if (isValidMove(grid_list, move) == 0):
          commitPlay(grid_list, 'X', move)
          turn = 'Computer'
        else:
          print 'That position has already been played.'
        if (isWinner(grid_list, 'X') == True):
          humanWins = humanWins + 1
          scoreboard(computerWins, humanWins, tieGames, 'You Win!!!!')
          endOfGame = True
        else:
          if (isBoardFull(grid_list) == True):
            tieGames = tieGames + 1
            scoreboard(computerWins, humanWins, tieGames, 'Tie Game.')
            endOfGame = True

      while (turn == 'Computer' and endOfGame == False):
        move = getComputerRandomInt()
        if (isValidMove(grid_list, move) == 0):
          commitPlay(grid_list, 'O', move)
          turn = 'Human'
        if (isWinner(grid_list, 'O') == True):
          computerWins = computerWins + 1
          scoreboard(computerWins, humanWins, tieGames, 'The Computer Won.')
          endOfGame = True
        else:
          if (isBoardFull(grid_list) == True):
            tieGames = tieGames + 1
            scoreboard(computerWins, humanWins, tieGames, 'Tie Game!')
            endOfGame = True

    displayBoard(grid_list)
    print 'Play Again? (Y, N): '
    again = raw_input()
    if (again.lower().startswith('y')):
      play=True
    else:
      play=False

if __name__ == '__main__':
  main()
