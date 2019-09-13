from pathlib import Path
from algorithm import dijkstra
from graph import Graph

def Main():
  graph = Graph(graphFile)
  graph.getNodes()
  graph.setObjective(1, 4)
  graph.printGraph()
  dijkstra(graph)
  graph.printGraph()
  path = graph.getPath()
  print(path)

if __name__ == "__main__":
  graphFile = Path('graph')
  if(graphFile.exists() and graphFile.is_file()):
    Main()
  else:
    print("No graph file exists to execute algorith...")