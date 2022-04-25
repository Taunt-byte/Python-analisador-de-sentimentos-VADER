# Em qualquer idioma existem palavras que não agregam muito sentido a frases como por exemplo: “a”, “as”, “e”, “de”, “das” e etc…
# Essas palavras na biblioteca nltk são conhecidas como StopWords.
# Deve se tambem lembrar de se retirar o sufixo e o prefixo das palavras e ficar apenas com seu radical.

import nltk
from nltk.compus import stopwords
stops = set(stopwords.words('portuguese'))

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
 
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)
wordsFiltered = []

for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)

print(wordsFiltered)
