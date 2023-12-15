def part_one(input):
  lines = input.read().splitlines()
  result = 0

  for line in lines:
    line = [int(x) for x in line.split()]
    ref = []

    while not all(c == 0 for c in line):
      for i in range(len(line) - 1):
        line[i] = line[i+1] - line[i]
      ref.append(line[-1])
      line = line[:-1]
    result += sum(ref)

  return result

def part_two(input):
  lines = input.read().splitlines()
  result = 0

  for line in lines:
    line = [int(x) for x in line.split()][::-1]
    ref = []

    while not all(c == 0 for c in line):
      for i in range(len(line) - 1):
        line[i] = line[i+1] - line[i]
      ref.append(line[-1])
      line = line[:-1]
    result += sum(ref)

  return result


with open('day9_input.txt', 'r') as input:
  print('part1', part_one(input))

with open('day9_input.txt', 'r') as input:
  print('part2', part_two(input))
  