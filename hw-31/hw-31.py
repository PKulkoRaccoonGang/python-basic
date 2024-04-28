import codecs
import re


def read_html_file(html_file: str) -> str:
    """Read the content of an HTML file and return it as a string."""
    with codecs.open(html_file, 'r', 'utf-8') as file:
        return file.read()


def remove_html_tags(text: str) -> str:
    """Remove HTML tags from a string and return the cleaned text."""
    return re.sub(r'<[^>]*>', '', text)


def remove_spaces(text: str) -> str:
    """Remove spaces from a string and return the cleaned text."""
    return text.replace(' ', '')


def remove_empty_lines(text: str) -> str:
    """Remove empty lines from a string and return the cleaned text."""
    lines = text.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return '\n'.join(cleaned_lines)


def save_text_to_file(text: str, result_file: str = 'cleaned.txt') -> None:
    """Save a string to a file."""
    with open(result_file, 'w', encoding='utf-8') as result:
        result.write(text)


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    """Remove HTML tags from an HTML file and save the cleaned text to a new file."""
    html = read_html_file(html_file)
    text = remove_html_tags(html)
    text = remove_spaces(text)
    cleaned_text = remove_empty_lines(text)
    save_text_to_file(cleaned_text, result_file)


delete_html_tags('draft.html')
