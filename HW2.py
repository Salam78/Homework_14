class Roman:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(to_roman(from_roman(self.value) + from_roman(other.value)))
        elif isinstance(other, int):
            return Roman(to_roman(from_roman(self.value) + other))
        else:
            raise TypeError("Неподдерживаемый тип операнда")

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(to_roman(from_roman(self.value) - from_roman(other.value)))
        elif isinstance(other, int):
            return Roman(to_roman(from_roman(self.value) - other))
        else:
            raise TypeError("Неподдерживаемый тип операнда")

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(to_roman(from_roman(self.value) * from_roman(other.value)))
        elif isinstance(other, int):
            return Roman(to_roman(from_roman(self.value) * other))
        else:
            raise TypeError("Неподдерживаемый тип операнда")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(to_roman(from_roman(self.value) // from_roman(other.value)))
        elif isinstance(other, int):
            return Roman(to_roman(from_roman(self.value) // other))
        else:
            raise TypeError("Неподдерживаемый тип операнда")

    @staticmethod
    def to_roman(number):

        pass

    @staticmethod
    def from_roman(roman):

        pass


    x = Roman("X")
    v = Roman("V")

    result1 = x + v
    print(result1)

    result2 = x - 3
    print(result2)

    result3 = v * 2
    print(result3)

    result4 = x / 2
    print(result4)



