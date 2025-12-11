from datetime import datetime, timezone

from app.cache.interfaces import ICacheDB, ICachedObject


class InMemoryCacheDB(ICacheDB):
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
        obj.created_at = datetime.now(timezone.utc)
        self.storage[obj.key] = obj

    def delete(self, key: str):
        if key in self.storage:
            del self.storage[key]
