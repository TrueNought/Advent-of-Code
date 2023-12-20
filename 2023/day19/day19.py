with open('day19_input.txt') as input:
  input = input.read().split('\n\n')

def part_one(input):
  top, parts = [i.split('\n') for i in input]
  workflow = {}

  parts = [x[1:-1].split(',') for x in parts]
  parts = [{k: int(v) for k, v in (item.split('=') for item in p)} for p in parts]
  
  for t in top:
    name, rules = t[:-1].split('{')
    rules = rules.split(',')
    workflow[name] = ([], rules.pop())
    for r in rules:
      condition, result = r.split(':')
      p, c, n = condition[0], condition[1], int(condition[2:])
      workflow[name][0].append((p, c, n, result))
  
  def valid(part, name='in'):
    if name == 'A':
      return True
    elif name == 'R':
      return False
    
    checks, follow =  workflow[name]
    for p, eq, n, later in checks:
      if eq == '<':
        if part[p] < n:
          return valid(part, later)
      else:
        if part[p] > n:
          return valid(part, later)
        
    return valid(part, follow)
  
  total = 0
  for p in parts:
    if valid(p):
      total += sum(list(p.values()))

  return total

def part_two(input):
  top, _ = [i.split('\n') for i in input]
  workflow = {}

  for t in top:
    name, rules = t[:-1].split('{')
    rules = rules.split(',')
    workflow[name] = ([], rules.pop())
    for r in rules:
      condition, result = r.split(':')
      p, c, n = condition[0], condition[1], int(condition[2:])
      workflow[name][0].append((p, c, n, result))

  def separate(r, start, end):
    overlap = (max(r[0], start), min(r[1], end))
    left = (r[0], overlap[0])
    right = (overlap[1], r[1])
    
    if left[0] < left[1]:
      return overlap, left
    else:
      return overlap, right

  def valid(r, name='in'):
    total = 0
    if name == 'A':
      combs = 1
      for i, j in r.values():
        combs *= (j - i)
      return combs
    elif name == 'R':
      return 0
    
    checks, follow =  workflow[name]
    for p, eq, n, later in checks:
      if eq == '<':
        new, remaining = separate(r[p], 1, n)
        newr = {k: new if k == p else v for k, v in r.items()}
        r[p] = remaining
        total += valid(newr, later)
      else:
        new, remaining = separate(r[p], n + 1, 4001)
        newr = {k: new if k == p else v for k, v in r.items()}
        r[p] = remaining
        total += valid(newr, later)

    return total + valid(r, follow)

  ranges = {k: (1, 4001) for k in 'xmas'} 
  return valid(ranges)

print('part1', part_one(input))
print('part2', part_two(input))