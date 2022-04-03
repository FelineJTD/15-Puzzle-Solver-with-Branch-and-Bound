from boardGenerator import randomBoard
from reader import read
from reachableGoal import *
from branchAndBound import branchAndBound
from board import Board
import sys

if (len(sys.argv) > 1):
  fileName = sys.argv[1]
  try:
    board = read(fileName)
  except FileNotFoundError:
    print("File tidak ditemukan.")
    sys.exit(1)
else:
  board = randomBoard()

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
  timeElapsedBnB, nodeCount = branchAndBound(board)
  print(f"Waktu yang diperlukan: {timeElapsedBnB:0.4f} detik")
  print(f"Jumlah simpul yang dibangkitkan: {nodeCount}")