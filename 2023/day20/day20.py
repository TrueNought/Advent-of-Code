"""
Credits to the approach that Oliver Ni used to store the data.
Conjunctions stores all the incoming modules for each module, and the type of most recent pulse received.
Modules store the type of each module and its outgoing connections.
Flipflops stores the on/off state for flip-flop modules.
"""

from collections import deque, defaultdict
import numpy as np
from copy import deepcopy

with open('day20_input.txt') as input:
  input = input.read().splitlines()

def part_one(input):
  conjunctions = defaultdict(dict)
  modules = {}
  flipflops = {}

  for line in input:
    curr, target = line.split(' -> ')
    target = target.split(', ')
    modules[curr[1:]] = (curr[0], target)

    if curr[0] == '%':
      flipflops[curr[1:]] = False

    for t in target:
      conjunctions[t][curr[1:]] = False

  def send(curr, target, pulse):
    pulses[pulse] += 1
    conjunctions[target][curr] = pulse
    q.append((target, pulse))
  
  pulses = defaultdict(int)
  q = deque()
 
  for _ in range(1000):
    send('button', 'roadcaster', False)
    
    while q:
      curr, pulse = q.popleft()
      if curr not in modules:
        continue
      
      if modules[curr][0] == '%':
        if pulse:
          continue
        
        pulse = not flipflops[curr]
        flipflops[curr] = not flipflops[curr]
      
      elif modules[curr][0] == '&':
        pulse = not all(conjunctions[curr].values())
      
      for m in modules[curr][1]:
        send(curr, m, pulse)

  return np.prod(list(pulses.values()))


def part_two(input):
  conjunctions = defaultdict(dict)
  modules = {}
  flipflops = {}

  for line in input:
    curr, target = line.split(' -> ')
    target = target.split(', ')
    modules[curr[1:]] = (curr[0], target)

    if curr[0] == '%':
      flipflops[curr[1:]] = False

    for t in target:
      conjunctions[t][curr[1:]] = False
  
  def iterations(item, conjunctions, flipflops):
    def send(curr, target, pulse):
      conjunctions[target][curr] = pulse
      q.append((target, pulse))

    conjunctions = deepcopy(conjunctions)
    flipflops = deepcopy(flipflops)

    q = deque()
    presses = 0
    while True:
      send('button', 'roadcaster', False)
      presses += 1
    
      while q:
        if conjunctions['qb'][item]:
          return presses
        
        curr, pulse = q.popleft()
        if curr not in modules:
          continue
        
        if modules[curr][0] == '%':
          if pulse:
            continue
          
          pulse = not flipflops[curr]
          flipflops[curr] = not flipflops[curr]
        
        elif modules[curr][0] == '&':
          pulse = not all(conjunctions[curr].values())
        
        for m in modules[curr][1]:
          send(curr, m, pulse)

  cycles = []
  for item in ('kv', 'jg', 'rz', 'mr'):
    cycles.append(iterations(item, conjunctions, flipflops))

  return np.lcm.reduce(cycles, dtype='int64')

print('part1', part_one(input))
print('part2', part_two(input))