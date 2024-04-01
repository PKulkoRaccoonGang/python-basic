# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

list_of_numbers = [0, 1, 7, 2, 4, 8]
# list_of_numbers = [1, 3, 5]
# list_of_numbers = [6]
# list_of_numbers = []

if list_of_numbers:
    sum_even_idx = sum(list_of_numbers[::2])
    result = sum_even_idx * list_of_numbers[-1]
    print(f'Result: {result}')
else:
    print(f'Result: {len(list_of_numbers)}')
