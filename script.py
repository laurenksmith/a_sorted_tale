import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# add a for loop that will print the titles within the bookshelf of small books
for book in bookshelf:
    print(book['title_lower'])


# add a sort comparison function
def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

