from block import Block

class Board:
  def __init__(self, blocks, steps, isInteger=True):
    self.steps = steps
    if (isInteger):
      self.blocks = []
      for i in range(16):
        self.blocks.append(Block(blocks[i]))
    else:
      self.blocks = blocks

  def copy(self):
    return Board(self.blocks[:], self.steps+1, False)

  def print(self):
    for i in range(4):
      for j in range(4):
        self.blocks[i*4+j].print()
      print()
    print()

  def emptyBlock(self):
    for i in range(16):
      if self.blocks[i].value == 16:
        return i

  def swap(self, i, j):
    result = self.copy()
    temp = result.blocks[i]
    result.blocks[i] = result.blocks[j]
    result.blocks[j] = temp
    return result

  def up(self):
    return self.swap(self.emptyBlock()-4, self.emptyBlock())

  def down(self):
    return self.swap(self.emptyBlock()+4, self.emptyBlock())

  def left(self):
    return self.swap(self.emptyBlock()-1, self.emptyBlock())

  def right(self):
    return self.swap(self.emptyBlock()+1, self.emptyBlock())

  def countMisplacedBlocks(self):
  # A function that returns the number of blocks that are misplaced
    misplaced = 0
    for i in range(16):
      if self.blocks[i].value != 16 and self.blocks[i].value != i+1:
        misplaced += 1
    return misplaced
  
  def isGoal(self):
    return self.countMisplacedBlocks() == 0

  def cost(self):
    return self.steps+self.countMisplacedBlocks()