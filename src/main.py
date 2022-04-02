from boardGenerator import randomBoard
from reader import read
from reachableGoal import *
from branchAndBound import branchAndBound
from board import Board

# Generate initial board
#board = randomBoard()
#board = Board([1,2,3,4,5,6,16,8,9,10,7,11,13,14,15,12], 0)
#board = Board([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,15], 0)

board = read("../test/test10.txt")

# Output initial board
print("Susunan awal:")
board.print()

kurang = kurang_i(board)
print("Nilai Kurang(i):")
for key in sorted(kurang):
  print(f"{key}: {kurang[key]}")
print()

sums = sumAll(kurang, X(board))
print(f"Nilai sigma Kurang(i) + X: {sums}")

if not reachableGoal(sums):
  print("Persoalan tidak dapat diselesaikan.")
else:
  branchAndBound(board)