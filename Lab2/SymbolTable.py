from Lab2.HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        """
        Initializes a new symbol table with the specified size.

        :param size: The size of the symbol table.
        """
        self.__ht = HashTable(size)

    def __str__(self):
        """
        Returns a string representation of the symbol table.

        :return: String representation of the symbol table.
        """
        return f"Your Symbol Table :\n{self.__ht}"

    def __contains__(self, key):
        """
        Checks if the symbol is present in the symbol table.

        :param key: The symbol (identifier) to be checked.
        :return: True if the symbol is found, False otherwise.
        """
        try:
            self.__ht.contains(key)
            return True
        except KeyError:
            return False

    def add(self, key):
        """
        Adds a symbol to the symbol table.

        :param key: The symbol (identifier) to be added.
        """
        self.__ht.put(key)

    def remove(self, key):
        """
        Removes a symbol from the symbol table.

        :param key: The symbol (identifier) to be removed.
        """
        self.__ht.remove(key)

    def pos(self, key):
        """
        Returns the position of the given symbol in the symbol table.

        :param key: The symbol (identifier) to be searched.
        :return: A tuple (hashmap_pos, hashmap_list_pos) indicating the position of the symbol.
        """
        return self.__ht.pos(key)

    def get(self, key):
        """
        Checks if the symbol is present in the symbol table.

        :param key: The symbol (identifier) to be checked.
        :return: True if the symbol is found, False otherwise.
        """
        self.__ht.pos(key)

