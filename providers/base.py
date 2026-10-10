from abc import ABC, abstractmethod

from models import SearchResult


class SearchProvider(ABC):
    name: str

    @abstractmethod
    async def search(self, query: str) -> list[SearchResult]:
        ...