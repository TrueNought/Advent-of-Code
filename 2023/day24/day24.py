with open('day24_input.txt') as input:
  input = input.read().splitlines()

lower = 200000000000000
upper = 400000000000000

def part_one(input):
  hailstones = []
  for line in input:
    hailstones.append(tuple(map(int, line.replace(' @ ', ', ').split(','))))

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
  for a, first in enumerate(hailstones[:-1]):
    for b, second in enumerate(hailstones[a+1:]):
      x1, y1, _, dx1, dy1, _ = first
      x2, y2, _, dx2, dy2, _ = second

      total += intersects((x1, y1, dx1, dy1), (x2, y2, dx2, dy2))

  return total

print('part1', part_one(input))