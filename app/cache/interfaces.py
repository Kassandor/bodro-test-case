from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import Any


@dataclass
class ICachedObject(ABC):
    """

    """

    key: str
    value: Any
    ttl: int | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def is_expired(self) -> bool:
        """

        :return:
        """
        if self.ttl is None:
            return False
        return datetime.now(timezone.utc) > self.created_at + timedelta(seconds=self.ttl)


class ICacheDB(ABC):
    """

    """

    @abstractmethod
    def get(self, key: str) -> ICachedObject | None:
        pass

    @abstractmethod
    def put(self, obj: ICachedObject):
        pass

    @abstractmethod
    def delete(self, key: str):
        pass
