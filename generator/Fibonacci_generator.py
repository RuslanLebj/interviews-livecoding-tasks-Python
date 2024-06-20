# class FibonacciGenerator:
#     def __init__(self):
#         self.prev = 0
#         self.cur = 1
#
#     def __next__(self):
#         result = self.prev
#         self.prev, self.cur = self.cur, self.prev + self.cur
#         return result
#
#     def __iter__(self):
#         return self
#
#
# for i in FibonacciGenerator():
#     print(i)
#
#     if i > 100:
#         break

# Используя ключевое слово yield можно сильно упростить реализацию:

def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur


for i in fibonacci():
    print(i)
    if i > 100:
        break
