# wordnet larges corpus

from nltk.corpus import wordnet

syns = wordnet.synsets("sex")


print(syns)

# synonim set
print(syns[0].name())

# word
print(syns[0].lemmas()[0].name())

# definition
print(syns[0].definition())

# examples
print(syns[0].examples())

# antonim
print(syns[0].lemmas()[0].antonyms())


# similarity checker
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("sex.n.01")
w2 = wordnet.synset("fuck.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("god.n.01")
print(w1.wup_similarity(w2))