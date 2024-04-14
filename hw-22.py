from typing import List, Union


def find_unique_value(some_list: List[Union[int, float]]) -> Union[int, float, None]:
    """
    Find and return the unique value in the given list.

    Args:
    - some_list (List[Union[int, float]]): A list of integers or floats.

    Returns:
    - Union[int, float, None]: The unique value, or None if no unique value is found.
    """
    single_count = 1
    for number in some_list:
        if some_list.count(number) == single_count:
            return number
    return None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print('ОК')
