import re
from collections import defaultdict

def get_winning_nums(card):
  matches = re.search(r':\s([\d\s]+)', card)
  return matches.group(1).split()

def get_curr_nums(card):
  matches = re.search(r'\|\s([\d\s]+)', card)
  return matches.group(1).split()

def get_wins(card):
  winning_nums = get_winning_nums(card)
  curr_nums = get_curr_nums(card)
  return len(curr_nums) - len(set(curr_nums) - set(winning_nums))

def part_one(lines):
  points = 0
  for card in lines:
    wins = get_wins(card)
    if wins > 0:
      points += 1 * (2 ** (wins - 1))
  return points

def part_two(lines):
  ref = defaultdict(int)
  for c in range(len(lines)):
    wins = get_wins(lines[c])
    ref[c] += 1
    for d in range(c+1, min(c + wins + 1, len(lines))):
      ref[d] += ref[c]
  return sum(ref.values())

with open('day4_input.txt', 'r') as input:
  lines = input.read().splitlines()
  print('part1', part_one(lines))

with open('day4_input.txt', 'r') as input:
  lines = input.read().splitlines()
  print('part2', part_two(lines))