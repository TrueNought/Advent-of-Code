from collections import deque

def part_one(input):
  grid = input.read().splitlines()

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


with open('day10_input.txt', 'r') as input:
  print('part1', part_one(input))