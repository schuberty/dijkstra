from node import Node

class Graph:
  def __init__(self, fileName):
    self.nodes = []
    self.file = fileName

  def getNodes(self):
    with open(self.file) as file:
      for line in file:
        node = Node()
        for c in line:
          if c.isdigit():
            node.point.append(int(c))
        self.nodes.append(node)

  def showGraph(self):
    for i in range(len(self.nodes)):
      print("Nodo " + str(i+1) + " = ", end = '')
      self.nodes[i].printNode()
