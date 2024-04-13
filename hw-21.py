def is_palindrome(text: str) -> bool:
    """
    Checks if a text is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward,
    ignoring spaces, punctuation, and capitalization.

    Args:
    text (str): The input text to check.

    Returns:
    bool: True if the text is a palindrome, False otherwise.
    """
    formatted_string = ''.join([char.lower() for char in text if char.isalnum()])
    return formatted_string == formatted_string[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print('ОК')
