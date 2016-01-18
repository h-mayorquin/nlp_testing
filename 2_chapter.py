import nltk
fileids = nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
emma_raw = nltk.corpus.gutenberg.raw('austen-emma.txt')
print('Emma length', len(emma))

espa = nltk.corpus.cess_esp
espa_raw = espa.raw()
espa_words = espa.words()
espa_book = nltk.text.Text(espa_words)
espa_freq = nltk.FreqDist(espa.words())
