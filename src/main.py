from randomizer import random_board

# Generate initial board
board = random_board()
# Output initial board
print("Initial board:")
for row in board:
  for block in row:
    print(block, end=" ")
  print()
print()

