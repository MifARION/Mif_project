class Key(object):
    def __init__(self, data=''):
        self.data = data

    def __eq__(self, another):
        return hasattr(another, 'data') and self.data == another.data   # __eq__Позволяет реализовать проверку на
        # равенство
        # для экземпляров пользовательских типов.

    def __hash__(self):       # __hash__ Позволяет настраивать хеширование объектов, а также управлять его возможностью.
        return hash(self.data)


a1, a2, a3 = Key('foo'), Key('foo'), Key('bar')
d = {a1: 'foo'}


