from queue import PriorityQueue
from board import Board
from time import sleep

def branchAndBound(start):
  nodeCount = 0
  liveNodes = PriorityQueue()
  liveNodes.put((start.cost(), start))
  curr = start
  checked = {str(curr.blocks) : True}

  while (not curr.isGoal()) and (not liveNodes.empty()):
    now = liveNodes.get()
    curr = now[1]
    checked[str(curr.blocks)] = True

    try:
      up = curr.up()
      if (str(up.blocks) not in checked):
        liveNodes.put((up.cost(), up))
        checked[str(up.blocks)] = True
        nodeCount += 1
    except IndexError:
      pass

    try:
      down = curr.down()
      if (str(down.blocks) not in checked):
        liveNodes.put((down.cost(), down))
        checked[str(down.blocks)] = True
        nodeCount += 1
    except IndexError:
      pass
      
    try:
      left = curr.left()
      if (str(left.blocks) not in checked):
        liveNodes.put((left.cost(), left))
        checked[str(left.blocks)] = True
        nodeCount += 1
    except IndexError:
      pass

    try:
      right = curr.right()
      if (str(right.blocks) not in checked):
        liveNodes.put((right.cost(), right))
        checked[str(right.blocks)] = True
        nodeCount += 1
    except IndexError:
      pass

  print("Berhasil diselesaikan.")
  stepsToSuccess = []
  currStep = curr
  
  while (currStep.prevStep is not None):
    stepsToSuccess.append(currStep)
    currStep = currStep.prevStep
  for i in range(len(stepsToSuccess)-1, -1, -1):
    print(f"Langkah ke-{len(stepsToSuccess)-i}:")
    stepsToSuccess[i].print()
  print(f"Langkah yang diperlukan: {curr.steps}")
  print(f"Waktu yang diperlukan: detik")
  print(f"Jumlah simpul yang dibangkitkan: {len(stepsToSuccess)}")

# board = Board([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,15], 0)
# branchAndBound(board)