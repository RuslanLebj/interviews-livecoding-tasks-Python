# Задание 1:

# Пример совместного использования *args и **kwargs\
def print_args_kwargs(*args, **kwargs):
    print("Аргументы позиционные:")
    for arg in args:
        print(arg)
    print("Аргументы именованные:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("\nЗадание 1:")
# Пример использования:
print_args_kwargs(1, 2, 3, name="Kekatel", age=30)


# Задание 2:

# Написать функцию concatenate_strings, которая принимает произвольное количество строковых аргументов через *args
# и произвольное количество именованных аргументов через **kwargs.
# Функция должна конкатенировать все строки из *args и все значения из **kwargs в одну строку и возвращать её.
def concatenate_strings(*args, **kwargs):
    # Создаем пустой список для хранения всех строк
    result = []
    # Добавляем все позиционные аргументы в список
    for arg in args:
        result.append(arg)
    # Добавляем все значения из именованных аргументов в список
    for key, value in kwargs.items():
        result.append(value)
    # Конкатенируем все строки в списке и возвращаем результат
    return ''.join(result)


print("\nЗадание 2:")
# Пример использования:
print(concatenate_strings("Some", " ", "body", " once told me", exclamation="!!!", question="???"))


# Задание 3:

# Напишите функцию describe_arguments, которая принимает произвольное количество позиционных и именованных аргументов.
# Функция должна возвращать строку, которая описывает количество позиционных и именованных аргументов, а также сами аргументы.
def describe_arguments(*args, **kwargs):
    # Считаем количество позиционных аргументов
    num_args = len(args)
    # Считаем количество именованных аргументов
    num_kwargs = len(kwargs)
    # Возвращаем строку с описанием аргументов
    return f"Позиционных аргументов: {num_args}, Именованных аргументов: {num_kwargs}, args: {args}, kwargs: {kwargs}"


print("\nЗадание 3:")
# Пример использования:
print(describe_arguments(1, 2, 3, a=4, b=5))
