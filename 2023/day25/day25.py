import networkx as nx

with open('day25_input.txt') as input:
  input = input.read().splitlines()

def part_one(input):
  G = nx.Graph()

  for line in input:
    k, v = line.split(': ')
    for node in v.split(' '):
      G.add_edge(k, node, capacity=1)

  for source in list(G.nodes)[:-1]:
    for sink in list(G.nodes)[1:]:
      cut, (a, b) = nx.minimum_cut(G, source, sink)
      if cut == 3:
        return len(a) * len(b)

print('part1', part_one(input))