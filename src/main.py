from boardGenerator import randomBoard
from reader import read
from reachableGoal import *
from branchAndBound import branchAndBound
import sys
cyan = "\033[96m"
red = "\033[91m"
end = "\033[0m"

# Read file if given, otherwise use a random board
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

# Output kurang(i) of the initial board
timeElapsedKurang_i, kurang = kurang_i(board)
print("Nilai Kurang(i):")
for key in sorted(kurang):
  print(f"{key}: {kurang[key]}")
print()

# Output the sum of all values in kurang(i) + X
sums = sumAll(kurang, X(board))
print(f"Nilai sigma Kurang(i) + X: {sums}\n")

# Perform branch and bound if the board is solvable, otherwise print an error message
timeElapsedBnB = 0
nodeCount = 0
if not reachableGoal(sums):
  print(f"{red}Persoalan tidak dapat diselesaikan.\n{end}")
else:
  timeElapsedBnB, nodeCount = branchAndBound(board)

# Output time taken and number of nodes generated
print(cyan, end="")
print(f"Waktu yang diperlukan: {timeElapsedKurang_i+timeElapsedBnB:0.4f} detik")
print(f"Jumlah simpul yang dibangkitkan: {nodeCount}")
print(end, end="")