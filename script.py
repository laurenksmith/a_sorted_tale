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

# create a second copy of the bookshelf data
bookshelf_v2 = bookshelf.copy()


# use quicksort on bookshelf_v2 by author ascending
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in bookshelf_v2:
    print(book['author'])


# add a new comparison function to sort the books by the length of the sum of the number of characters in the book as
# well as the author's name
def by_total_length(book_a, book_b):
    return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])