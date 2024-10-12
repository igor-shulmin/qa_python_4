import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_same_books_add_only_one(self):
        collector = BooksCollector()

        collector.add_new_book('Название_книги_1')
        collector.add_new_book('Название_книги_1')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', 'Название книги превышает допустимую длину в 40 символов'])
    def test_add_new_book_incorrect_name_error(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_choose_genre_from_list(self):
        collector = BooksCollector()

        collector.add_new_book('Название_книги_1')
        collector.set_book_genre('Название_книги_1', 'Фантастика')

        assert collector.get_books_genre() == {'Название_книги_1': 'Фантастика'}

    def test_set_book_genre_choose_genre_not_from_list_error(self):
        collector = BooksCollector()

        collector.add_new_book('Название_книги_1')
        collector.set_book_genre('Название_книги_1', 'Нон фикшн')

        assert collector.get_books_genre() == {'Название_книги_1': ''}

    def test_get_book_genre_book_with_genre_get_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Название_книги_1')
        collector.set_book_genre('Название_книги_1', 'Фантастика')

        assert collector.get_book_genre('Название_книги_1') == 'Фантастика'

    def test_get_book_genre_book_with_no_genre_get_empty_string(self):
        collector = BooksCollector()

        collector.add_new_book('Название_книги_1')

        assert collector.get_book_genre('Название_книги_1') == ''

    def test_get_books_with_specific_genre_get_list_with_genre_filter(self):
        collector = BooksCollector()

        collector.add_new_book('Название_книги_1')
        collector.set_book_genre('Название_книги_1', 'Детективы')
        collector.add_new_book('Название_книги_2')
        collector.set_book_genre('Название_книги_2', 'Детективы')

        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    @pytest.mark.parametrize('name, genre', [['Название_книги_1', 'Мультфильмы'], ['Название_книги_2', 'Комедии']])
    def test_get_books_for_children_not_from_age_rating_get_list(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == [name]

    @pytest.mark.parametrize('name, genre', [['Название_книги_1', 'Ужасы'], ['Название_книги_2', 'Детективы']])
    def test_get_books_for_children_from_age_rating_get_empty_list(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_add_same_two_books_add_only_one(self):
        collector = BooksCollector()

        collector.add_new_book('Название_книги_1')
        collector.add_book_in_favorites('Название_книги_1')
        collector.add_book_in_favorites('Название_книги_1')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_book_get_empty_list(self):
        collector = BooksCollector()

        collector.add_new_book('Название_книги_1')
        collector.add_book_in_favorites('Название_книги_1')
        collector.delete_book_from_favorites('Название_книги_1')

        assert len(collector.get_list_of_favorites_books()) == 0
