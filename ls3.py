# stemming

# i was taking a ride in the car
# i was riding in the car

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

for word in example_words:
	print(ps.stem(word))