from cache.interfaces import ICacheDB, ICachedObject


class CachedObject(ICachedObject):
    """
    Кэшированный объект
    """
    pass


class InMemoryCacheDB(ICacheDB):
    """
    In memory кэш
    """

    def __init__(self):
        self.storage: dict[str, ICachedObject] = {}

    def get(self, key: str):
        obj = self.storage.get(key)
        if obj is None:
            return None
        if obj.is_expired():
            self.delete(key)
            return None
        return obj

    def put(self, obj: ICachedObject):
        if not isinstance(obj, ICachedObject):
            raise TypeError('Нужен ICachedObject объект')
        self.storage[obj.key] = obj

    def delete(self, key: str):
        if key in self.storage:
            del self.storage[key]


cache = InMemoryCacheDB()