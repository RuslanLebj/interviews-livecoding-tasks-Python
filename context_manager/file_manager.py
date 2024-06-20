# На контекстный менеджер возлагается 2 функции:
# Что нужно сделать в момент когда необходим доступ к ресурсу
# Что нужно сделать когда доступ уже не нужен

# Встроенная функция open открывает и закрывает объект

# Контекстные менеджеры упрощают запись блоков try-finally.
# Оператор with позволяет разработчикам писать свой код в сжатом и понятном виде.

# Пример менеджера контекста для открытия файла:
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print("Error: File not found")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with FileManager("file.txt", "r") as f:
    if f:
        print(f.read())
