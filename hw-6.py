# [12, 3, 4, 10] => [10, 12, 3, 4]
my_list = [12, 3, 4, 10]

# [1] => [1]
# my_list = [1]

# [] => []
# my_list = []

# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
# my_list = [12, 3, 4, 10, 8]

if len(my_list):
    removed_num = my_list.pop()
    my_list.insert(0, removed_num)


print('my_list ===>', my_list)
