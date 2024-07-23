import unittest
class MoviesLibrary:
    def __init__(self, genres):
        self.data = {}
        for genre in genres:
            self.data[genre] = []

    def add_movie(self, genre, title):
        self.data[genre].append(title)

    def recommend(self, genre):
        return self.data[genre]


class TestMoviesLibrary(unittest.TestCase):

    def setUp(self):
        self.library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    def test_initialization(self):
        # Проверка, что все жанры присутствуют в библиотеке
        self.assertIn('Ужасы', self.library.data)
        self.assertIn('Комедия', self.library.data)
        self.assertIn('Романтика', self.library.data)

    def test_add_movie(self):
        # Добавление фильмов и проверка, что они добавлены
        self.library.add_movie('Комедия', 'Весёлый питонист')
        self.assertIn('Весёлый питонист', self.library.data['Комедия'])

        self.library.add_movie('Комедия', 'Три разраба и тестировщик')
        self.assertIn('Три разраба и тестировщик', self.library.data['Комедия'])

    def test_recommend_isolated_genres(self):
        # Проверка, что фильмы добавляются только в соответствующий жанр
        self.library.add_movie('Комедия', 'Весёлый питонист')
        self.library.add_movie('Комедия', 'Три разраба и тестировщик')
        self.library.add_movie('Ужасы', 'Страшилки 1')

        self.assertEqual(self.library.recommend('Комедия'), ['Весёлый питонист', 'Три разраба и тестировщик'])
        self.assertEqual(self.library.recommend('Ужасы'), ['Страшилки 1'])
        self.assertEqual(self.library.recommend('Романтика'), [])


if __name__ == '__main__':
    unittest.main()












