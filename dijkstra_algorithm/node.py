inf = float('inf')

class Node:
  def __init__(self):
    self.point = []
    self.closed = False
    self.predesc = -1
    self.estimate = inf
  
  def printNode(self):
    print(str(self.point) + " " + str(self.closed) + " " + str(self.predesc) + " " + str(self.estimate))
