'''
PART ONE
Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

PART TWO
For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
'''

sample_text = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'

import re
# ============= PART ONE
color_limit = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def is_legit(handful):
  for key, limit in color_limit.items():
    matches = re.findall(fr'\d*(?=\s{key})', handful)
    for match in matches:
      if match != '' and int(match) > limit:
        return False
  return True

def find_games(handful_groups):
  print(f'🔥{handful_groups}', end='\n')

  game_num = re.search('(?<=(Game)\s)\d*', handful_groups).group()

  to_add = is_legit(handful_groups[6+len(game_num):])
  
  print(f'Game {game_num} {"⛔️ should not " if to_add == False else "✅ should "}be added\n')
  # check num and string
  return (to_add, int(game_num))

game_sum = 0

# for game in sample_text.split('\n'):
#   results = find_games(game)
#   if results[0]:
#     game_sum += results[1]

# with open('day-2-input.txt', 'r') as game_list:
#   for game in game_list:
#     results = find_games(game)
#     if results[0] == True:
#       game_sum += results[1]
# print(game_sum)

# ============= PART TWO

def find_color_power(handful_groups):
  # print(f'🔥{handful_groups}', end='\n')

  color_mins = {
    'red': 0,
    'green': 0,
    'blue': 0,
  }

  for key in color_mins.keys():
    matches = re.findall(fr'\d*(?=\s{key})', handful_groups)
    for match in matches:
      if match != '' and int(match) > color_mins[key]:
        color_mins[key] = int(match)
  
  power = color_mins['red'] * color_mins['green'] * color_mins['blue']
  return power

power_sum = 0

# for game in sample_text.split('\n'):
#   power_sum += find_color_power(game)

with open('day-2-input.txt', 'r') as game_list:
  for game in game_list:
    power_sum += find_color_power(game)

print(power_sum)