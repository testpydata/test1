import os
import re

datasets = {i: os.listdir("./dataset/" + i) for i in os.listdir("./dataset")}
print("datasets:\n{0}".format(datasets))

data = dict()

for dirs in datasets:
    for i in datasets.get(dirs):
        if os.path.isfile(os.path.join("./dataset/", dirs, i)):
            with open(os.path.join("./dataset/", dirs, i), 'r', encoding = "windows 1252") as fp:
                data[os.path.join("./dataset", dirs, i)] = re.split(r'([\W\n])+', fp.read())

print("\n\ndata:\n{0}".format(data))

with open("./stopwords.txt",'r', encoding="utf-8") as fp:
    stop_word = set(fp.read().split())
    print(stop_word)
    for wd in stop_word:
        for file in data:
            if wd in data[file]:
                data[file].remove(wd)

print("\n\nafter remove stop words,data:\n{0}".format(data))


words_set = set()
for file in data:
    words_set = set.union(words_set, set(data[file]))

print("\n\n",words_set)


total_occur = {}
for word in words_set:
    for file in data:
        n = data[file].count(word)
        print("\"{0}\" occurs in {1} {2} times\n".format(word,file, n))
        if word in total_occur:
            total_occur[word] = total_occur[word] +  n
        else:
            total_occur[word] = n

print(total_occur)


