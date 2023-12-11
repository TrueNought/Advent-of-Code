def part_one(input):
  grid = input.read().splitlines()
  r_shifts = set()
  c_shifts = set(range(len(grid[0])))
  galaxies = []

  for i, row in enumerate(grid):
    if '#' not in row:
      r_shifts.add(i)
      continue 
    for j, ch in enumerate(row):
      if ch == '#':
        galaxies.append((i, j))
        if j in c_shifts:
          c_shifts.remove(j)

  length = 0

  for i in range(len(galaxies)-1):
    for j in range(i + 1, len(galaxies)):
      r_1, c_1 = galaxies[i]
      r_2, c_2 = galaxies[j]
      c_1, c_2 = min(c_1, c_2), max(c_1, c_2)

      r_shift = len(r_shifts.intersection(set(range(r_1, r_2 + 1))))
      c_shift = len(c_shifts.intersection(set(range(c_1, c_2 + 1))))

      length += r_2 - r_1 + r_shift
      length += c_2 - c_1 + c_shift

  return length

def part_two(input):
  grid = input.read().splitlines()
  r_shifts = set()
  c_shifts = set(range(len(grid[0])))
  galaxies = []

  for i, row in enumerate(grid):
    if '#' not in row:
      r_shifts.add(i)
      continue 
    for j, ch in enumerate(row):
      if ch == '#':
        galaxies.append((i, j))
        if j in c_shifts:
          c_shifts.remove(j)

  length = 0

  for i in range(len(galaxies)-1):
    for j in range(i + 1, len(galaxies)):
      r_1, c_1 = galaxies[i]
      r_2, c_2 = galaxies[j]
      c_1, c_2 = min(c_1, c_2), max(c_1, c_2)

      r_shift = len(r_shifts.intersection(set(range(r_1, r_2 + 1)))) * 999999
      c_shift = len(c_shifts.intersection(set(range(c_1, c_2 + 1)))) * 999999

      length += r_2 - r_1 + r_shift
      length += c_2 - c_1 + c_shift

  return length

with open('day11_input.txt', 'r') as input:
  print('part1', part_one(input))

with open('day11_input.txt', 'r') as input:
  print('part2', part_two(input))