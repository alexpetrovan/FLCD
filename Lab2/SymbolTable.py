from HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__ht = HashTable(size)

    def __str__(self):
        return f"Your Symbol Table :\n{str(self.__ht)}"

    def __contains__(self, key):
        try:
            self.__ht.contains(key)
            return True
        except KeyError:
            return False

    def add(self, key):
        self.__ht.put(key)

    def remove(self, key):
        self.__ht.remove(key)

    def pos(self, key):
        self.__ht.get_pos(key)

    def get(self, key):
        self.__ht.get_pos(key)

