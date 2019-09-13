from graph import Graph

def allClosed(graph):
  for i in range(len(graph.nodes)):
    if(graph.nodes[i].closed == False):
      return False
  return True

def dijkstra(graph):
  graph.printGraph()
  # while(not(allClosed(graph))):