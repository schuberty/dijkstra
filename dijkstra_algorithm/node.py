inf = float('inf')

class Node:
  def __init__(self):
    self.point = []
    self.closed = False
    self.ancestor = -1
    self.estimate = inf
  
  def printNode(self):
    # print(" NODE - TO - CLOSED - ANCESTOR - ESTIMATE")
    print(str(self.point) + " " + str(self.closed) + " " + str(self.ancestor) + " " + str(self.estimate))

  def close(self):
    self.closed = True
