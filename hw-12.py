# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
import string

MAX_HASHTAG_LENGTH = 140

hashtag_text = input('Enter a hashtag value: ')
hashtag = ''.join(hashtag_text.title().split())
hashtag = ''.join(char for char in hashtag if char not in string.punctuation)

if len(hashtag) > MAX_HASHTAG_LENGTH:
    hashtag = hashtag[:MAX_HASHTAG_LENGTH]

print(f'#{hashtag}')
