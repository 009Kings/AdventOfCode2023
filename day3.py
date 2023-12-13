'''
What is the sum of all of the part numbers in the engine schematic?
any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
'''
import re

sample_text = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

def find_parts(graph):
  line_len = len(re.match(r'.+\B', graph).group()) + 1
  
  parts_total = 0

  nums = re.finditer(r'[0-9]+', graph)
  for num in nums:
    left_i = num.span()[0]-1 if num.span()[0]-1 > 0 else 0
    right_i = num.span()[1]
    top_check = graph[left_i-line_len:right_i-line_len+1] if left_i - line_len > 0 else ''
    bottom_check = graph[left_i+line_len:right_i+line_len+1]
    check_area = f'{graph[left_i]}{graph[right_i]}{top_check}{bottom_check}'
    is_valid = True if re.search(r'[^\w\d\s.\n]', check_area) is not None else False
    print(f'{num.group()} is {"✅ valid" if is_valid else "⛔️ not valid"}')
    if is_valid:
      parts_total += int(num.group())
  
  return parts_total

# print(find_parts(sample_text))

# with open('day-3-input.txt', 'r') as graph:
#   print(find_parts(graph.read()))

# ================ Part Two

def find_gears(graph):
  line_len = len(re.match(r'.+\B', graph).group()) + 1
  potential_gears = re.finditer(r'[^\w|.|\n]', graph)

  gear_parts_list = []
  gear_ratio_list = []

  for potential_gear in potential_gears:
    left = potential_gear.span()[0]-1 if potential_gear.span()[0]-1 > 0 else 0
    right = potential_gear.span()[1] if potential_gear.span()[1] < len(graph) else len(graph) - 1
    top_check = graph[left-line_len:right-line_len+1] if left - line_len > 0 else '...'
    bottom_check = graph[left+line_len:right+line_len+1]
    check_area = f'{graph[left]}-{graph[right]}-{top_check}-{bottom_check}'
    # print(f'⚙️ Potential Gear: {potential_gear.group()} check area "{check_area}"')

    gear_parts = list(re.finditer(r'\d+', check_area))

    if len(gear_parts) > 1:
      gear_pair = []
      for gear_part in gear_parts:
        # print(f'\tGear_part {gear_part.group()} at index: {gear_part.span()[0]}')

        match gear_part.span()[0]:
          case 0:
            num_index = left
            # print(f"\tleft")
          case 2:
            num_index = right
            # print(f"\tright")
          case 4:
            num_index = left - line_len
            # print(f"\ttop left")
          case 5:
            num_index = left + 1 - line_len
            # print(f"\ttop middle")
          case 6:
            num_index = right - line_len
            # print(f"\ttop right")
          case 8:
            num_index = left + line_len
            # print(f"\tbottom left")
          case 9:
            num_index = left + 1 + line_len
            # print(f"\tbottom middle")
          case 10:
            num_index = right + line_len
            # print(f"\tbottom right")

        gear_part_num = graph[num_index]
        digit_check = re.compile('\d')

        while digit_check.match(graph[num_index - 1]) != None or digit_check.match(graph[num_index + len(gear_part_num)]) != None:
          # print(f'\t\t{gear_part_num} at index {num_index}\n\t\t\tleft: {graph[num_index - 1]}, right: {graph[num_index + len(gear_part_num)]}')

          if digit_check.match(graph[num_index - 1]) != None:
            # print(f'\t\t🍂 Digit to the left')
            gear_part_num = graph[num_index - 1] + gear_part_num
            num_index -= 1
          if digit_check.match(graph[num_index + len(gear_part_num)]) != None:
            # print(f'\t\t🐸 Digit to the right')
            gear_part_num = gear_part_num + graph[num_index + len(gear_part_num)]
        
        gear_pair.append(gear_part_num)
      
      gear_ratio_list.append(int(gear_pair[0]) * int(gear_pair[1]))
  
  sum_of_gear_parts=0
  for i in range(len(gear_ratio_list)):
    sum_of_gear_parts += gear_ratio_list[i]

  # print(f'first two gear parts {gear_parts_list[0]} and {gear_parts_list[1]}')
  print(f'Sum = {sum_of_gear_parts}')


# print(find_gears(sample_text))

with open('day-3-input.txt', 'r') as graph:
  print(find_gears(graph.read()))