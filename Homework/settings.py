import datetime

class settings:
    name = ''
    year = ''
    group = ''
    rating = 4

    def __init__(self, name='', year='', group='',rating=4):
        self.name = input('Введите ваше имя:')
        self.year = input('В каком году вы родились?')
        self.group = input('Введите вашу группу:')
        self.rating = rating






    def __str__(self):
        return f' == {self.name} ==\n' \
               f'Возраст: {self.year}\n' \
               f'Группа: {self.group}\n' \
               f'Средний бал: {self.rating}\n' \






