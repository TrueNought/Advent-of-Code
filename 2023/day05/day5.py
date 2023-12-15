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

def part_two(input):
  seeds, *maps = input.read().split('\n\n')
  seeds = [int(s) for s in seeds.split() if s.isdigit()]
  seeds = [[seeds[i], seeds[i] + seeds[i+1]] for i in range(0, len(seeds), 2)]
  
  for m in maps:
    _, *m = m.splitlines()
    m = [x.split() for x in m]
    m = [(int(x[0]), int(x[1]), int(x[2])) for x in m]
    m = [(x[1], x[1] + x[2], x[0] - x[1]) for x in m]

    new_seeds = []    
    for seed in seeds:
      for start, end, change in m:
        if start >= seed[1] or end <= seed[0]:
          continue

        overlap = [max(seed[0], start), min(seed[1], end)]
        left = [seed[0], overlap[0]]
        right = [overlap[1], seed[1]]

        if left[0] < left[1]:
          seeds.append(left)
        if right[0] < right[1]:
          seeds.append(right)

        new_seeds.append([overlap[0] + change, overlap[1] + change])
        break
      else:
        new_seeds.append(seed)
    seeds = new_seeds   
  return min([x[0] for x in seeds])

if __name__ == "__main__":
  with open('day5_input.txt', 'r') as input:
    print('part1', part_one(input))

  with open('day5_input.txt', 'r') as input:
    print('part2', part_two(input))
  