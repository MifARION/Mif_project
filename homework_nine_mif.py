import operator


class HomeLibrary:
    books = []
    by_author = []
    books_year = []

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def add_book(self):
        HomeLibrary.books.append((self.name, self.author, self.year))

    def del_book(self):
        HomeLibrary.books.remove((self.name, self.author, self.year))

    def search_book_name(self, name):
        for book in HomeLibrary.books:
            if book[0] == name:
                return book

    def search_book_author(self, author):
        for book in HomeLibrary.books:
            if book[1] == author:
                HomeLibrary.by_author.append(book)
        return HomeLibrary.by_author

    def search_year(self, year):
        for book in HomeLibrary.books:
            if book[2] == year:
                HomeLibrary.books_year.append(book)
        return HomeLibrary.books_year

    def sort_name(self):
        return sorted(self.books)

    def sort_year(self):
        return sorted(HomeLibrary.books, key=operator.itemgetter(2))

    def sort_author(self):
        return sorted(self.books, key=operator.itemgetter(1))


book = HomeLibrary('Нутрициология', 'Лола Тэйлор', 3000)
book.add_book()
book = HomeLibrary('Теория струн', 'Саша Грэй', 1999)
book.add_book()
book = HomeLibrary('Квантовая механика', 'Кэтрин Тэкила', 2004)
book.add_book()
book = HomeLibrary('Психология по Фрэйду', 'Элли Бриэлсон', 2015)
book.add_book()

# book = HomeLibrary('Теория струн', 'Саша Грэй', 1999)
# book.del_book()
print(book.search_year(2004))
print(book.search_book_author('Саша Грэй'))
print(book.search_book_name('Нутрициология'))
print(book.books)
print(book.sort_name())
print(book.sort_year())
print(book.sort_author())
