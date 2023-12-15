import numpy as np

def part_one(input):
  path, _, *network = input.read().splitlines()
  ref = {}

  for n in network:
    curr, next = n.split(' = ')
    ref[curr] = next[1:-1].split(', ')

  curr = 'AAA'
  i = 0
  steps = 0
  while curr != 'ZZZ':
    if i == len(path):
      i = 0
    if path[i] == 'L':
      curr = ref[curr][0]
    else:
      curr = ref[curr][1]
    i += 1
    steps += 1

  return steps

def part_two(input):
  path, _, *network = input.read().splitlines()
  ref = {}
  positions = []

  for n in network:
    curr, next = n.split(' = ')
    ref[curr] = next[1:-1].split(', ')

    if curr[-1] == 'A':
      positions.append(curr)

  i = 0
  parts = []

  for p in positions:
    steps = 0
    while p[-1] != 'Z':
      if i == len(path):
        i = 0
      if path[i] == 'L':
        p = ref[p][0]
      else:
        p = ref[p][1]
      i += 1
      steps += 1
 
    parts.append(steps)

  return np.lcm.reduce(parts, dtype='int64')

with open('day8_input.txt', 'r') as input:
  print('part1', part_one(input))

with open('day8_input.txt', 'r') as input:
  print('part2', part_two(input))