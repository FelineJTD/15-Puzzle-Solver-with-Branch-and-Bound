from board import Board

def read(fileName):
  board = []
  with open(fileName, "r") as f:
    data = f.read()

  data = data.split("\n")
  for i in range(4):
    data[i] = data[i].split(" ")
    for j in range(4):
      curr = data[i][j]
      if curr == "-":
        board.append(16)
      else:
        board.append(int(curr))
  
  return Board(board, 0)