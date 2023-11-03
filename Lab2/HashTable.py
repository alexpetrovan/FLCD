from typing import Tuple


class HashTable:
    def __init__(self, size=100):
        """
        Initializes a new hash table with the specified size.

        :param size: The size of the hash table. Default is 100.
        """
        self.size = size
        self.hashmap = [[] for _ in range(size)]

    def __str__(self):
        """
        Returns a string representation of the hash table.

        :return: String representation of the hash table.
        """
        result = ""
        for i, lst in enumerate(self.hashmap):
            if lst:
                result += f"Key {i} -> {lst}\n"
        return result

    def _hash(self, key):
        """
        Computes the hash value for the given key.

        :param key: The key to be hashed.
        :return: The hash value.
        """
        return hash(key) % self.size

    def _get_index_and_bucket(self, key):
        """
        Returns the index and the bucket list for the given key.

        :param key: The key for which index and bucket are needed.
        :return: A tuple (index, bucket) indicating the index in the hash table and the bucket list.
        """
        index = self._hash(key)
        bucket = self.hashmap[index]
        return index, bucket

    def _raise_key_error(self):
        """
        Raises a KeyError indicating that the key was not found in the hash table.
        """
        raise KeyError("Key not found !")

    def put(self, key):
        """
        Inserts a key into the hash table.

        :param key: The key to be inserted.
        """
        index, bucket = self._get_index_and_bucket(key)
        try:
            self.contains(key)
            return
        except KeyError:
            bucket.append(key)

    def contains(self, key) -> bool:
        """
        Checks if the hash table contains the given key.

        :param key: The key to be checked.
        :return: True if the key is found, False otherwise.
        """
        index, bucket = self._get_index_and_bucket(key)
        for curr_key in bucket:
            if curr_key == key:
                return True
        self._raise_key_error()

    def remove(self, key):
        """
        Removes the specified key from the hash table.

        :param key: The key to be removed.
        """
        index, bucket = self._get_index_and_bucket(key)
        if key in bucket:
            bucket.remove(key)
        else:
            self._raise_key_error()

    def pos(self, key) -> Tuple[int, int]:
        """
        Returns the position of the given key in the hash table.

        :param key: The key to be searched.
        :return: A tuple (hashmap_pos, hashmap_list_pos) indicating the position of the key.
        """
        index, bucket = self._get_index_and_bucket(key)
        for i, curr_key in enumerate(bucket):
            if curr_key == key:
                return index, i
        self._raise_key_error()


