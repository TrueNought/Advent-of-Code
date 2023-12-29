import networkx as nx

with open('day25_input.txt') as input:
  input = input.read().splitlines()

def part_one(input):
  G = nx.Graph()

  for line in input:
    k, v = line.split(': ')
    for node in v.split(' '):
      G.add_edge(k, node, capacity=1)

  for i in range(len(list(G.nodes)) - 1):
    for j in range(i + 1, len(list(G.nodes))):
      source = list(G.nodes)[i]
      sink = list(G.nodes)[j]
      cut, (a, b) = nx.minimum_cut(G, source, sink)
      if cut == 3:
        return len(a) * len(b)

print('part1', part_one(input))