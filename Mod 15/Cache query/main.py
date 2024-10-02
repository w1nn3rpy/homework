from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = OrderedDict()

    @property
    def cache(self):  # этот метод должен возвращать самый старый элемент
        if not self._cache:
            return None

        oldest_key = next(iter(self._cache))
        return oldest_key, self._cache[oldest_key]

    @cache.setter
    def cache(self, new_elem):  # этот метод должен добавлять новый элемент
        key, value = new_elem
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self.capacity:
            self._cache.popitem(last=False)

    def get(self, key):
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        return None

    def print_cache(self):
        print('LRU Cache:\n')
        for key, value in self._cache.items():
            print(f'{key}: {value}')


# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)
# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3
# Получаем значение по ключу
print(cache.get("key2"))  # value2
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")
# Выводим обновлённый кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
