integer_list = [1, 2, 3, 4, 5, 6]
# integer_list = [1, 2, 3]
# integer_list = [1, 2, 3, 4, 5]
# integer_list = [1]
# integer_list = []

is_divisible_in_half = len(integer_list) % 2 == 0

if is_divisible_in_half:
    start_half = integer_list[:len(integer_list) // 2]
    finish_half = integer_list[len(integer_list) // 2:]
else:
    start_half = integer_list[:len(integer_list) // 2 + 1]
    finish_half = integer_list[len(integer_list) // 2 + 1:]

split_list = [start_half, finish_half]

print(split_list)
