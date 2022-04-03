from board import Board

def read(fileName):
  # A function that reads a board from a file and returns a Board object

  # Read file
  with open(fileName, "r") as f:
    data = f.read()

  board = [] # Initiating the board

  # Processing data
  data = data.split("\n")
  for i in range(4):
    data[i] = data[i].split(" ")
    for j in range(4):
      curr = data[i][j]
      if curr == "-" or curr == "0" or curr == "--": # Empty block is converted to 16
        board.append(16)
      else:
        board.append(int(curr))
  
  # Creating a Board object
  return Board(board, 0)