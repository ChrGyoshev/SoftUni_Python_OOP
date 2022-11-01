from functools import reduce
class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce((lambda x,y: x * y), args)

    @staticmethod
    def divide(*args):
        return reduce((lambda x,y: x / y), args)

    @staticmethod
    def subtract(*args):
        return reduce((lambda x,y: x - y), args)
