from boardGenerator import randomBoard
from reachableGoal import *

# Generate initial board
board = ["01","03","04","15","02","--","05","12","07","06","11","14","08","09","10","13"]
board = ["01","02","03","04","05","06","--","08","09","10","07","11","13","14","15","12"]

# Output initial board
print("Susunan awal:")
for i in range(4):
  for j in range(4):
    print(board[i*4+j], end=" ")
  print()
print()

kurang = kurang_i(board)
print("Nilai Kurang(i):")
for key in sorted(kurang):
  print(f"{key}: {kurang[key]}")
print()

sums = sumAll(kurang, X(board))
print(f"Nilai sigma Kurang(i) + X: {sums}")

if not reachableGoal(sums):
  print("Persoalan tidak dapat diselesaikan.")