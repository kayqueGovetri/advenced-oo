from Program import Program


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