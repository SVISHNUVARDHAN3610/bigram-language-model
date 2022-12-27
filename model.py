import nltk
import random
from collections import Counter
from nltk import bigrams,trigrams
from nltk.corpus import brown
nltk.download("brown")
sentences = brown.sents()

class Language_model:
  def __init__(self,sentances):
    self.count = 0
    self.tri   = []
    self.word  = []
    self.tokens   = self.processing(sentances)
    self.bigram  = self.bigrams(self.tokens)
    self.trigram  = self.trigrams(self.tokens)
  def processing(self,sentance):
    words = []
    tokens = []
    for sent in sentance:
      word = [word.lower() for word in sent if word.isalpha()]
      words.append(word)
    for i in range(len(words)):
      for word in words[i]:
        tokens.append(word)
    return tokens
  def bigrams(self,tokens):
    tokens = list(bigrams(tokens))
    return tokens
  def trigrams(self,tokens):
    tokens = list(trigrams(tokens))
    return tokens
  def prob(self):
    pass
  def model1(self,sentances,input):
    input    = input.split()
    input    = list(bigrams(input))[0]
    count    = 0
    for i in range(len(self.bigram)):
      if input==self.bigram[i]:
        count = count+1
        idx   = i+1
        word  = self.bigram[i]
        next  = self.bigram[i+1]
        final = [word[0],word[1],next[1]]
        final = list(trigrams(final))
        self.tri.append(final)
    self.count = count
  def model2(self,sentances,input):
    self.model1(sentances,input)
    for i in range(len(self.tri)):
      for j in range(len(self.trigram)):
        if self.tri[i][0]==self.trigram[j]:
          self.word.append(self.trigram[j][2])
    return self.word
  def prob(self,sentances,input):
    self.model2(sentances,input)
    count = Counter(self.word)
    count_keys = list(count.keys())
    count_values = list((count.values()))
    probility = []
    for i in range(len(count_keys)):
      prob = count_values[i]/self.count
      probility.append(prob)
    for i in range(len(probility)):
      if probility[i]==max(probility):
        x = i
        break
    return count_keys,probility,count_keys[x]

model = Language_model(sentences)
line = "force it"
words,prob,word = model.prob(sentences,line)
print(line +" "+ word)
