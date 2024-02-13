from library import Library

#Integration testcase to search the availability of a  book after adding
def test_add_book():
    library = Library()
    book1 = "The Famous Five"
    library.add_book(book1)
    assert library.is_book_available(book1) == True

#Integration testcase to search the availability of a book after removing
def test_is_book_available():
    library = Library()
    book2 ="Harry Potter"
    library.add_book(book2);
    library.remove_book(book2);
    assert library.is_book_available(book2) == True
