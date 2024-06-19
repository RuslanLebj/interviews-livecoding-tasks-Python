# Задание 1:

# Напишите функцию is_hashable, которая принимает один аргумент и возвращает True, если аргумент хэшируем, и False в противном случае.

def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False


def test_is_hashable():
    # Примитивные типы данных
    print("int:", is_hashable(42))  # True
    print("float:", is_hashable(3.14))  # True
    print("complex:", is_hashable(1+2j))  # True
    print("bool:", is_hashable(True))  # True
    print("NoneType:", is_hashable(None))  # True
    print("str:", is_hashable("hello"))  # True

    # Кортежи (tuple)
    print("tuple:", is_hashable((1, 2, 3)))  # True
    print("nested tuple:", is_hashable((1, (2, 3))))  # True
    print("tuple with list:", is_hashable((1, [2, 3])))  # False

    # Списки (list)
    print("list:", is_hashable([1, 2, 3]))  # False

    # Словари (dict)
    print("dict:", is_hashable({'a': 1, 'b': 2}))  # False

    # Множества (set и frozenset)
    print("set:", is_hashable(set([1, 2, 3])))  # False
    print("frozenset:", is_hashable(frozenset([1, 2, 3])))  # True

    # Объекты пользовательских классов
    class MyClass:
        pass

    obj = MyClass()
    print("custom class instance:", is_hashable(obj))  # True

    # Функции
    def my_function():
        pass

    print("function:", is_hashable(my_function))  # True

    # Bytes и bytearray
    print("bytes:", is_hashable(b"hello"))  # True
    print("bytearray:", is_hashable(bytearray(b"hello")))  # False

    # Нумерические типы из numpy
    try:
        import numpy as np
        print("numpy int:", is_hashable(np.int32(42)))  # True
        print("numpy array:", is_hashable(np.array([1, 2, 3])))  # False
    except ImportError:
        print("numpy is not installed")


# Запуск тестов
test_is_hashable()