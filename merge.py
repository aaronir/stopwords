import os
import os.path

words_set = set()
DIR = 'stopwords'

for filename in os.listdir(DIR):
    file = os.path.join(DIR, filename)
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as f:
            for word in f.readlines():
                words_set.add(word.strip())

words_set = sorted(words_set)
with open('stopwords.txt', 'w', encoding='utf-8') as f:
    for word in words_set:
        f.write(f"{word}\n")
