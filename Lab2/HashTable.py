class HashTable():
    def __init__(self, size=100):
        self.size = size
        self.hashmap = [[] for _ in range(size)]

    def __str__(self):
        result = ""
        for i, lst in enumerate(self.hashmap):
            result += f"Key {i} -> {list}\n"

    def _hash(self, key):
        return hash(key) % self.size

    def _get_index_and_bucket(self, key):
        index = self._hash(key)
        bucket = self.hashmap[index]
        return index, bucket

    def _raise_key_error(self):
        raise KeyError("Key not found !")

    def put(self, key):
        index, bucket = self._get_index_and_bucket(key)
        try:
            self.get(key)
            return
        except KeyError:
            bucket.append(key)

    def contains(self, key):
        index, bucket = self._get_index_and_bucket(key)
        for curr_key in bucket:
            if curr_key == key:
                return True
        self._raise_key_error()

    def remove(self, key):
        index, bucket = self._get_index_and_bucket(key)
        if key in bucket:
            bucket.remove(key)
        else:
            self._raise_key_error()

    def pos(self, key):
        """
        This returns
        :param key: key to search in the hashmap
        :return: (hashmap_pos, hashmap_list_pos)
        """
        index, bucket = self._get_index_and_bucket(key)
        for i, curr_key in enumerate(bucket):
            if curr_key == key:
                return index, i
        self._raise_key_error()


