import random

def display_row(col1, col2, col3, board):
  print(f"  {board[col1]}  |  {board[col2]}  |  {board[col3]}  ")

def display_hyphen(num):
  print("-" * num)

def display_separator(separator):
  print(f"  {separator}  |  {separator}  |  {separator}  ")
    
def display_board(board):
    display_separator("#")
    display_row(6, 7, 8, board)
    display_separator("#")
    display_hyphen(15)
    display_separator("#")
    display_row(3, 4, 5, board)
    display_separator("#")
    display_hyphen(15)
    display_separator("#")
    display_row(0, 1, 2, board)
    display_separator("#")

def player_input():
  player1 = None
  player2 = None
  while player1 not in ["X", "O"]:
    player1 = input("You are Player1. Please pick a marker 'X' or 'O'")
    if player1 == "X":
      player2 = "O"
    elif player1 == "O":
      player2 = "X"
    else:
      "You chose 'X' or 'O'"
  return (player1, player2)

def place_marker(board, marker, position):
  board[position] = marker

def row_check(board, mark):
  for num in range(0, 9, 3):
    # print(board[num: num+3])
    # print([mark] * 3)
    if board[num: num+3] == [mark] * 3:
      return True
  return False

def column_check(board, mark):
  for i in range(0, 3):
    if [board[n] for n in range(i, 9 ,3) ]  == [mark] * 3:
      return True
  return False

def diagonal_check(board, mark):
  print([board[n] for n in range(0, 9, 4)])
  if [board[n] for n in range(0, 9, 4)] == [mark] * 3:
    return True
  print([board[n] for n in range(2, 7, 2)])
  if [board[n] for n in range(2, 7, 2)] == [mark] * 3:
    return True
  return False

def win_check(board, mark):
  return row_check(board, mark) or column_check(board, mark) or diagonal_check(board, mark)

def choose_first():
  return random.randint(0,1)

def space_check(board, position):
  return isinstance(board[position], int)

def full_board_check(board):
  for marker in board:
    if isinstance(marker, int):
      return False
  return True

def player_choice(board):
  player_position = None
  while True:
    player_position = input("Choose your position (1-9)")
    try:
      player_position = int(player_position)
    except:
      print("Please enter integer")
      continue
    if player_position not in list(range(1,9)):
      print("Please choose from (1-9)")
      continue
    if not space_check(board, player_position-1):
      print("That position is already taken")
      continue
    break
  return player_position

def replay():
  player_input = None
  while player_input not in ["Yes", "No"]:
    player_input = input("Do you play again? - Yes or No: ")
    if player_input not in ["Yes", "No"]:
      print("Please enter Yes or No")
      continue
    if player_input == "Yes":
      player_input = True
      break
    else:
      player_input = False
      break
  return player_input

print('Welcome to Tic Tac Toe!')

while True:
  # Set the game up here
  game_on = True
  position_board = [1,2,3,4,5,6,7,8,9]
  player1_marker, player2_marker = player_input()
  while game_on:
    #Player 1 Turn
    print("Player1's turn")
    display_board(position_board)
    place_marker(position_board, player1_marker, player_choice(position_board)-1)
    display_board(position_board)
    if win_check(position_board, player1_marker):
        print("Player1 Wins")
        game_on = False
        break
    elif full_board_check(position_board):
        print("Draw")
        game_on = False
        break
    # Player2's turn.
    print("Player2's turn")
    display_board(position_board)
    place_marker(position_board, player2_marker, player_choice(position_board)-1)
    display_board(position_board)
    if win_check(position_board, player2_marker):
      print("Player2 Wins")
      game_on = False
      break
    elif full_board_check(position_board):
      print("Draw")
      game_on = False
      break
  if replay():
      continue
  else:
      break
