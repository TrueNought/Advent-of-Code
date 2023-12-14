def part_one(input):
  input = input.read().splitlines()
  rows = len(input)
  pos = [0] * len(input[0])
  load = 0

  for i, line in enumerate(input):
    for j, l in enumerate(line):
      if l == 'O':
        load += rows - pos[j]
        pos[j] += 1
      elif l == '#':
        pos[j] = i + 1

  return load

def part_two(input):
  grid = input.read().splitlines()

  def shift(grid):
    pos = [0] * len(grid[0])
    for i, line in enumerate(grid):
      for j, l in enumerate(line):
        if l == 'O':
          grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
          grid[pos[j]] = grid[pos[j]][:j] + 'O' + grid[pos[j]][j+1:]
          pos[j] += 1
        elif l == '#':
          pos[j] = i + 1
    
  visited = set(tuple(grid))
  ref = [tuple(grid)]

  cycles = 0
  while cycles < 1000000000:
    for _ in range(4):
      shift(grid)
      grid = [''.join(row[i] for row in grid)[::-1] for i in range(len(grid[0]))]
    cycles += 1
    curr = tuple(grid)
    if curr in visited:
      break
    visited.add(curr)
    ref.append(curr)

  first = ref.index(curr)
  period = cycles - first 
  idx = (1000000000 - first) % period + first

  result = list(ref[idx])
  rows = len(result[0])
  load = 0
  
  for i, line in enumerate(result):
    load += line.count('O') * (rows - i) 

  return load

with open('day14_input.txt', 'r') as input:
  print('part1', part_one(input))

with open('day14_input.txt', 'r') as input:
  print('part2', part_two(input))