from time import perf_counter

def kurang_i(board):
  # A function that returns the number of blocks that are misplaced
  # The board is represented as an array of strings
  # The function will return a dictionary
  timeStart = perf_counter() # Start the timer
  board_copy = board.blocks[:] # Make a copy of the board blocks configuration
  kurang = {} # Initiate the dictionary
  for i in range(16):
    curr = (board_copy[i])
    kurang[curr] = 0
    for j in range(i+1, 16):
      if curr > (board_copy[j]):
        kurang[curr] += 1
  timeEnd = perf_counter() # End the timer
  return timeEnd-timeStart, kurang

def X(board):
  # Function X(board) receives a board
  # and returns the value of X (0 or 1)
  idx = board.emptyBlock() # find the index of the empty block
  return ((idx//4 + idx%4)%2) # 0 if row+col is even, 1 if row+col is odd

def sumAll(kurang_i, X):
  # Function sumAll(kurang_i, X) receives the value of kurang_i and X
  # and returns the sum of all values in kurang_i + X
  sumOfKurang_i = sum(kurang_i.values())
  return (sumOfKurang_i + X)
  
def reachableGoal(sumAll):
  # Function reachableGoal(sumAll) receives the value of the sum of all values in kurang_i + X
  # and returns True if it is even, False otherwise
  return ((sumAll)%2 == 0)