inf = float('inf')

class Node:
  """
  save each node info
  @para point    : each index has value for other node,
                   or zero if has no connection;
  @para closed   : if it is closed or not;
  @para ancestor : index to the ancestor in the graph;
  @para estimate : estimate from the goal node in the graph.
  """
  def __init__(self):
    self.point = []
    self.closed = False
    self.ancestor = -1
    self.estimate = inf
  
  def printNode(self):
    # print(" NODE - TO - CLOSED - ANCESTOR - ESTIMATE")
    print(str(self.point) + " " + str(self.closed) + " " + str(chr(self.ancestor+65)) + " " + str(self.estimate))

  def close(self):
    self.closed = True

class Graph:
  """
  generate and manage the graph
  @para nodes : store nodes info
  @para file  : file name to generate the graph
  @para start : index for start node
  @para goal  : index for goal node
  """
  def __init__(self, fileName):
    self.nodes = []
    self.file = fileName
    self.start = -1
    self.goal = -1
    self.setNodes()

  def setNodes(self):
    """
    from _file_ generate the nodes for _nodes_
    """
    if(len(self.nodes) != 0):
      return
    with open(self.file, 'r') as file:
      for line in file:
        node = Node()
        c = ""
        for i in range(len(line)):
          if(line[i].isdecimal()):
            c = c + line[i]
          else:
            node.point.append(int(c))
            c = ""
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
    return path, self.nodes[self.goal].estimate