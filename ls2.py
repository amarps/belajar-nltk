# stop words 
# preprocessing remove words that dont realy have meaning

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "Yeah, that’s true, but I sometimes feel like our relationship is more one-sided."
stop_words = set(stopwords.words("english"))

# print(stop_words)

words = word_tokenize(example_sentence)

filtered_sentence = [word for word in words if not word in stop_words]

print(filtered_sentence)