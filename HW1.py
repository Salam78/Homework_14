from abc import ABC, abstractmethod

class BaseClass(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def set_value(self):
        pass

class MainClass(BaseClass):
    def __init__(self, text):
        self._text = text

    def set_value(self, text=''):
        self._text = text

    def get_value(self):
        return self._text

class ChildClass(BaseClass):
    def __init__(self, text, number):
        self._text = text
        self._number = number

    def set_value(self, text='', number=0):
        self._text = text
        self._number = number

    def get_value(self):
        return self._text, self._number


main_obj = MainClass("Привет Мир")
print(main_obj.get_value())

main_obj.set_value("Здравствуйте все")
print(main_obj.get_value())

child_obj = ChildClass("Все хорошо", 98765)
print(child_obj.get_value())

child_obj.set_value("Все нормально", 12345)
print(child_obj.get_value())

