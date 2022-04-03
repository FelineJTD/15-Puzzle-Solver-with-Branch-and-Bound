from queue import PriorityQueue
from board import Board
from time import sleep, perf_counter

def branchAndBound(start):
  timeStart = perf_counter()
  nodeCount = 0
  liveNodes = PriorityQueue()
  liveNodes.put((start.cost(), start))
  curr = start
  checked = {str(curr.blocks) : True}

  while (not curr.isGoal()) and (not liveNodes.empty()):
    now = liveNodes.get()
    curr = now[1]
    checked[str(curr.blocks)] = True

    up = curr.up()
    if (up is not None) and (str(up.blocks) not in checked):
      liveNodes.put((up.cost(), up))
      checked[str(up.blocks)] = True
      nodeCount += 1

    down = curr.down()
    if (down is not None) and (str(down.blocks) not in checked):
      liveNodes.put((down.cost(), down))
      checked[str(down.blocks)] = True
      nodeCount += 1
      
    left = curr.left()
    if (left is not None) and (str(left.blocks) not in checked):
      liveNodes.put((left.cost(), left))
      checked[str(left.blocks)] = True
      nodeCount += 1

    right = curr.right()
    if (right is not None) and (str(right.blocks) not in checked):
      liveNodes.put((right.cost(), right))
      checked[str(right.blocks)] = True
      nodeCount += 1
  
  timeEnd = perf_counter()
  if (curr.steps == 0):
    print("Loh puzzle-nya sudah selesai. >:(\n")
  else:
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
  return (timeEnd-timeStart, nodeCount)

# board = Board([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,15], 0)
# branchAndBound(board)