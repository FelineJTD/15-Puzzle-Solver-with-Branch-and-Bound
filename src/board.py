class Board:
  # A class that represents a board of 15-puzzle

  # Attributes:
  #   blocks: an array of integers representing the blocks on the board
  #   steps: an integer representing the number of steps taken to reach the board
  #   prevStep: a Board object representing the previous step taken to reach the board
  #   misplacedBlocks: an integer representing the number of misplaced blocks on the board

  # Methods:
  #   copy: a function that returns a copy of the board and adds one step
  #   print: a function that prints the board
  #   emptyBlock: a function that returns the index of the empty block on the board

  #   swap: a function that returns a copy of the board with the blocks swapped
  #   up: a function that returns a copy of the board with the empty block swapped with the block above it
  #   down: a function that returns a copy of the board with the empty block swapped with the block below it
  #   left: a function that returns a copy of the board with the empty block swapped with the block to the left of it
  #   right: a function that returns a copy of the board with the empty block swapped with the block to the right of it

  #   countMisplacedBlocks: a function that returns the number of misplaced blocks on the board
  #   isGoal: a function that returns True if the board is a goal board, False otherwise
  #   cost: a function that returns the cost of the board
  #   __lt__: a function that returns True if the board has a lower cost than the other board, False otherwise

  def __init__(self, blocks, steps):
    self.steps = steps
    self.blocks = blocks
    self.prevStep = None
    self.misplacedBlocks = self.countMisplacedBlocks()

  def copy(self):
    return Board(self.blocks[:], self.steps+1)

  def print(self):
    for i in range(4):
      for j in range(4):
        if (self.blocks[i*4+j] < 10):
          print(f"0{self.blocks[i*4+j]}", end=" ")
        elif (self.blocks[i*4+j] == 16):
          print("--", end=" ")
        else:
          print(self.blocks[i*4+j], end=" ")
      print()
    print()

  def emptyBlock(self):
    for i in range(16):
      if self.blocks[i] == 16:
        return i

  def swap(self, i, j):
    result = self.copy()
    result.prevStep = self
    temp = result.blocks[i]
    result.blocks[i] = result.blocks[j]
    result.blocks[j] = temp
    result.misplacedBlocks = result.countMisplacedBlocks()
    return result

  def up(self):
    if self.emptyBlock() < 4:
      return None
    else:
      up = self.swap(self.emptyBlock()-4, self.emptyBlock())
      return up

  def down(self):
    if self.emptyBlock() > 11:
      return None
    else:
      down = self.swap(self.emptyBlock()+4, self.emptyBlock())
      return down

  def left(self):
    if self.emptyBlock() % 4 == 0:
      return None
    else:
      left = self.swap(self.emptyBlock()-1, self.emptyBlock())
      return left

  def right(self):
    if self.emptyBlock() % 4 == 3:
      return None
    else:
      right = self.swap(self.emptyBlock()+1, self.emptyBlock())
      return right

  def countMisplacedBlocks(self):
    misplaced = 0
    for i in range(16):
      if self.blocks[i] != 16 and self.blocks[i] != i+1:
        misplaced += 1
    return misplaced
  
  def isGoal(self):
    return self.misplacedBlocks == 0

  def cost(self):
    return self.steps+self.misplacedBlocks

  def __lt__(self, other):
    if(self.steps<other.steps):
      return self
    else:
      return other