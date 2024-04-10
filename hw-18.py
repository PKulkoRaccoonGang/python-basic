from typing import Optional


def second_index(text: str, some_str: str) -> Optional[int]:
    first_occurrence = text.find(some_str)
    if first_occurrence == -1:
        return None
    second_occurrence = text.find(some_str, first_occurrence + 1)
    if second_occurrence == -1:
        return None
    return second_occurrence


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')