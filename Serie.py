from Program import Program


class Serie(Program):
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
