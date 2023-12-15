from collections import defaultdict

def part_one(input):
  hands = input.read().splitlines()

  ref = {
  'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10
  }

  def sort_hand(hand):
    return [ref[value] if (value in ref) else int(value) for value in hand]

  def categorize_hand(h):
    ref = defaultdict(int)
    for c in h:
      ref[c] += 1

    if 5 in ref.values():
      return 7
    elif 4 in ref.values():
      return 6
    elif 3 in ref.values() and 2 in ref.values():
      return 5
    elif 3 in ref.values():
      return 4
    elif list(ref.values()).count(2) == 2:
      return 3
    elif 2 in ref.values():
      return 2
    else:
      return 1

  result = []

  for hand in hands:
    h, bid = hand.split(' ')
    bid = int(bid)
    result.append((categorize_hand(h), h, bid))
  
  result = sorted(result, key=lambda x: (x[0], sort_hand(x[1])))
  winnings = 0
  rank = 1
   
  for _, _, bid in result:
    winnings += bid * rank 
    rank += 1

  return winnings

def part_two(input):
  hands = input.read().splitlines()

  ref = {
  'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10
  }

  def sort_hand(hand):
    return [ref[value] if (value in ref) else int(value) for value in hand]

  def categorize_hand(h):
  
    ref = defaultdict(int)
    jokers = 0
    for c in h:
      ref[c] += 1
      if c == 'J':
        jokers += 1

    if 5 in ref.values():
      return 7
    elif 4 in ref.values():
      if jokers:
        return 7
      return 6
    elif 3 in ref.values() and 2 in ref.values():
      if jokers:
        return 7
      return 5
    elif 3 in ref.values():
      if jokers:
        return 6
      return 4
    elif list(ref.values()).count(2) == 2:
      if jokers == 1:
        return 5
      elif jokers == 2:
        return 6
      return 3
    elif 2 in ref.values():
      if jokers:
        return 4
      return 2
    else:
      if jokers:
        return 2
      return 1

  result = []
  
  for hand in hands:
    h, bid = hand.split(' ')
    bid = int(bid)
    result.append((categorize_hand(h), h, bid))
  
  result = sorted(result, key=lambda x: (x[0], sort_hand(x[1])))
  winnings = 0
  rank = 1

  for _, _, bid in result:
    winnings += bid * rank 
    rank += 1

  return winnings

with open('day7_input.txt', 'r') as input:
  print('part1', part_one(input))

with open('day7_input.txt', 'r') as input:
  print('part2', part_two(input))