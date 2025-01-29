
# This is great for learning the fundamentals of code, but
# actually isn't very realistic. Most software engineers
# spend their time modifying and maintaining existing
# programs, not writing entirely new ones.

# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this. DONE 

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point. DONE 

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board. DONE 

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.


def play_game(board_size):
  board = make_blank_board(board_size)
  player = "X"
  while not is_game_over(board):# is game_ocer => T/F not True - code doesn't run - False ie. not match /complete => F - not False => True
    print(print_board(board))
    print("It's " + player + "'s turn.")
    # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    board = make_move(board, row, column, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")

def make_blank_board(board_size):
  grid = []
  for row in range(0, board_size):
    row = ['.'] * board_size
    grid.append(row)
  return grid 

def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

def make_move(board, row, column, player):
  # check here to see if 'X' or 'O' already in place
#  if board[row][column] != '.' and board[row][column] != 'X':
    if board[row][column] not in ['X', 'O']:# Q1 
      board[row][column] = player
    else:
      print('Sorry - that tile is taken')
      row = int(input("Enter another row: "))
      column = int(input("Enter another column: "))
      make_move(board, row, column, player)
    return board
    # else:
    #   print('Try again! That tile is taken!!!')
    #   play_game(board)
  # board[row][column] = player # original
  # return board
def generate_groups_to_check(board_size):
  groups = []
  for row in range(0, board_size):
    row_group = []
    col_group = []
    for col in range(0, board_size):
      row_group.append((row, col))
      col_group.append((col, row))
    groups.append(row_group)
    groups.append(col_group)

  diag_fwd = []
  diag_bwd = []
  for i in range(0, board_size):
    diag_fwd.append((i, i))
    diag_bwd.append((i, board_size - i -1))
  groups.append(diag_bwd)
  groups.append(diag_fwd)
  return groups


# This function will extract three cells from the board
def get_cells(board, coord_1, coord_2, coord_3):
  return get_cells_by_list(board, [coord_1, coord_2, coord_3])



# make more gemneric 
def get_cells_by_list(board, coords):
  cells = []
  for coord in coords: 
    cells.append(board[coord[0]][coord[1]])
  return cells
  

# board = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
# ]




# This function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, coords):
  cells = get_cells_by_list(board, coords)
  return "." not in cells

# This function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, coords):
  cells = get_cells_by_list(board, coords)
  return cells[0] == cells[1] and cells[1] == cells[2]


# checks if all tiles filled
def is_draw(board):
  for row in board:
    if '.' in row:
      return False
  return True

# We'll make a list of groups to check:

groups_to_check = [
  # Rows
  [(0, 0), (0, 1), (0, 2), (0, 3), (0,4)],
  [(1, 0), (1, 1), (1, 2), (1, 3), (1,4)],
  [(2, 0), (2, 1), (2, 2), (2, 3), (2,4)],
  [(3, 0), (3, 1), (3, 2), (3, 3), (3,4)],
  [(4, 0), (4, 1), (4, 2), (4, 3), (4,4)],
  # Columns
  [(0, 0), (1, 0), (2, 0), (3, 0), (4,0)],
  [(0, 1), (1, 1), (2, 1), (3, 1), (4,1)],
  [(0, 2), (1, 2), (2, 2), (3, 2), (4,2)],
  [(0, 3), (1, 3), (2, 3), (3, 3), (4,3)],
  [(0, 4), (1, 4), (2, 2), (3, 4), (4,4)],
  # Diagonals
  [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
  [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
]


def is_game_over(board):
  
  if is_draw(board):
    print("Game over! All cells are filled!")
    return True # Game ends
   
  # We go through our groups
  for group in groups_to_check:
    # If any of them are empty, they're clearly not a
    # winning row, so we skip them.
    if is_group_complete(board, group):# if True next 
      if are_all_cells_the_same(board, group):
        return True # We found a winning row!
        # Note that return also stops the function
  return False # If we get here, we didn't find a winning row

print("Game time!")
play_game(6)
