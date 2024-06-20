# Что такое slots?

* Классы хранят поля и их значения в секретном словаре __dict__. Поскольку словарь – изменяемая структура, вы можете на лету добавлять и удалять из класса поля. Параметр __slots__ в классе жестко фиксирует набор полей класса. Слоты используются когда у класса может быть очень много полей, например, в некоторых ORM, либо когда критична производительность, потому что доступ к слоту срабатывает быстрее, чем поиск в словаре, или когда в процессе выполнения программы создаются миллионы экземпляров класса, применение __slots__ позволит сэкономить память.

* Слоты активно используются в библиотеках requests и falcon.

* Недостатотк: нельзя присвоить классу поле, которого нет в слотах. Не работают методы __getattr__ и __setattr__. Решение: включить в __slots__ элемент __dict__

## Это магический метод, который позволяет нам иметь только заданный набор атрибутов в экземпляре класса.

```
class PointSlots:

    __slots__ = ('x','y') # Перечисляем все возможные атрибуты экземпляров класса
                          
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### Плюсы:

**Фиксированность** 
* После указания __slots__ добавление новых атрибутов в экземпляр класса, кроме уже указанных, невозможно

**Скорость работы программы**
* Используемая коллекция для хранения имён переменных в slots позволяет ускорить работу программы

**Использование памяти**
* Уменьшение количества занимаемой памяти при использовании __slots_ связано с тем, что в __slots__ хранятся только значения из пространства имён