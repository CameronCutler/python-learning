import random


quotes = (
	("To be, or not to be: that is the question.", "William Shakespeare"),
	("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.", "Jane Austen"),
	("It was the best of times, it was the worst of times.", "Charles Dickens"),
	("All that we see or seem is but a dream within a dream.", "Edgar Allan Poe"),
	("The proper study of mankind is man.", "Alexander Pope"),
	("Hope is the thing with feathers that perches in the soul.", "Emily Dickinson"),
	("Knowledge is power.", "Francis Bacon"),
	("I think, therefore I am.", "Rene Descartes"),
	("The only way to have a friend is to be one.", "Ralph Waldo Emerson"),
	("It is never too late to be what you might have been.", "George Eliot"),
)

quote, author = random.choice(quotes)
print(f'"{quote}" - {author}')
