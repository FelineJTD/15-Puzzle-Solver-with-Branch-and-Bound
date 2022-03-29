import random

def randomBoard():
  # A function that returns a random board of 15-puzzle
  # The board is represented as an array of strings
  board = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","--"] # Initiating the board
  random.shuffle(board) # Shuffling the board
  return board