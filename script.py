import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# add a for loop that will print the titles within the bookshelf of small books
for book in bookshelf:
    print(book['title_lower'])


# add a sort comparison function for sorting by title
def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']


# sort the bookshelf by title using bubble sort
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

for book in sort_1:
    print(book['title'])


# add a sort comparison function for sorting by author's full name
def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']


# create a new copy of the bookshelf data
bookshelf_v1 = bookshelf.copy()


# sort the bookshelf by author's full name using bubble sort
sort_2 = sorts.bubble_sort(bookshelf, by_author_ascending)

for book in sort_2:
    print(book['author'])