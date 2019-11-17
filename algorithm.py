from graph import Graph
inf = float('inf')

def checkAllClosed(graph):
  for i in range(len(graph.nodes)):
    if(graph.nodes[i].closed == False):
      return False
  return True

def getLessEstimate(graph):
  """
  @return índice do nodo aberto que tiver a menor estimativa
  """
  min = inf
  index = 0
  for i in range(len(graph.nodes)):
    if(graph.nodes[i].estimate < min and not(graph.nodes[i].closed)):
      min = graph.nodes[i].estimate
      index = i
  return index

def dijkstra(graph):
  """
  manipula o grafo passado como parâmetro e aplica o algoritmo de dijkstra
  """
  erro = 0
  while(not(checkAllClosed(graph))):
    if(erro > 1000000):
      print("ERRO! Dijkstra executado 1.000.001 vezes...")
      print("Provavelmente é um grafo desconexo!")
      exit()
    erro += 1
    selected = getLessEstimate(graph)
    graph.nodes[selected].close()
    for i in range(len(graph.nodes[selected].point)):
      if(not(graph.nodes[i].closed) and graph.nodes[selected].point[i] != 0):
        sumEstimate = graph.nodes[selected].estimate + graph.nodes[selected].point[i]
        if(sumEstimate < graph.nodes[i].estimate):
          graph.nodes[i].estimate = sumEstimate
          graph.nodes[i].ancestor = selected