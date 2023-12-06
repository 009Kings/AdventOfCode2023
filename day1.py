'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
'''

sample_text = 'eighthree\ntwo1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen'

digit_dic_front = {
  "o": {
    "one": 1
  },
  "t": {
    "two": 2,
    "three": 3
  },
  "f": {
    "four": 4,
    "five": 5
  },
  "s": {
    "six": 6,
    "seven": 7
  },
  "e": {
    "eight": 8
  },
  "n": {
    "nine": 9
  }
}

digit_dic_back = {
  "e": {
    "one": 1,
    "three": 3,
    "five": 5,
    "nine": 9
  },
  "o": {
    "two": 2,
  },
  "r": {
    "four": 4,
  },
  "x": {
    "six": 6,
  },
  "n" : {
    "seven": 7
  },
  "t": {
    "eight": 8
  }
}

calibration_values = []

def find_calibration_value(line):
  first_num = None
  last_num = None
  i = 0
  while i < len(line):
    if first_num == None:
      if line[i].isnumeric():
        first_num = line[i]
      if line[i] in digit_dic_front:
        for key, num in digit_dic_front[line[i]].items():
          if line[i:].startswith(key):
            first_num = str(num)
    back_i = i + 1
    if last_num == None:
      if line[-back_i].isnumeric():
        last_num = line[-back_i]
      if line[-back_i] in digit_dic_back:
        for key, num in digit_dic_back[line[-back_i]].items():
          substring = line if i == 0 else line[:-i]
          if substring.endswith(key):
            last_num = str(num)
    if first_num != None and last_num != None:
      calibration_values.append(int(first_num + last_num))
      # print(f'{line}🎄{first_num + last_num}')
      return
    i += 1

# for line in sample_text.split('\n'):
#   find_calibration_value(line)

with open('day-one-input.txt', 'r') as garbled:
  for line in garbled:
    find_calibration_value(line)

sum_of_calibration_values=0
for i in range(len(calibration_values)):
  sum_of_calibration_values += calibration_values[i]

print(sum_of_calibration_values)
