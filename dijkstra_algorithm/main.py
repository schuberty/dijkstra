from graph import Graph
from pathlib import Path






def Main():
  graph = Graph(graphFile)
  graph.getNodes()
  graph.showGraph()

if __name__ == "__main__":
  graphFile = Path('graph')
  if(graphFile.exists() and graphFile.is_file()):
    Main()
  else:
    print("No graph file exists to execute algorith...")