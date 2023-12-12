def part_one(input):
  springs = input.read().splitlines()

  def combs(s):
    if '?' not in s:
      return [s]
    
    i = s.index('?')
    result = []
    for ch in ('#', '.'):
      new = s[:i] + ch + s[i+1:]
      result.extend(combs(new))

    return result

  total = 0
  for spring in springs:
    group, order = spring.split()
    order = [int(x) for x in order.split(',')]
    
    for comb in combs(group):
      if order == [len(x) for x in comb.split('.') if x]:
        total += 1

  return total

with open('day12_input.txt', 'r') as input:
  print('part1', part_one(input))
