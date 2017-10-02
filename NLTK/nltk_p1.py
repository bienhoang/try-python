import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

example_text = "hello Mr. Smith, how are you doing today? The weather is great nad python is awesome. The sky is pipe."

print (sent_tokenize(example_text))
print (word_tokenize(example_text))

for word in word_tokenize(example_text):
    print(word)
