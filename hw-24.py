from typing import Union


def difference(*numbers: Union[int, float]) -> Union[int, float]:
    """
    Calculate the difference between the maximum and minimum values in a list of numbers.

    Args:
    *numbers: A variable number of integers or floats.

    Returns:
    float: The difference between the maximum and minimum values in the input numbers, rounded to 2 decimal places.
    If no numbers are provided, returns 0.
    """
    if not numbers:
        return 0

    difference_value = max(numbers) - min(numbers)
    return round(difference_value, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
