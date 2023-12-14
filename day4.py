'''
figure out which of the numbers you have appear in the list of winning numbers. The first match makes the card worth one point and each match after the first doubles the point value of that card.

'''
import re

sample_text = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
find_digits = re.compile(r'\d+')

def get_value(num):
  if num < 2:
    return num
  
  return 2 * get_value(num-1)

def find_wins(string):
  if len(string) < 2:
    return 0
  global find_digits
  colon_i = string.find(':')
  separator = string.find('|')

  winning_nums = find_digits.findall(string[colon_i + 1:separator])
  nums = find_digits.findall(string[separator + 1:])
  
  total_matches = 0

  for num in nums:
    if num in winning_nums:
      total_matches += 1
  return total_matches

def get_card_value(string):
  if len(string) < 2:
    return 0
  
  global find_digits
  colon_i = string.find(':')
  separator = string.find('|')

  winning_nums = find_digits.findall(string[colon_i + 1:separator])
  nums = find_digits.findall(string[separator + 1:])
  
  total_matches = 0

  for num in nums:
    if num in winning_nums:
      total_matches += 1

  return get_value(total_matches)


def sum_card_values(string):
  cards = string.split('\n')
  card_sum = 0

  for card in cards:
    card_sum += get_card_value(card)
    # get_card_value(card)
  
  return card_sum

def total_scratch_cards(string):
  card_strings = string.split('\n')
  cards = list({'wins': 0, 'num': 1} for i in range(len(card_strings)))
  card_sum = 0

  for i, card in enumerate(card_strings):
    if len(card) < 2:
      cards[i]['num'] = 0
    wins = find_wins(card)
    cards[i]['wins'] = wins

    # print(f'🐸 Index{i}: {cards[i]}')

    for j in range(wins):
      if i+j+1 < len(cards):
        cards[i+j+1]['num'] += 1 * cards[i]['num']

    card_sum += cards[i]['num']

  # print(cards)
  print(f'🔥 Card Sum: {card_sum}')

# print(sum_card_values(sample_text))
print(total_scratch_cards(sample_text))

# with open('day-4-input.txt', 'r') as cards:
#   print(sum_card_values(cards.read()))

with open('day-4-input.txt', 'r') as cards:
  print(total_scratch_cards(cards.read()))