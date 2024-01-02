"""
Credits to HyperNeutrino for the recursive approach used in Part 1
"""

with open('day12_input.txt', 'r') as input:
  input =  input.read().splitlines()

def part_one(input):
  def combs(springs, nums):
    if springs == '':
      if nums == ():
        return 1
      else:
        return 0
    
    if nums == ():
      if '#' in springs:
        return 0
      else:
        return 1
    
    result = 0
    
    if springs[0] in '.?':
      result += combs(springs[1:], nums)
    
    if springs[0] in '#?':
      if len(springs) >= nums[0] and '.' not in springs[:nums[0]] and (len(springs) == nums[0] or springs[nums[0]] != '#'):
        result += combs(springs[nums[0] + 1:], nums[1:])
    
    return result
  
  total = 0
  for line in input:
    springs, nums = line.split()
    nums = tuple([int(x) for x in nums.split(',')])
    total += combs(springs, nums)
  
  return total

def part_two(input):
  dp = {}

  def combs(springs, nums):
    if springs == '':
      if nums == ():
        return 1
      else:
        return 0
    
    if nums == ():
      if '#' in springs:
        return 0
      else:
        return 1
    
    result = 0
    
    if (springs, nums) in dp:
      return dp[(springs, nums)]

    if springs[0] in '.?':
      curr = combs(springs[1:], nums)
      result += curr
    
    if springs[0] in '#?':
      if len(springs) >= nums[0] and '.' not in springs[:nums[0]] and (len(springs) == nums[0] or springs[nums[0]] != '#'):
        result += combs(springs[nums[0] + 1:], nums[1:])
    
    dp[(springs, nums)] = result
    return result
  
  total = 0
  for line in input:
    springs, nums = line.split()
    springs = '?'.join([springs] * 5)
    nums = tuple([int(x) for x in nums.split(',')] * 5)
    total += combs(springs, nums)
  
  return total

print('part1', part_one(input))
print('part2', part_two(input))