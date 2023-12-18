import heapq

with open('day17_input.txt') as input:
  grid = [[int(ch) for ch in s] for s in input.read().splitlines()]

def part_one():
  checks = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  rows = len(grid)
  cols = len(grid[0])
  pq = [(0, 0, 0, 0, 1, 1), (0, 0, 0, 1, 0, 1)]
  visited = set()

  while pq:
    cost, r, c, dr, dc, count = heapq.heappop(pq)

    if (r, c, dr, dc, count) in visited:
      continue

    visited.add((r, c, dr, dc, count))
    nr = r + dr
    nc = c + dc

    if not (0 <= nr < rows and 0 <= nc < cols):
      continue
    
    ncost = cost + grid[nr][nc]

    if count <= 3 and (nr, nc) == (rows-1, cols-1):
      return ncost

    for di, dj in checks:
      if (dr + di, dc + dj) == (0, 0):
        continue
      ncount = count + 1 if (di, dj) == (dr, dc) else 1
      if ncount > 3:
        continue
      heapq.heappush(pq, (ncost, nr, nc, di, dj, ncount))

def part_two():
  checks = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  rows = len(grid)
  cols = len(grid[0])
  pq = [(0, 0, 0, 0, 1, 1), (0, 0, 0, 1, 0, 1)]
  visited = set()

  while pq:
    cost, r, c, dr, dc, count = heapq.heappop(pq)

    if (r, c, dr, dc, count) in visited:
      continue

    visited.add((r, c, dr, dc, count))
    nr = r + dr
    nc = c + dc

    if not (0 <= nr < rows and 0 <= nc < cols):
      continue
    
    ncost = cost + grid[nr][nc]

    if 4 <= count <= 10 and (nr, nc) == (rows-1, cols-1):
      return ncost

    for di, dj in checks:
      if (dr + di, dc + dj) == (0, 0):
        continue
      ncount = count + 1 if (di, dj) == (dr, dc) else 1
      if ((dr, dc) != (di, dj) and count < 4) or ncount > 10:
        continue
      heapq.heappush(pq, (ncost, nr, nc, di, dj, ncount))

print('part1', part_one())
print('part2', part_two())