from Класс_Book import Book, BOOKS_DATABASE


class Library:
    """Класс "Библиотека"
    """
    def __init__(self, books: list[Book] = None):
        """
        :param books: список книг
        """
        self.books = [] if books is None else books

    def get_books_id_list(self) -> list:
        """
        Создание списка индентификаторов книг на основе полученного списка книг

        :return: список id книг
        """
        return [book.id_ for book in self.books]

    def get_next_book_id(self) -> int:
        """
        Получение индентификатора для добавления новой книги в библиотеку

        :return: id для новой книги
        """
        if not self.books:
            return 1
        else:
            return max(self.get_books_id_list()) + 1

    def get_index_by_book_id(self, id_) -> int:
        """
        Получение индекса книги в списке книг библиотеки по ее индентификатору

        :param id_: индентификатор требуемой книги
        :return: индекс книги в списке
        """
        if id_ not in self.get_books_id_list():
            raise ValueError("Книги с запрашиваемым id не существует")
        return self.get_books_id_list().index(id_)


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
