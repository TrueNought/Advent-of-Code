def part_one(input):
  time, distance = input.read().splitlines()
  time = [int(t) for t in time.split() if t.isdigit()]
  distance = [int(r) for r in distance.split() if r.isdigit()]

  ways = 1
  for i, rtime in enumerate(time):
    count = 0
    for htime in range(1, rtime):
      if (rtime - htime) * htime > distance[i]:
        count += 1
    ways *= count

  return ways

def part_two(input):
  time, distance = input.read().splitlines()
  _, *time = time.split()
  time = int(''.join(time))
  _, *distance = distance.split()
  distance = int(''.join(distance))
  
  ways = 0
  for htime in range(1, time):
    if (time - htime) * htime > distance:
      ways += 1

  return ways

with open('day6_input.txt', 'r') as input:
  print('part1', part_one(input))

with open('day6_input.txt', 'r') as input:
  print('part2', part_two(input))
