from collections import deque

def energize(r, c, chr, chc, grid):
  visited = set()
  q = deque([(r, c, chr, chc)])
  energized = set()

  while q:
    r, c, chr, chc = q.popleft()
    r += chr
    c += chc
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
      continue
    
    if (r, c) not in energized:
      energized.add((r, c))

    curr = grid[r][c]

    if (curr == '.' or (curr == '-' and chr == 0) or (curr == '|' and chc == 0)) and (r, c, chr, chc) not in visited:
      q.append((r, c, chr, chc))
      visited.add((r, c, chr, chc))

    elif curr == "/" and (r, c, -chc, -chr) not in visited:
      visited.add((r, c, -chc, -chr))
      q.append((r, c, -chc, -chr))
    
    elif curr == "\\" and (r, c, chc, chr) not in visited:
      visited.add((r, c, chc, chr))
      q.append((r, c, chc, chr))

    elif curr == '-':
      for chr, chc in [(0, -1), (0, 1)]:
        if (r, c, chr, chc) not in visited:
          q.append((r, c, chr, chc))
          visited.add((r, c, chr, chc))

    else:
      for chr, chc in [(-1, 0), (1, 0)]:
        if (r, c, chr, chc) not in visited:
          q.append((r, c, chr, chc))
          visited.add((r, c, chr, chc))

  return len(energized)

def part_one(input):
  grid = input.read().splitlines()
  return energize(0, -1, 0, 1, grid)

with open('day16_input.txt', 'r') as input:
  print('part1', part_one(input))