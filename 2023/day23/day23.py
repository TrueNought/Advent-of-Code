with open('day23_input.txt') as input:
  input = input.read().splitlines()

slopes = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def part_one(grid):
  longest = 0
  start = (0, next(j for j in range(len(grid[0])) if grid[0][j] == '.'))
  goal = (len(grid)-1, next(j for j in range(len(grid[-1])) if grid[-1][j] == '.'))
  
  s = [(start, 0, set())]

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
  longest = 0
  start = (0, next(j for j in range(len(grid[0])) if grid[0][j] == '.'))
  goal = (len(grid)-1, next(j for j in range(len(grid[-1])) if grid[-1][j] == '.'))
  
  s = [(start, 0, set())]

  while s:
    (curr, steps, visited) = s.pop()
    print(curr)
    
    if curr == goal:
      longest = max(longest, steps)
      print('got to goal with', longest)
      continue

    visited.add(curr)
    r, c = curr

    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
      if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] != '#':
          s.append(((nr, nc), steps + 1, set(visited)))        

  return longest

# print('part1', part_one(input))
print('part2', part_two(input))