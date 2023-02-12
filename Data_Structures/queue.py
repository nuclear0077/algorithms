# Создадим свой класс Queue. У объектов этого класса будут поля:
# head — индекс, по которому нужно извлекать элемент, если очередь не пустая;
# tail — индекс, по которому нужно добавлять элемент, если в очереди есть место;
# max_n — максимально возможное количество элементов в очереди;
# size — размер очереди.

# - `push(item)` — добавляет элемент в конец очереди;
# - `pop()` — берёт элемент из начала очереди и удаляет его;
# - `peek()` — берёт элемент из начала очереди без удаления;
# - `size()` — возвращает количество элементов в очереди.

class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x