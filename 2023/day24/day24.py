"""
Part 1: Cramer's rule to find solution for each pair of hailstones
Part 2: 6 unkowns (x, y, z, dx, dy, d z) requires 6 equations. Tried np.linalg.solve with a system of 6 equations (2 pairs, 3 equations per pair with XY XZ YZ) but had slight floating point inaccuracy. Sympy worked without any issues
"""

import sympy as sp

with open('day24_input.txt') as input:
  input = input.read().splitlines()

lower = 200000000000000
upper = 400000000000000

def part_one(input):
  hailstones = []
  for line in input:
    a = tuple(map(int, line.replace(' @ ', ', ').split(',')))
    hailstones.append(a[:2] + a[3:5])

  def intersects(a, b):
    x1, y1, dx1, dy1 = a
    x2, y2, dx2, dy2 = b

    a1, b1, c1 = dy1/dx1, -1, (dy1/dx1) * x1 - y1
    a2, b2, c2 = dy2/dx2, -1, (dy2/dx2) * x2 - y2
    d = a1 * b2 - a2 * b1

    if d == 0:
      return 0
    
    x = (c1 * b2 - c2 * b1) / d
    y = (a1 * c2 - a2 * c1) / d

    if (x1 < x and dx1 < 0) or (x1 > x and dx1 > 0) or (x2 < x and dx2 < 0) or (x2 > x and dx2 > 0):
      return 0
 
    if lower <= x <= upper and lower <= y <= upper:
      return 1

    return 0
  
  total = 0
  for i in range(len(hailstones) - 1):
    for j in range(i + 1, len(hailstones)):
      total += intersects(hailstones[i], hailstones[j])

  return total

def part_two(input):
  hailstones = []
  for line in input:
    hailstones.append(tuple(map(int, line.replace(' @ ', ', ').split(','))))

  x, y, z, dx, dy, dz = sp.symbols("x, y, z, dx, dy, dz")
  equations = []

  for x1, y1, z1, dx1, dy1, dz1 in hailstones[:3]:
    equations.append((x - x1) * (dy1 - dy) - (y - y1) * (dx1 - dx))
    equations.append((y - y1) * (dz1 - dz) - (z - z1) * (dy1 - dy))

  res = sp.solve(equations)
  res = [r for r in res if all(v.is_integer for v in r.values())]
  res = res[0]
  
  return res[x] + res[y] + res[z]

print('part1', part_one(input))
print('part2', part_two(input))