class Board:
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
    up = self.swap(self.emptyBlock()-4, self.emptyBlock())
    up.prevStep = self
    return up

  def down(self):
    down = self.swap(self.emptyBlock()+4, self.emptyBlock())
    down.prevStep = self
    return down

  def left(self):
    left = self.swap(self.emptyBlock()-1, self.emptyBlock())
    left.prevStep = self
    return left

  def right(self):
    right = self.swap(self.emptyBlock()+1, self.emptyBlock())
    right.prevStep = self
    return right

  def countMisplacedBlocks(self):
  # A function that returns the number of blocks that are misplaced
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