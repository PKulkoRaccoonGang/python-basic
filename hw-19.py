def create_multiples(multiplicity_number: int) -> list:
    """
    Generate a list of numbers that are multiples of the given number from 1 to 100.

    :param multiplicity_number: The number whose multiples are checked.
    :return: List of numbers that are multiples of the given number.
    """
    return [i for i in range(1, 101) if i % multiplicity_number == 0]


def common_elements() -> set:
    """
    Find the common elements in the lists of numbers that are multiples of 3 and 5 from 1 to 100.

    :return: Set of common elements.
    """
    multiples_of_3 = create_multiples(3)
    multiples_of_5 = create_multiples(5)

    common_set = set(multiples_of_3) & set(multiples_of_5)

    return common_set


result = common_elements()

print(f'Result: {result}')
