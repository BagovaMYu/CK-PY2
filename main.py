class Book:
    """ Базовый класс книги."""
    def __init__(self, name: str, author: str):
        """
        :param name: название книги
        :param author: автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает имя автора книги."""
        return self._author

    def __str__(self):
        return f'Книга "{self.name}". Автор {self.author}.'


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        :param name: название книги
        :param author: автор книги
        :param pages: количество страниц в книге
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц книги."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """
        Устанавливает количество страниц в книге.

        :param pages: количество страниц в книге
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __str__(self):
        return f'{super().__str__()} Количество страниц {self.pages}.'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        :param name: название аудиокниги
        :param author: автор аудиокниги
        :param duration: продожительность аудиокниги
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """
        Устанавливает продолжительность аудиокниги.

        :param duration: продолжительность аудиокниги
        """
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
        self._duration = duration

    def __str__(self):
        return f'{super().__str__()} Продолжительность {self.duration}.'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
