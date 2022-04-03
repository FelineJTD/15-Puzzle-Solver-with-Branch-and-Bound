from queue import PriorityQueue
from time import perf_counter

def branchAndBound(start):
  # Function branchAndBound accepts initial board,
  # prints the steps taken to reach goal,
  # and returns the time taken and number of nodes generated.

  # Formats ehe, don't mind this :D
  green = "\033[92m"
  cyan = "\033[96m"
  red = "\033[91m"
  u = "\033[4m"
  b = "\033[1m"
  end = "\033[0m"

  timeStart = perf_counter() # Start timer

  # Initialize variables
  nodeCount = 0 # Number of nodes generated
  liveNodes = PriorityQueue() # PriorityQueue for live nodes
  liveNodes.put((start.cost(), start))
  curr = start
  checked = {str(curr.blocks) : True} # Dictionary for checked nodes

  # Iterate through liveNodes until goal is reached or all nodes are checked
  while (not curr.isGoal()) and (not liveNodes.empty()):
    # Take the node with the lowest cost from liveNodes
    curr = liveNodes.get()[1]
    # Add current node to checked nodes
    checked[str(curr.blocks)] = True

    # For each node, try to swap empty block up, down, left, and right
    # and add the swapped board to liveNodes if it's not yet checked
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
  # Goal is reached

  timeEnd = perf_counter() # End timer

  # Output steps
  if (curr.steps == 0):
    print(f"{red}{b}Loh puzzle-nya sudah selesai. >:(\n{end}{end}")
  else:
    print(f"{green}{b}Berhasil diselesaikan!{end}{end}")
    stepsToSuccess = []
    currStep = curr

    while (currStep.prevStep is not None):
      stepsToSuccess.append(currStep)
      currStep = currStep.prevStep

    print(f"{u}Awalnya gini:{end}")
    start.print()

    for i in range(len(stepsToSuccess)-1, -1, -1):
      print(f"{u}Langkah ke-{len(stepsToSuccess)-i}:{end}")
      stepsToSuccess[i].print()
      
    print(f"{cyan}Langkah yang diperlukan: {curr.steps}{end}")

  return (timeEnd-timeStart, nodeCount)