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

    def __str__(self):
        return f"{self._name} - {self.year} - {self.likes} Likes"

    def __repr__(self):
        return f"Program(_name='{self._name}', year='{self.year}', likes='{self.likes}')"


class Movie(Program):

    def __init__(self, duration, name, year):
        super().__init__(name=name, year=year)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        return f"{self._name} - {self.year} - {self.__duration}- {self.likes} Likes"

    def __repr__(self):
        return f"Program(_name='{self._name}', year='{self.year}', likes='{self.likes}', duration='{self.duration}')"


class Series(Program):
    def __init__(self, seasons, name, year):
        super().__init__(name=name, year=year)
        self.__seasons = seasons

    @property
    def seasons(self):
        return self.__seasons

    def __str__(self):
        return f"{self._name} - {self.year} - {self.__seasons}- {self.likes} Likes"

    def __repr__(self):
        return f"Program(_name='{self._name}', year='{self.year}', likes='{self.likes}', __seasons='{self.__seasons}')"


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    @property
    def list(self):
        return self._programs

    @property
    def length(self):
        return len(self._programs)


avengers = Movie(name="avengers teste", year=2018, duration=160)
atlanta = Series(name="Atlanta", year=2018, seasons=2)
everyone = Movie(name="everyone", year=199, duration=100)
demolich = Series(name="demolich", year=2016, seasons=3)

movies_and_series = [avengers, atlanta, demolich, everyone]

playlist = Playlist(name="programs2021", programs=movies_and_series)

for program in playlist.list:
    print(program)

