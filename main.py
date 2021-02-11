from Movie import Movie
from Serie import Serie
from Playlist import Playlist

avengers = Movie(name="avengers teste", year=2018, duration=160)
atlanta = Serie(name="Atlanta", year=2018, seasons=2)
everyone = Movie(name="everyone", year=199, duration=100)
demolich = Serie(name="demolich", year=2016, seasons=3)

movies_and_series = [avengers, atlanta, demolich, everyone]

playlist = Playlist(name="programs_2021", programs=movies_and_series)

playlist - demolich
playlist + Movie(name="Kimetsu no Yaiba", year=2018, duration=100)

for program in playlist:
    print(program)

