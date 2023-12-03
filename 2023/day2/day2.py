import re

red_cubes = 12
green_cubes = 13
blue_cubes = 14

def get_id(s):
  match = re.search(r'Game (\d+):', s)
  return int(match.group(1))

def highest_color(s, color):
  matches = re.findall(rf'(\d+) {color}', s)
  return max([int(match) for match in matches])

def is_possible(s):
  return highest_color(s, 'red') <= red_cubes and highest_color(s, 'green') <= green_cubes and highest_color(s, 'blue') <= blue_cubes

def product_fewest_cubes(s):
  return highest_color(s, 'red') * highest_color(s, 'green') * highest_color(s, 'blue')

if __name__ == "__main__":
  with open('day2_input.txt', 'r') as input:
    result1 = 0
    result2 = 0
    for game in input:
      if is_possible(game):
        result1 += get_id(game)
      result2 += product_fewest_cubes(game)

    print('part1', result1)
    print('part2', result2)
