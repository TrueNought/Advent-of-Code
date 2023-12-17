from collections import deque

with open('day16_input.txt', 'r') as input:
  grid = input.read().splitlines()

def energize(r, c, chr, chc):
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

def part_one():
  return energize(0, -1, 0, 1)

def part_two():
  largest = 0

  for r in range(len(grid)):
    largest = max(largest, energize(r, -1, 0, 1))
    largest = max(largest, energize(r, len(grid[0]), 0, -1))

  for c in range(len(grid[0])):
    largest = max(largest, energize(-1, c, 1, 0))
    largest = max(largest, energize(len(grid), c, -1, 0))

  return largest

print('part1', part_one())
print('part2', part_two())