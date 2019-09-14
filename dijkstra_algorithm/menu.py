from sys import argv
from time import sleep
from pathlib import Path
from graph import Graph
from algorithm import dijkstra
import click

def run():
  click.clear()
  print("Executando " + argv[0] + "...")

  if(len(argv) != 3):
    print("Sem parâmetros informados!\n    Modo de uso:")
    print(" > python " + argv[0] + " [ARQUIVO] [VÉRTICE INICIAL]")
    exit()
  else:
    file = Path(argv[1])
    if(not(file.is_file() and file.exists())):
      print("Arquivo \"" + argv[1] + "\" não existe, enviar arquivo existente!")
      print(" > python " + argv[0] + " [ARQUIVO] [VÉRTICE INICIAL]")
      exit()
    else:
      print("Arquivo do grafo: \"" + argv[1] + "\"   |OK|")
      num = 0
      for line in open(file):
        if(line is "\n"):
          continue
        num += 1
      index = ord(argv[2])-65
      if(index < num and index >= 0 and index < 26):
        print("Vértice inicial do grafo: " + argv[2] + " |OK|")
      else:
        print("Vértice inicial [" + argv[2] + "] inexistente.")
        print("Vértices existentes = { ", end='')
        for i in range(num):
          print(chr(i+65) + " ", end='')
        print("}\nSelecionar vértice existente!")
        print(" > python " + argv[0] + " [ARQUIVO] [VÉRTICE INICIAL]")
        exit()
  
  graph = Graph(argv[1])
  graph.setStart(argv[2])
  print("\\--" + "--"*14 + "---/")
  print(" Executando Algoritmo de DIJKSTRA")
  dijkstra(graph)
  print(" Algoritmo executado...")
  print("/--" + "--"*14 + "---\\")

  return graph

def result(graph):
  print("Vértices = { ", end='')
  for i in range(len(graph.nodes)):
    if(i != graph.start):
      print(chr(i+65) + " ", end='')
  print("}")
  v = input("Digite um vértice > ")
  v = ord(v)-65
  if(v < len(graph.nodes) and v >= 0 and v < 26 and v != graph.start):
    path = graph.getPath(v)
    print(path)

def loop(graph):
  menu()
  print(" Digite um valor (1-4)")
  c = input(" > ")
  while(c.isdigit):
    if(c == '1'):
      result(graph)
    elif(c == '2'):
      click.clear()
      print("  Grafo em Lista de Adjacência:")
      graph.printGraph()
    elif(c == '3'):
      click.clear()
      print("  Informações dos Nodos:")
      graph.printDiagram()
    elif(c == '4'):
      print("Deletando grafo e saindo...")
      del graph
      exit()
    else:
      click.clear()
      menu()
      print(" Digite um valor válido (1-4)")
      c = input(" > ")
      continue

    menu()
    print(" Digite um valor (1-4)")
    c = input(" > ")
  
def menu():
  print("_________________________________________")
  print("                ~ MENU ~")
  print("1. Mostrar caminho mínimo entre o vértice")
  print("   inicial e...")
  print("2. Grafo em lista de adjacência;")
  print("3. Informações dos nodos;")
  print("4. SAIR.")