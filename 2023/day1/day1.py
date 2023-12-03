import re

def get_calibration_value_part1(s):
  filtered = [c for c in s if c.isdigit()]
  return int(filtered[0] + filtered[-1])

def get_calibration_value_part2(s):
  ref = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
  }
  first = [len(s), '0']
  last = [0, '0']

  pattern = '|'.join(ref.keys())
  matches = list(re.finditer(f"(?=({pattern}))", s))
  
  if matches:
    first = [matches[0].start(), ref[matches[0].group(1)]] 
    last = [matches[-1].start(), ref[matches[-1].group(1)]]

  matches = list(re.finditer('\d', s))
  
  if matches:
    if matches[0].start() < first[0]:
      first = [matches[0].start(), matches[0].group()]
    if matches[-1].start() >= last[0]:
      last = [matches[-1].start(), matches[-1].group()]

  return int(first[1] + last[1])

if __name__ == "__main__":
  result1 = 0
  result2 = 0

  with open('day1_input.txt', 'r') as input:
    for line in input:
      result1 += get_calibration_value_part1(line.strip())
      result2 += get_calibration_value_part2(line.strip())

    print('part1', result1)
    print('part2', result2)