import random

def random_board():
  # A function that returns a random board of 15-puzzle
  # The board is represented as an array of array of strings

  blocks = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","--"] # Initiating the blocks
  random.shuffle(blocks) # Shuffling the blocks
  board = [[blocks[i*4+j] for i in range(4)] for j in range(4)] # Assigning the blocks to the board

  return board