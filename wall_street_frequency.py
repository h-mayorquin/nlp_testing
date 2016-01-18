import numpy as np
import matplotlib.pyplot as plt
from nltk.book import text7 as text
import nltk
import string


number_of_words = len(text)
print('Number of words', number_of_words)
print(text[0:10])

concatenated_text = ' '.join(text)
text_lowercase = [letter.lower() for letter in concatenated_text]
number_of_letters = len(text_lowercase)
print('Number of letters', number_of_letters)

## Bigrams
# First we count them
bigrams = nltk.bigrams(text_lowercase)
number_of_bigrams = len(list(bigrams))
print('Number of bigrams', number_of_bigrams)

# Then we transform their frequency and remove the spaces
bigrams = nltk.bigrams(text_lowercase)
bigrams_frequency = nltk.FreqDist(bigrams)
bigrams_without_space = [key for key in bigrams_frequency.keys() if ' ' not in key]
bigrams_without_space2 = [key for key in bigrams_frequency if ' ' not in key]
bigrams_without_space_dic = {key:item for key,item in bigrams_frequency.items() if ' ' not in key}


# Another route
bigrams = nltk.bigrams(text_lowercase)
bigrams_without_space = {bigram for bigram in bigrams if ' ' not in bigram}
bigrams_frequency = nltk.FreqDist(bigrams_without_space)

