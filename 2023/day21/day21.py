"""
Part 2: Noticing that total steps divided by grid length is 26501365 % 131 = 65, let f(n) be number of reachable plots after 65 + 131*n steps where n = number of grid lengths. Since f is quadratic, we calculate 3 points to solve for the 3 coefficients for a quadratic before plugging in and solving.
"""

from collections import deque
from numpy.polynomial import Polynomial
import numpy as np

with open('day21_input.txt') as input:
  grid = input.read().splitlines()

def part_one(grid):
  start = [(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S']
  q = deque(start)
  visited = set(start)
  res = set()

  while q:
    r, c, s = q.popleft()
    if s % 2 == 0:
      res.add((r, c))
    
    if s == 64:
      continue
    
    for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
      if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in visited:
        q.append((nr, nc, s + 1))
        visited.add((nr, nc))

  return len(res)

def part_two(grid):
  length = len(grid)
  steps = 26501365
  remainder = steps % length
  
  def search(steps):
    start = [(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S']
    q = deque(start)
    visited = set(start)
    res = set()

    while q:
      r, c, s = q.popleft()
      if steps % 2 == 0 and s % 2 == 0:
        res.add((r, c))
      elif steps % 2 == 1 and s % 2 == 1:
        res.add((r, c))

      if s == steps:
        continue

      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if grid[nr % length][nc % length] != '#' and (nr, nc) not in visited:
          q.append((nr, nc, s + 1))
          visited.add((nr, nc))
    
    return len(res)
  
  points = [(x, search(remainder + length * x)) for x in range(3)]
  coefs = np.polyfit(*zip(*points), 2)
  
  return round(np.polyval(coefs, steps // length))
  
print('part1', part_one(grid))
print('part2', part_two(grid))