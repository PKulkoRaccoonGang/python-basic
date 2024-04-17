def string_formatter(string: str) -> str:
    """
    Formats the input string by converting it to lowercase and stripping whitespace.

    Args:
        string (str): The input string to be formatted.

    Returns:
        str: The formatted string.

    Raises:
        TypeError: If the input is not a string.
    """
    if isinstance(string, str):
        return string.lower().strip()
    else:
        raise TypeError('Input must be a string')


def popular_words(text: str, target_words: list) -> dict:
    """
    Counts the occurrences of target words in the given text.

    Args:
        text (str): The input text in which to count the words.
        target_words (list): A list of words to be counted in the text.

    Returns:
        dict: A dictionary where keys are target words and values are their counts.
    """
    words_in_text = string_formatter(text).split()
    target_words = set(string_formatter(word).strip() for word in target_words)

    word_count = {word: words_in_text.count(word) for word in target_words}

    return word_count


assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']
) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
