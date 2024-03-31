# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

# numbers = [0, 1, 0, 12, 3]
# numbers = [0]
# numbers = [1, 0, 13, 0, 0, 0, 5]
numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

zero_count = numbers.count(0)

numbers = [number for number in numbers if number != 0]

numbers += [0] * zero_count

print(f'Sorted numbers: {numbers}')
