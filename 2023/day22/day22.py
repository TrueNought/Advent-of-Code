"""
Credits to HyperNeutrino for the approach used for this problem.
"""

from collections import defaultdict, deque

with open('day22_input.txt') as input:
  input = input.read().splitlines()

def part_one(input):
  bricks =  []
  
  for line in input:
    brick = line.replace('~', ',').split(',')
    brick = list(map(int, brick))
    bricks.append(brick)

  bricks.sort(key=lambda x: x[2])

  def overlaps(a, b):
    if max(a[0], b[0]) <= min(a[3], b[3]):
      if max(a[1], b[1]) <= min(a[4], b[4]):
        return True
    return False

  for i, b in enumerate(bricks):
    highest = 1
    for c in bricks[:i]:
      if overlaps(b, c):
        highest = max(highest, c[5] + 1)
    b[5] = highest + b[5] - b[2]
    b[2] = highest

  bricks.sort(key=lambda x: x[2])
  supports = defaultdict(set)
  supportedby = defaultdict(int)

  for i, upper in enumerate(bricks):
    for j, lower in enumerate(bricks[:i]):
      if overlaps(lower, upper) and lower[5] + 1 == upper[2]:
        supports[j].add(i)
        supportedby[i] += 1

  result = 0
  for i in range(len(bricks)):
    if not supports[i]:
      result += 1
      continue
    
    if all(supportedby[j] >= 2 for j in supports[i] if supports[i]):
      result += 1

  return result

def part_two(input):
  bricks =  []
  
  for line in input:
    brick = line.replace('~', ',').split(',')
    brick = list(map(int, brick))
    bricks.append(brick)

  bricks.sort(key=lambda x: x[2])

  def overlaps(a, b):
    if max(a[0], b[0]) <= min(a[3], b[3]):
      if max(a[1], b[1]) <= min(a[4], b[4]):
        return True
    return False

  for i, b in enumerate(bricks):
    highest = 1
    for c in bricks[:i]:
      if overlaps(b, c):
        highest = max(highest, c[5] + 1)
    b[5] = highest + b[5] - b[2]
    b[2] = highest

  bricks.sort(key=lambda x: x[2])
  supports = defaultdict(set)
  supportedby = defaultdict(set)

  for i, upper in enumerate(bricks):
    for j, lower in enumerate(bricks[:i]):
      if overlaps(lower, upper) and lower[5] + 1 == upper[2]:
        supports[j].add(i)
        supportedby[i].add(j)
  
  result = 0
  for i in range(len(bricks)):
    q = deque(j for j in supports[i] if len(supportedby[j]) == 1)
    falling = set(q)
    falling.add(i)

    while q:
      curr = q.popleft()
      for j in supports[curr] - falling:
        if supportedby[j] <= falling:
          q.append(j)
          falling.add(j)

    result += len(falling) - 1
  return result

print('part1', part_one(input))
print('part2', part_two(input))