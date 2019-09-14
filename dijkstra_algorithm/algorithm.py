from graph import Graph
inf = float('inf')

def checkAllClosed(graph):
  for i in range(len(graph.nodes)):
    if(graph.nodes[i].closed == False):
      return False
  return True

def getLessEstimate(graph):
  min = inf
  index = 0
  for i in range(len(graph.nodes)):
    if(graph.nodes[i].estimate < min and not(graph.nodes[i].closed)):
      min = graph.nodes[i].estimate
      index = i
  return index

def dijkstra(graph):
  while(not(checkAllClosed(graph))):
    selected = getLessEstimate(graph)
    graph.nodes[selected].close()
    for i in range(len(graph.nodes[selected].point)):
      if(not(graph.nodes[selected] is graph.nodes[i]) and not(graph.nodes[i].closed) and graph.nodes[selected].point[i] != 0):
        sumEstimate = graph.nodes[selected].estimate + graph.nodes[selected].point[i]
        if(sumEstimate < graph.nodes[i].estimate):
          graph.nodes[i].estimate = sumEstimate
          graph.nodes[i].ancestor = selected