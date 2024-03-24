import random

random_length = random.randint(3, 10)
random_numbers = [random.randint(3, 10) for _ in range(random_length)]

print('random_numbers ==>', random_numbers)
new_list = [random_numbers[0], random_numbers[2], random_numbers[-2]]
print('new_list ===>', new_list)
