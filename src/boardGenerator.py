import random
from block import Block
from board import Board

def randomBoard():
  # A function that returns a random board of 15-puzzle
  # The board is represented as an array of strings
  blocks = [] # Initiating the board
  for i in range(1,17):
    blocks.append(Block(i))
  random.shuffle(blocks) # Shuffling the board
  board = Board(blocks, 0, False) # Creating a Board object
  return board