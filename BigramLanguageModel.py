"""
    Author: Helana Brock
    Date: Tuesday, Oct. 12th, 2021

    Program counts the frequency of co-occurences in the reuters dataset and
    transforms those counts to probabilites. It then asks for input and returns
    the input plus the next word.

    Even though it adds the next word and "completes" the sentence how the lab
    wants, these sentences don't always make sense and could still be considered
    unfinished.
"""


from collections import Counter, defaultdict
from nltk.corpus import reuters
from nltk import bigrams
import random


model = defaultdict(lambda: defaultdict(lambda: 0))

for sentence in reuters.sents():
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        model[w1][w2] += 1

for w1 in model:
    total_count = float(sum(model[w1].values()))
    for w2 in model[w1]:
        model[w1][w2] /= total_count

text = input("Hi there! Please enter an incomplete sentence and I can help you finish it!\n")

print("I finished your sentence! Here are some options…")

word_dict = model[text.lower().split()[-1]]

k = Counter(word_dict)
high = k.most_common(3)

for i in high:
    print(text + " " + str(i[0]) + ".")
