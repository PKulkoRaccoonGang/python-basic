# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

letters_range = input('Enter your string: ')

founded_indexes = []

for letter in letters_range.split('-'):
    idx = string.ascii_letters.index(letter)
    founded_indexes.append(idx)

result = string.ascii_letters[founded_indexes[0]:founded_indexes[1] + 1]

print(f'RESULT: {result}')
