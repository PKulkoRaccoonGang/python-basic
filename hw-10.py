# _ => True
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import string
import keyword

user_variable_name = input('Enter a variable name: ')

double_underline_count = user_variable_name.count('__')
has_invalid_chars = any((char in string.punctuation and char != '_') for char in user_variable_name)
has_spaces = any(char.isspace() for char in user_variable_name)
has_reserved_keywords = user_variable_name in keyword.kwlist

if (not user_variable_name[0].isdigit()
        and not user_variable_name != user_variable_name.lower()
        and not has_invalid_chars
        and not has_spaces
        and not has_reserved_keywords and not double_underline_count):
    print(True)
else:
    print(False)
