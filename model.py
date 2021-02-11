class Movie:

    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.__year = year
        self.__duration = duration
        self.__likes = 0

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, value):
        self.__name = value.title()

    @property
    def year(self):
        return self.__year

    @property
    def duration(self):
        return self.__duration

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1


class Series:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.__year = year
        self.__seasons = seasons
        self.__likes = 0

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, value):
        self.__name = value.title()

    @property
    def year(self):
        return self.__year

    @property
    def seasons(self):
        return self.__seasons

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1


avengers = Movie(name="avengers teste", year=2018, duration=160)
print(f'Nome: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration}, - Likes: {avengers.likes}')

atlanta = Series(name="Atlanta", year=2018, seasons=2)
print(f'Nome: {atlanta.name} - Year: {atlanta.year} - Seasons: {atlanta.seasons} - Likes: {atlanta.likes}')
