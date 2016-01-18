import nltk
import nltk.book as book
import string

# Let's do frequency analysis for book 1 (Moby Dicke)
text1 = book.text1
concatenated_text = ''.join(text1)
dis = nltk.FreqDist(concatenated_text)
# dis.plot()

# Now we can get the bigrams
aux = nltk.bigrams(text1)
bigram_frequency = nltk.FreqDist(aux)
print('Most common bigrams')
print(bigram_frequency.most_common(20))  # Now we print the most common bigrams

