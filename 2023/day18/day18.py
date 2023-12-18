"""
Shoelace Theorem to find the area based on coordinates, then rearrange Pick's Theorem to obtain number of interior points. Add interior points to number of points alongside the edge of the trench to obtain how much lava it can hold.
"""

with open('day18_input.txt') as input:
  input = input.read().splitlines()

def part_one(input):
  points = [(0, 0)]
  ref = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

  boundary_points = 0
  for line in input:
    d, count, _ = [int(x) if x.isdigit() else x for x in line.split()]
    dx, dy = ref[d]
    x, y = points[-1]
    points.append((x + dx * count, y + dy * count))
    boundary_points += count

  area = 0
  for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    area += x1 * y2 - y1 * x2

  area = abs(area) // 2
  interior_points = area - boundary_points // 2 + 1
  return interior_points + boundary_points

def part_two(input):
  x = y = 0
  points = [(0, 0)]
  ref = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
  dir = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

  boundary_points = 0
  for line in input:
    _, _, color = line.split()
    d = dir[color[-2]]
    count = int(color[2:-2], 16)
    dx, dy = ref[d]
    x, y = points[-1]
    points.append((x + dx * count, y + dy * count))
    boundary_points += count

  area = 0
  for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    area += x1 * y2 - y1 * x2

  area = abs(area) // 2
  interior_points = area - boundary_points // 2 + 1
  return interior_points + boundary_points
  
print('part1', part_one(input))
print('part2', part_two(input))