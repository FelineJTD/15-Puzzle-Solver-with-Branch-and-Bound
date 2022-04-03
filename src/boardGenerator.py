import random
from board import Board

def randomBoard():
  # A function that returns a random board of 15-puzzle
  blocks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] # Initiating the blocks
  random.shuffle(blocks) # Shuffling the blocks
  board = Board(blocks, 0) # Creating a Board object
  return board