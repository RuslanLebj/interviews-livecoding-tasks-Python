# Пример готового контекcтного менеджера:
with open('file.txt') as f:
    data = f.read()
    print(data)


# Пример реализации своего контекстного менеджера на основе класса:
class Printable:
    def __enter__(self):
        print('enter')

    def __exit__(self, type, value, traceback):
        print('exit')


# Использование контекстного менеджера с оператором 'with'
with Printable() as p:
    print('В котнексте Printable')
