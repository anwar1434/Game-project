#TIC-TAC-TOE board:
import random

def print_board(board):
  for i, row in enumerate(board):
      row_str = " "
      for j, value in enumerate(row):
          row_str += value
          if j != len(row) - 1:
              row_str += " | "
      print(row_str)
      if i != len(board) - 1:
          print("-----------")

def player_move(turn, board): 
  while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = turn
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")

def computer_choice(turn, board):
  empty_cells = [(i, j) for i in range(3) for j in range(3) if board [i][j] == " "]
  if empty_cells:
    row, col = random.choice(empty_cells)
    board[row][col] = turn
    print(f"Computer placed '{turn}' in position ({row + 1}, {col + 1})")

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

board = [
    [" ", " ", " "],
    [" ", " ", " "],  
    [" ", " ", " "],]

turn = "X"
turn_number = 0
print_board(board)

while turn_number < 9:
  if turn == "X":
    print()
    print(f"It's the {turn} player, please select your move: ")
    player_move(turn, board)
  else: 
    print(f"It's the {turn} player's turn (computer)")
    computer_choice(turn, board)
  print_board(board)
  
  winner = check_winner(board)
  if winner:
      print(f"Player {winner} wins!")
      break
  
  # Switch turns
  turn = "O" if turn == "X" else "X"
  turn_number += 1

if turn_number == 9 and not winner:
    print("It's a draw!")