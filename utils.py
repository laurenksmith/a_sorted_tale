import csv


# This code loads the current bookshelf data from the csv file
def load_books(filename):
    bookshelf = []
    with open(filename) as file:
        shelf = csv.DictReader(file)
        for book in shelf:
            # make all characters lowercase, so when sorting, not confused by eg fact that ord("c") > ord("D") is True
            book['author_lower'] = book['author'].lower()
            book['title_lower'] = book['title'].lower()
            bookshelf.append(book)
    return bookshelf
