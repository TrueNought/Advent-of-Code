from collections import deque

with open('day21_input.txt') as input:
  grid = input.read().splitlines()

def part_one(grid):
  start = [(i, j, 0) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S']
  q = deque(start)
  visited = set(start)
  curr = -1

  while q:
    r, c, d = q.popleft()
    if d == 64:
      break
    
    if d > curr:
      visited.clear()
      curr = d
    
    for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
      if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in visited:
        q.append((nr, nc, d + 1))
        visited.add((nr, nc))

  return len(visited)

print('part1', part_one(grid))