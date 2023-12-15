from collections import defaultdict
import re

def convert(s):
  val = 0
  for ch in s:
    val += ord(ch)
    val *= 17
    val %= 256
  return val

def part_one(input):
  input = input.read().split(',')
  return sum(map(convert, input))

def part_two(input):
  input = input.read().split(',')
  ref = defaultdict(list)

  for s in input:
    label = re.search(r'[a-z]+', s).group()
    box = convert(label)
    if '-' in s:
      for x in ref[box]:
        if x[0] == label:
          ref[box].remove(x)
          if not ref[box]:
            del ref[box]
          break 
      continue
    
    focal = int(s[-1])
    for i, x in enumerate(ref[box]):
      if x[0] == label:
        ref[box][i] = (label, focal)
        break 
    else:
      ref[box].append((label, focal))

  total = 0
  for k, v in ref.items():
    for i, lens in enumerate(v):
      total += (k + 1) * (i + 1) * lens[1]

  return total

with open('day15_input.txt', 'r') as input:
  print('part1', part_one(input))

with open('day15_input.txt', 'r') as input:
  print('part2', part_two(input))