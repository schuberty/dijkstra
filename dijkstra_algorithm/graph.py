from node import *

class Graph:
  def __init__(self, fileName):
    self.nodes = []
    self.file = fileName
    self.start = -1
    self.goal = -1

  def getNodes(self):
    if(len(self.nodes) != 0):
      return
    with open(self.file, 'r') as file:
      for line in file:
        node = Node()
        for c in line:
          if c.isdigit():
            node.point.append(int(c))
        self.nodes.append(node)

  def printGraph(self):
    print(" NODE - TO - CLOSED - ANCESTOR - ESTIMATE")
    for i in range(len(self.nodes)):
      print("Node " + str(chr(i+65)) + " = ", end = '')
      self.nodes[i].printNode()
    # print("START NODE = " + str(self.start+1) + "\nGOAL NODE = " + str(self.goal+1))

  def setObjective(self, start, goal):
    if(start is goal):
      print("Start can't be goal")
      return True
    start = int(ord(start))-65
    goal = int(ord(goal))-65
    self.start = start
    self.goal = goal
    self.nodes[self.start].estimate = 0
    self.nodes[self.start].ancestor = start

  def getGoal(self):
    return self.nodes[self.goal]

  def getLessEstimate(self):
    min = inf
    index = 0
    for i in range(len(self.nodes)):
      if(self.nodes[i].estimate < min and not(self.nodes[i].closed)):
        min = self.nodes[i].estimate
        index = i
    return index

  def getPath(self):
    path = []
    selected = self.goal
    while(not(self.nodes[selected] is self.nodes[self.start])):
      path.append(selected)
      selected = self.nodes[selected].ancestor
    path.append(self.start)
    path.reverse()
    for i in range(len(path)):
      path[i] = chr(path[i]+65)
    return path