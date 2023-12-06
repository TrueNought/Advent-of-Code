def part_one(input):
  seeds, *maps = input.read().split('\n\n')
  seeds = [int(s) for s in seeds.split() if s.isdigit()]

  for m in maps:
    _, *m = m.splitlines()
    m = [x.split() for x in m]
    m = [(int(x[0]), int(x[1]), int(x[2])) for x in m]
    m = [(x[1], x[1] + x[2] - 1, x[0] - x[1]) for x in m]

    def convert(s):
      for start, end, change in m:
        if start <= s <= end:
          return s + change 
      return s 
    
    seeds = [convert(s) for s in seeds]

  return min(seeds)

with open('day5_input.txt', 'r') as input:
  print('part1', part_one(input))
  