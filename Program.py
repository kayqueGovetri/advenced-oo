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