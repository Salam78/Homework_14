class MainClass:
    def __init__(self, text):
        self._text = text

    def set_text(self, text=''):
        self._text = text

    def get_text(self):
        return self._text


class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self._number = number

    def set_number(self, number):
        self._number = number

    def get_number(self):
        return self._number



main_obj = MainClass("Привет Мир")
print(main_obj.get_text())

main_obj.set_text("Здравствуйте все")
print(main_obj.get_text())

child_obj = ChildClass("Все хорошо", 654321)
print(child_obj.get_text())
print(child_obj.get_number())

child_obj.set_text("Все нормально")
child_obj.set_number(123456)
print(child_obj.get_text())
print(child_obj.get_number())

