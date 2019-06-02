class Stack:
    # 构造一个栈的容器
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def front(self):
        return self.__list[self.size()-1]

    def size(self):
        return len(self.__list)

    def get_last_second(self):
        return self.__list[self.size()-2]