import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# add a for loop that will print the titles within the bookshelf of small books
book: str
for book in bookshelf:
    print(book['title_lower'])


