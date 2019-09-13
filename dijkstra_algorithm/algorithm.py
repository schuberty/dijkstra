from graph import Graph

def allClosed(graph):
  for i in range(len(graph.nodes)):
    if(graph.nodes[i].closed == False):
      return False
  return True

def dijkstra(graph):
  while(not(allClosed(graph))):
    selected = graph.getLessEstimate()
    graph.nodes[selected].close()
    for i in range(len(graph.nodes[selected].point)):
      if(graph.nodes[selected] is graph.nodes[i]):
        continue
      else:
        if(not(graph.nodes[i].closed) and graph.nodes[selected].point[i] != 0):
          sumEstimate = graph.nodes[selected].estimate + graph.nodes[selected].point[i]
          if(sumEstimate < graph.nodes[i].estimate):
            graph.nodes[i].estimate = sumEstimate
            graph.nodes[i].ancestor = selected