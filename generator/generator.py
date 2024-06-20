# Выражение генератор (Generator Expressions):
my_generator = (i for i in range(10))
print(my_generator)  # <generator object <genexpr> at ________>


# Функция генератор:
# Для возврата значения функция использует не return a yield
# - главное отличие yield от return это то, что yield, после возврата объекта, сохраняет стек генератора,
# так что при следующем вызове функции next() от генератора, исполнение кода генератора продолжится с того момента,
# где yield вернул объект в прошлый раз.


def generator():
    for i in range(2):
        yield i


# Пример работы 1:
a = generator()
print("Пример 1:")
print(next(a))  # 0
print(next(a))  # 1
# print(next(a))  # StopIteration

# Пример работы 2:
a = generator()
print("Пример 2:")
for i in a:
    print(i)
# 1
# 2


# Реализация генератора чисел Фибоначчи с помощью готовой функции с ключевым словом yield:
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print("Числа Фибоначчи:")
for x in fibon(10):
    print(x)
