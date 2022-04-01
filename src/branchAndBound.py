from queue import PriorityQueue
from board import Board

def branchAndBound(start):
  liveNodes = PriorityQueue()
  liveNodes.put((start.cost(), start))
  now = start

  while not liveNodes.empty() and not now.isGoal():
    now = liveNodes.get()
    curr = now[1]
    curr.print()

    try:
      up = curr.up()
      liveNodes.put((up.cost(), up))
    except IndexError:
      pass
    try:
      down = curr.down()
      liveNodes.put((down.cost(), down))
    except IndexError:
      pass
    try:
      left = curr.left()
      liveNodes.put((left.cost(), left))
    except IndexError:
      pass
    try:
      right = curr.right()
      liveNodes.put((right.cost(), right))
    except IndexError:
      pass

board = Board([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,15], 0)
branchAndBound(board)