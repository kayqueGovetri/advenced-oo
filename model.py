class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self._year = year
        self._likes = 0

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        self._name = value.title()

    @property
    def year(self):
        return self._year

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1


class Movie(Program):

    def __init__(self, duration, name, year):
        super().__init__(name=name, year=year)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration


class Series(Program):
    def __init__(self, seasons, name, year):
        super().__init__(name=name, year=year)
        self.__seasons = seasons

    @property
    def seasons(self):
        return self.__seasons


avengers = Movie(name="avengers teste", year=2018, duration=160)
print(f'Nome: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration}, - Likes: {avengers.likes}')

atlanta = Series(name="Atlanta", year=2018, seasons=2)
print(f'Nome: {atlanta.name} - Year: {atlanta.year} - Seasons: {atlanta.seasons} - Likes: {atlanta.likes}')
