'''
find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number.

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
'''
import re

sample_text = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''
find_digits = re.compile(r'\d+')
seed_list = []

class Map:
  def __init__(self, source_name, destination_name, destination, source, range):
    self.source_name = source_name
    self.destination_name = destination_name
    self.source = source
    self.destination = destination
    self.range = range

  def __str__(self):
    return(f'source: {self.source}, destination: {self.destination}, range: {self.range}')
  
  def __repr__(self):
    return(f'<{self.source_name} to {self.destination_name}--source: {self.source}, destination: {self.destination}, range: {self.range}>')
  
  def to_destination(self, source_num):
    if source_num >= self.source and source_num < self.source + self.range:
      diff = source_num - self.source
      conversion = self.destination + diff
      return conversion
    return None

# parse string
current_map = []
maps = {}

# with open('day-5-input.txt', 'r') as stupid:
#   for line in stupid:
#     if len(line) < 2:
#       continue
#     if 'seeds' in line:
#       seed_list = [int(seed) for seed in find_digits.findall(line)]
#     elif 'map' in line:
#       current_map = re.split('-', line[:-5])
#       maps[line[:-5]] = []
#     else:
#       maps[f'{current_map[0]}-{current_map[1]}-{current_map[2]}'].append(Map(current_map[0], current_map[2], *[int(num) for num in find_digits.findall(line)]))

# for line in iter(sample_text.splitlines()):
#   if len(line) < 2:
#     continue
#   if 'seeds' in line:
#     seed_list = [int(seed) for seed in find_digits.findall(line)]
#   elif 'map' in line:
#     current_map = re.split('-', line[:-5])
#     maps[line[:-5]] = []
#   else:
#     maps[f'{current_map[0]}-{current_map[1]}-{current_map[2]}'].append(Map(current_map[0], current_map[2], *[int(num) for num in find_digits.findall(line)]))

# current_conversions = [0 for seed in seed_list]

# for i, seed in enumerate(seed_list):
#   for key, conversion_type in maps.items():
#     for conversion in conversion_type:
#       if key[:4] == 'seed':
#         result = conversion.to_destination(seed)
#         if result != None:
#           current_conversions[i] = result
#           break
#         else:
#           current_conversions[i] = seed
#       else:
#         result = conversion.to_destination(current_conversions[i])
#         if result != None:
#           current_conversions[i] = result
#           break

# print(min(current_conversions))

#  ================= Pt. 2
for line in iter(sample_text.splitlines()):
  if len(line) < 2:
    continue
  if 'seeds' in line:
    seed_list = [int(seed) for seed in find_digits.findall(line)]
  elif 'map' in line:
    current_map = re.split('-', line[:-5])
    maps[line[:-5]] = []
  else:
    maps[f'{current_map[0]}-{current_map[1]}-{current_map[2]}'].append(Map(current_map[0], current_map[2], *[int(num) for num in find_digits.findall(line)]))


# check seeds

current_conversions = [0 for seed in seed_list]

for i, seed in enumerate(seed_list):
  for key, conversion_type in maps.items():
    for conversion in conversion_type:
      if key[:4] == 'seed':
        result = conversion.to_destination(seed)
        if result != None:
          current_conversions[i] = result
          break
        else:
          current_conversions[i] = seed
      else:
        result = conversion.to_destination(current_conversions[i])
        if result != None:
          current_conversions[i] = result
          break

# print(min(current_conversions))
