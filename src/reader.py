from board import Board
from block import Block

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
        board.append(Block(16))
      else:
        board.append(Block(int(curr)))
  
  return Board(board, 0, False)