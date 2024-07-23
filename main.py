class MoviesLibrary:
    def __init__(self, genres):
        self.data = {}
        for genre in genres:
            self.data[genre] = []

    def add_movie(self, genre, title):
        self.data[genre].append(title)

    def recommend(self, genre):
        return self.data[genre]


if __name__ == '__main__':
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    library.add_movie('Комедия', 'Весёлый питонист')
    library.add_movie('Комедия', 'Три разраба и тестировщик')

    print(library.recommend('Комедия'))