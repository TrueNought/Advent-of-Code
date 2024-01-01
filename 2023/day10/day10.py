from collections import deque

with open('day10_input.txt', 'r') as input:
  input = input.read().splitlines()

def part_one(grid):
  for i in range(len(grid)):
    if 'S' in grid[i]:
      start = (i, grid[i].index('S'))

  q = deque([start])
  visited = set([start])

  while q:
    r, c = q.popleft()
    curr = grid[r][c]

    # up
    if r > 0 and curr in 'S|JL' and grid[r-1][c] in '|7F' and (r-1, c) not in visited:
      visited.add((r-1, c))
      q.append((r-1, c))

    # down
    if r < len(grid)-1 and curr in 'S|7F' and grid[r+1][c] in '|JL' and (r+1, c) not in visited:
      visited.add((r+1, c))
      q.append((r+1, c))

    # left
    if c > 0 and curr in 'S-J7' and grid[r][c-1] in '-LF' and (r, c-1) not in visited:
      visited.add((r, c-1))
      q.append((r, c-1))

    # right
    if c < len(grid[0])-1 and curr in 'S-LF' and grid[r][c+1] in '-J7' and (r, c+1) not in visited:
      visited.add((r, c+1))
      q.append((r, c+1))

  return len(visited) // 2

def part_two(grid):
  for i in range(len(grid)):
    if 'S' in grid[i]:
      start = (i, grid[i].index('S'))

  s = [start]
  visited = set([start])
  points = [(start[1], start[0])]

  while s:
    r, c = s.pop()
    curr = grid[r][c]

    if r > 0 and curr in 'S|JL' and grid[r-1][c] in '|7F' and (r-1, c) not in visited:
      visited.add((r-1, c))
      points.append((c, r-1))
      s.append((r-1, c))

    elif r < len(grid)-1 and curr in 'S|7F' and grid[r+1][c] in '|JL' and (r+1, c) not in visited:
      visited.add((r+1, c))
      points.append((c, r+1))
      s.append((r+1, c))

    elif c > 0 and curr in 'S-J7' and grid[r][c-1] in '-LF' and (r, c-1) not in visited:
      visited.add((r, c-1))
      points.append((c-1, r))
      s.append((r, c-1))

    elif c < len(grid[0])-1 and curr in 'S-LF' and grid[r][c+1] in '-J7' and (r, c+1) not in visited:
      visited.add((r, c+1))
      points.append((c+1, r))
      s.append((r, c+1))

  area = 0
  for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % len(points)]
    area += x1 * y2 - y1 * x2
  area = abs(area) // 2

  return area + 1 - len(points) // 2

print('part1', part_one(input))
print('part2', part_two(input))