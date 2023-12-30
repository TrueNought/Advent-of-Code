"""
Credits to HyperNeutrino for the edge contraction approach used to simplify the number of total nodes that need to be considered when finding the longest path.
"""

with open('day23_input.txt') as input:
  input = input.read().splitlines()

slopes = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def part_one(grid):
  start = (0, grid[0].index('.'))
  goal = (len(grid)-1, grid[-1].index('.'))
  
  s = [(start, 0, set())]
  longest = 0

  while s:
    (curr, steps, visited) = s.pop()
    
    if curr == goal:
      longest = max(longest, steps)
      continue

    visited.add(curr)
    r, c = curr

    if grid[r][c] in slopes:
      dr, dc = slopes[grid[r][c]]
      nr, nc = r + dr, c + dc
      if (nr, nc) not in visited:
        s.append(((nr, nc), steps + 1, set(visited)))
        continue

    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
      if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
        if (grid[nr][nc] in slopes and slopes[grid[nr][nc]] != (r-nr, c-nc)) or grid[nr][nc] == '.':
          s.append(((nr, nc), steps + 1, set(visited)))        

  return longest

def part_two(grid):
  start = (0, grid[0].index('.'))
  goal = (len(grid)-1, grid[-1].index('.'))

  points = [start, goal]
  
  for r, row in enumerate(grid):
    for c, ch in enumerate(row):
      if ch == '#':
        continue

      neighbors = 0
      for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#':
          neighbors += 1

      if neighbors >= 3:
        points.append((r, c))

  graph = {p: {} for p in points}
  
  for sr, sc in points:
    stack = [(sr, sc, 0)]
    visited = {(sr, sc)}

    while stack:
      r, c, n = stack.pop()

      if n != 0 and (r, c) in points:
        graph[(sr, sc)][(r, c)] = n
        continue

      for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in visited:
          stack.append((nr, nc, n + 1))
          visited.add((nr, nc))

  visited = set()
  def dfs(curr):
    if curr == goal:
      return 0
    
    length = float('-inf')
    visited.add(curr)

    for neighbor in graph[curr]:
      if neighbor not in visited:
        length = max(length, dfs(neighbor) + graph[curr][neighbor])
    visited.remove(curr)

    return length
  
  return dfs(start)

print('part1', part_one(input))
print('part2', part_two(input))