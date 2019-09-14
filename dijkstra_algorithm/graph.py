from pathlib import Path
inf = float('inf')

class Node:
  """
  salva as informações de cada nodo.
  @para point    : cada índice tem o valor para o nodo[índice] atual ou zero caso não aponte;
  @para closed   : se o nodo está fechado ou não;
  @para ancestor : índice para o antecessor;
  @para estimate : valor do custo do caminho da origem até o nodo atual.
  """
  def __init__(self):
    self.point = []
    self.closed = False
    self.ancestor = -1
    self.estimate = inf
  
  def close(self):
    self.closed = True

class Graph:
  """
  gera e administra o grafo
  @para nodes : salva as informações de cada nodo;
  @para file  : nome do arquivo para gerar o grafo;
  @para start : índice do nodo inicial.
  """
  def __init__(self, fileName):
    self.nodes = []
    self.file = fileName
    self.start = -1
    self.setNodes()

  def setNodes(self):
    """
    do arquivo, gera os nodos no grafo
    """
    graphFile = Path(self.file)
    if(not(graphFile.exists() and graphFile.is_file())):
      print("No graph file exists to execute algorith...")
      return
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

  def setStart(self, start):
    start = int(ord(start))-65
    self.start = start
    self.nodes[self.start].estimate = 0
    self.nodes[self.start].ancestor = start

  def getPath(self, goal):
    """
    @return lista com os nome dos nodos até o nodo desejado
    """
    selected = goal
    path = []
    while(not(self.nodes[selected] is self.nodes[self.start])):
      path.append(selected)
      selected = self.nodes[selected].ancestor
    path.append(self.start)
    path.reverse()
    for i in range(len(path)):
      path[i] = chr(path[i]+65)
    return path

  def printGraph(self):
    for i in range(len(self.nodes)):
      print("[ " + chr(i+65) + "-]->", end='')
      for j in range(len(self.nodes[i].point)):
        if(self.nodes[i].point[j] != 0):
          print("(" + chr(j+65) + "," + str(self.nodes[i].point[j]) + ")->" ,end='')
      print("#")

  def printDiagram(self):
    for i in range(len(self.nodes)):
      print("[ " + chr(i+65) + " ] Estimativa = " + str(self.nodes[i].estimate), end='')
      print("; Precedente = " + chr(self.nodes[i].ancestor+65))