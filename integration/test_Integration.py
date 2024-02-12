from library import Library
#Testing the valid scenario for add_book()
def test_add_book():
    library = Library()
    book = "The Famous Five"
    library.add_book(book)
    assert library.is_book_available(book) == True

#Testing the invalid scenario for is_book_available()
def test_is_book_available():
    library = Library()
    book ="Harry Potter"
    assert library.is_book_available(book) == True