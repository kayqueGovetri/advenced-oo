

class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)

    def __add__(self, value):
        return self._programs.append(value)

    def __sub__(self, value):
        return self._programs.remove(value)
