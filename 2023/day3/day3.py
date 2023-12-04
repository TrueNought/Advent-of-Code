import re

def adjacent_to_symbol(lines, r, rows, cols, start, end):
  checks = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]

  for c in range(start, end):
    for i, j in checks:
      new_r = r + i
      new_c = c + j
      if 0 <= new_r < rows and 0 <= new_c < cols and re.match(r'[^\d.]', lines[new_r][new_c]):
        return True
  
  return False

def match_numbers(s):
  matches = re.finditer(r'\d+', s)
  return [(int(match.group()), match.start(), match.end()) for match in matches]

def adjacent_to_gear(start, end, gear_c):
  if start <= gear_c + 1 and end >= gear_c - 1:
    return True
  return False

def get_ratio(lines, r, c):
  parts = []

  for i in range(r - 1, r + 2):
    ref = match_numbers(lines[i])
    for n in ref:
      if adjacent_to_gear(n[1], n[2]-1, c):
        parts.append(n[0])
        if len(parts) > 2:
          return 0
        
  if len(parts) == 2:
    return parts[0] * parts[1]
  else:
    return 0

def part_one(lines):
  result = 0
  for r in range(rows):
      for n in match_numbers(lines[r]):
        if adjacent_to_symbol(lines, r, rows, cols, n[1], n[2]):
          result += n[0]
  return result
 
def part_two(lines):
  result = 0
  for r in range(rows):
      for c in range(cols):
        if lines[r][c] == '*':
          result += get_ratio(lines, r, c)
  return result 

if __name__ == "__main__":
  result2 = 0

  with open('day3_input.txt', 'r') as input:
    lines = input.read().splitlines()
    rows = len(lines)
    cols = len(lines[0])

    print('part1', part_one(lines)) 
    print('part2', part_two(lines))