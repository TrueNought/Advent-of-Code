def part_one(input):
  def find_reflection(pattern):
    for i in range(len(pattern)-1):
      a = i 
      b = i + 1
      while a >= 0 and b < len(pattern) and pattern[a] == pattern[b]:
        a -= 1
        b += 1
      
      if a < 0 or b >= len(pattern):
        return (a + 1, b)
      
    return (0, 0)

  patterns = [x.split('\n') for x in input.read().split('\n\n')]
  result = 0

  for hpattern in patterns:
    vpattern = [''.join(row[i] for row in hpattern) for i in range(len(hpattern[0]))]

    h1, h2 = find_reflection(hpattern)

    if h1 or h2:
      result += (h2 + h1) // 2 * 100
    else:
      v1, v2 = find_reflection(vpattern)
      result += (v2 + v1) // 2

  return result

def part_two(input):
  def find_reflection(pattern):
    for i in range(len(pattern)-1):
      a = i 
      b = i + 1
      diff = 0
      while a >= 0 and b < len(pattern):
        if pattern[a] != pattern[b]:
          diff += sum(x != y for x, y in zip(pattern[a], pattern[b]))
        a -= 1
        b += 1
      
      if diff == 1 and (a < 0 or b >= len(pattern)):
        return (a + 1, b)
      
    return (0, 0)

  patterns = [x.split('\n') for x in input.read().split('\n\n')]
  result = 0

  for hpattern in patterns:
    vpattern = [''.join(row[i] for row in hpattern) for i in range(len(hpattern[0]))]

    h1, h2 = find_reflection(hpattern)

    if h1 or h2:
      result += (h2 + h1) // 2 * 100
    else:
      v1, v2 = find_reflection(vpattern)
      result += (v2 + v1) // 2

  return result

with open('day13_input.txt', 'r') as input:
  print('part1', part_one(input))

with open('day13_input.txt', 'r') as input:
  print('part2', part_two(input))